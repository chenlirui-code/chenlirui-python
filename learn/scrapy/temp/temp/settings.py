# Scrapy项目的配置文件

BOT_NAME = 'temp'

SPIDER_MODULES = ['temp.spiders']
NEWSPIDER_MODULE = 'temp.spiders'

# 遵守robots.txt规则
ROBOTSTXT_OBEY = True

# 设置Scrapy同时处理的最大并发请求数（默认为16）
# CONCURRENT_REQUESTS = 32

# 为同一网站的请求设置延迟（默认为0）
# 参考：https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# 下载延迟设置只会应用于以下一个：
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# 禁用cookies（默认启用）
# COOKIES_ENABLED = False

# 禁用Telnet控制台（默认启用）
# TELNETCONSOLE_ENABLED = False

# 覆盖默认请求头:
# DEFAULT_REQUEST_HEADERS = {
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#    'Accept-Language': 'en',
# }

# 启用或禁用Spider中间件
# 参考：https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'temp.middlewares.TempSpiderMiddleware': 543,
# }

# 启用或禁用Downloader中间件
# 参考：https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'temp.middlewares.TempDownloaderMiddleware': 543,
# }

# 启用或禁用扩展
# 参考：https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# 配置Item处理管道
# 参考：https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'temp.pipelines.TempPipeline': 300,
# }

# 启用并配置自动限速扩展（默认禁用）
# 参考：https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# 初始下载延迟
# AUTOTHROTTLE_START_DELAY = 5
# 在高延迟情况下设置的最大下载延迟
# AUTOTHROTTLE_MAX_DELAY = 60
# Scrapy应同时发送到每个远程服务器的平均请求数
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# 启用显示用于每个接收到的响应的节流统计信息：
# AUTOTHROTTLE_DEBUG = False

# 启用并配置HTTP缓存（默认禁用）
# 参考：https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 设置默认值已弃用的设置以保证未来兼容性
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
FEED_EXPORT_ENCODING = 'utf-8'
