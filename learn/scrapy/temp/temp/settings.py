# Scrapy 针对 temp 项目的设置
#
# 为了简单起见，此文件仅包含被认为重要或常用的设置。您可以通过查阅文档获取更多设置：
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "temp"  # 爬虫项目的名称

SPIDER_MODULES = ["temp.spiders"]  # 包含爬虫模块的 Python 模块的列表
NEWSPIDER_MODULE = "temp.spiders"  # 新爬虫模块的默认模块

# 通过用户代理标识您自己（和您的网站）以负责任地爬取
# USER_AGENT = "temp (+http://www.yourdomain.com)"  # 注释掉了，您可以在此设置用户代理

# 遵守 robots.txt 规则
ROBOTSTXT_OBEY = True  # 设置为 True 表示遵守

# 配置 Scrapy 执行的最大并发请求数（默认：16）
# CONCURRENT_REQUESTS = 32  # 注释掉了，您可以在此设置并发请求数

# 为同一网站的请求配置延迟（默认：0）
# 请参考 https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# 也可参考自动节流设置和文档
# DOWNLOAD_DELAY = 3  # 注释掉了，您可以在此设置下载延迟
# 下载延迟设置只会遵循以下之一：
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# 禁用 cookies（默认启用）
# COOKIES_ENABLED = False  # 注释掉了，您可以在此设置是否启用 cookies

# 禁用 Telnet 控制台（默认启用）
# TELNETCONSOLE_ENABLED = False  # 注释掉了，您可以在此设置是否启用 Telnet 控制台

# 覆盖默认的请求头：
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }  # 注释掉了，您可以在此设置默认请求头

# 启用或禁用爬虫中间件
# 请参考 https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "temp.middlewares.TempSpiderMiddleware": 543,
# }  # 注释掉了，您可以在此设置爬虫中间件

# 启用或禁用下载器中间件
# 请参考 https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "temp.middlewares.TempDownloaderMiddleware": 543,
# }  # 注释掉了，您可以在此设置下载器中间件

# 启用或禁用扩展
# 请参考 https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }  # 注释掉了，您可以在此设置扩展

# 配置项目管道
# 请参考 https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "temp.pipelines.TempPipeline": 300,
# }  # 注释掉了，您可以在此设置项目管道

# 启用并配置自动节流扩展（默认禁用）
# 请参考 https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True  # 设置为 True 启用自动节流
# 初始下载延迟
# AUTOTHROTTLE_START_DELAY = 5
# 在高延迟情况下设置的最大下载延迟
# AUTOTHROTTLE_MAX_DELAY = 60
# Scrapy 应并行发送到每个远程服务器的平均请求数
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# 启用显示每个收到的响应的节流统计信息：
# AUTOTHROTTLE_DEBUG = False

# 启用并配置 HTTP 缓存（默认禁用）
# 请参考 https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True  # 启用 HTTP 缓存
# HTTPCACHE_EXPIRATION_SECS = 0  # 缓存过期时间（秒）
# HTTPCACHE_DIR = "httpcache"  # 缓存目录
# HTTPCACHE_IGNORE_HTTP_CODES = []  # 忽略的 HTTP 状态码
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"  # 缓存存储方式

# 将默认值已弃用的设置设置为面向未来的值
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"  # 请求指纹实现的版本
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"  # 选择的 Twisted 反应堆
FEED_EXPORT_ENCODING = "utf-8"  # 输出文件的编码
