import requests

# 假设这是你的Token
token = 'your_token_here'

# 目标URL
url = 'http://example.com/api/data'

# 发送带有Token的请求
headers = {
    'Authorization': f'Token {token}',  # 注意这里的格式可能根据API的要求而不同
    'Content-Type': 'application/json',  # 根据API的要求可能会有所不同
}

response = requests.get(url, headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    # 解析数据
    data = response.json()
    print(data)
else:
    print('Failed to retrieve web.')