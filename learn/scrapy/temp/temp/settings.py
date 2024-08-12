# Scrapy ��� temp ��Ŀ������
#
# Ϊ�˼���������ļ�����������Ϊ��Ҫ���õ����á�������ͨ�������ĵ���ȡ�������ã�
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "temp"  # ������Ŀ������

SPIDER_MODULES = ["temp.spiders"]  # ��������ģ��� Python ģ����б�
NEWSPIDER_MODULE = "temp.spiders"  # ������ģ���Ĭ��ģ��

# ͨ���û������ʶ���Լ�����������վ���Ը����ε���ȡ
# USER_AGENT = "temp (+http://www.yourdomain.com)"  # ע�͵��ˣ��������ڴ������û�����

# ���� robots.txt ����
ROBOTSTXT_OBEY = True  # ����Ϊ True ��ʾ����

# ���� Scrapy ִ�е���󲢷���������Ĭ�ϣ�16��
# CONCURRENT_REQUESTS = 32  # ע�͵��ˣ��������ڴ����ò���������

# Ϊͬһ��վ�����������ӳ٣�Ĭ�ϣ�0��
# ��ο� https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# Ҳ�ɲο��Զ��������ú��ĵ�
# DOWNLOAD_DELAY = 3  # ע�͵��ˣ��������ڴ����������ӳ�
# �����ӳ�����ֻ����ѭ����֮һ��
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# ���� cookies��Ĭ�����ã�
# COOKIES_ENABLED = False  # ע�͵��ˣ��������ڴ������Ƿ����� cookies

# ���� Telnet ����̨��Ĭ�����ã�
# TELNETCONSOLE_ENABLED = False  # ע�͵��ˣ��������ڴ������Ƿ����� Telnet ����̨

# ����Ĭ�ϵ�����ͷ��
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }  # ע�͵��ˣ��������ڴ�����Ĭ������ͷ

# ���û���������м��
# ��ο� https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "temp.middlewares.TempSpiderMiddleware": 543,
# }  # ע�͵��ˣ��������ڴ����������м��

# ���û�����������м��
# ��ο� https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "temp.middlewares.TempDownloaderMiddleware": 543,
# }  # ע�͵��ˣ��������ڴ������������м��

# ���û������չ
# ��ο� https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }  # ע�͵��ˣ��������ڴ�������չ

# ������Ŀ�ܵ�
# ��ο� https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "temp.pipelines.TempPipeline": 300,
# }  # ע�͵��ˣ��������ڴ�������Ŀ�ܵ�

# ���ò������Զ�������չ��Ĭ�Ͻ��ã�
# ��ο� https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True  # ����Ϊ True �����Զ�����
# ��ʼ�����ӳ�
# AUTOTHROTTLE_START_DELAY = 5
# �ڸ��ӳ���������õ���������ӳ�
# AUTOTHROTTLE_MAX_DELAY = 60
# Scrapy Ӧ���з��͵�ÿ��Զ�̷�������ƽ��������
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# ������ʾÿ���յ�����Ӧ�Ľ���ͳ����Ϣ��
# AUTOTHROTTLE_DEBUG = False

# ���ò����� HTTP ���棨Ĭ�Ͻ��ã�
# ��ο� https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True  # ���� HTTP ����
# HTTPCACHE_EXPIRATION_SECS = 0  # �������ʱ�䣨�룩
# HTTPCACHE_DIR = "httpcache"  # ����Ŀ¼
# HTTPCACHE_IGNORE_HTTP_CODES = []  # ���Ե� HTTP ״̬��
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"  # ����洢��ʽ

# ��Ĭ��ֵ�����õ���������Ϊ����δ����ֵ
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"  # ����ָ��ʵ�ֵİ汾
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"  # ѡ��� Twisted ��Ӧ��
FEED_EXPORT_ENCODING = "utf-8"  # ����ļ��ı���
