import base64
import hashlib
import hmac
import json
import ssl
import threading
from datetime import datetime
from time import mktime
from urllib.parse import urlparse, urlencode
from wsgiref.handlers import format_date_time
import websocket


class Ws_Param:
    def __init__(self, APPID, APIKey, APISecret, gpt_url):
        self.APPID = APPID
        self.APIKey = APIKey
        self.APISecret = APISecret
        self.host = urlparse(gpt_url).netloc
        self.path = urlparse(gpt_url).path
        self.gpt_url = gpt_url

    def create_url(self):
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))

        signature_origin = "host: " + self.host + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + self.path + " HTTP/1.1"

        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()
        signature_sha_base64 = base64.b64encode(signature_sha).decode(encoding='utf-8')

        authorization_origin = f'api_key="{self.APIKey}", algorithm="hmac-sha256", headers="host date request-line", signature="{signature_sha_base64}"'
        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')

        v = {
            "authorization": authorization,
            "date": date,
            "host": self.host
        }
        url = self.gpt_url + '?' + urlencode(v)
        return url


def on_error(ws, error):
    # Disable error printout
    pass


def on_close(ws, close_status_code, close_msg):
    # Disable close printout
    ws.ready.set()  # Signal that the WebSocket is closed


def on_open(ws):
    ws.send(json.dumps(gen_params(appid=ws.appid, query=ws.query, domain=ws.domain)))


def on_message(ws, message):
    data = json.loads(message)
    code = data['header']['code']
    text = ""
    if 'choices' in data['payload']:
        choices = data['payload']['choices']
        if 'text' in choices and len(choices['text']) > 0:
            text = choices['text'][0]['content']

    ws.status_code = 200 if code == 0 else 300  # Set status code, normal is 200, exception is 300
    ws.text = text
    if code == 0 and choices.get('status') == 2:
        ws.ready.set()  # Signal that the WebSocket is closed


def gen_params(appid, query, domain):
    data = {
        "header": {
            "app_id": appid,
            "uid": "1234",
        },
        "parameter": {
            "chat": {
                "domain": domain,
                "temperature": 0.5,
                "max_tokens": 4096,
                "auditing": "default",
            }
        },
        "payload": {
            "message": {
                "text": [{"role": "user", "content": query}]
            }
        }
    }
    return data


def Spark_lite(query):
    appid = "6bcfb093"
    api_secret = "MDRjMjJmZGMwOTg0M2I1OTFiNGY3YTc0"
    api_key = "f3baabd49bc9f9720376d35c64806fd8"
    Spark_url = "ws://spark-api.xf-yun.com/v1.1/chat"
    domain = "general"

    wsParam = Ws_Param(appid, api_key, api_secret, Spark_url)
    websocket.enableTrace(False)
    wsUrl = wsParam.create_url()

    ws = websocket.WebSocketApp(wsUrl,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                on_open=on_open)
    ws.appid = appid
    ws.query = query
    ws.domain = domain

    # Use an Event to wait for the WebSocket to close
    ws.ready = threading.Event()

    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    ws.ready.wait()  # Wait for the WebSocket to close

    if hasattr(ws, 'status_code'):
        if ws.status_code == 200:
            return {"code": 200, "text": ws.text}
        elif ws.status_code == 300:
            return {"code": 300, "text": ws.text}
        else:
            return {"code": 404, "text": "Unknown error"}
    else:
        return {"code": 404, "text": "No response received"}


if __name__ == "__main__":
    result = Spark_lite("给我写一篇100字的作文")
    print("AI返回的结果:", result)
