# 在此定义您的爬虫中间件模型
#
# 请参考文档：
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals  # 从 Scrapy 导入信号

# 对于使用单个接口处理不同的项目类型很有用
from itemadapter import is_item, ItemAdapter  # 导入相关模块


class TempSpiderMiddleware:  # 定义名为 TempSpiderMiddleware 的类
    # 并非所有方法都需要定义。如果某个方法未定义，
    # Scrapy 会认为该爬虫中间件不会修改传递的对象。

    @classmethod  # 类方法
    def from_crawler(cls, crawler):  # 此方法由 Scrapy 用于创建您的爬虫
        # 这个方法用于创建中间件实例
        s = cls()  # 创建类的实例
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)  # 连接信号
        return s  # 返回实例

    def process_spider_input(self, response, spider):  # 处理爬虫输入
        # 针对每个通过爬虫中间件并进入爬虫的响应被调用。

        # 应该返回 None 或抛出异常。
        return None  # 这里返回 None

    def process_spider_output(self, response, result, spider):  # 处理爬虫输出
        # 在爬虫处理响应后，使用返回的结果调用。

        # 必须返回一个可迭代的 Request 或 item 对象。
        for i in result:  # 遍历结果
            yield i  # 生成

    def process_spider_exception(self, response, exception, spider):  # 处理爬虫异常
        # 当爬虫或 process_spider_input() 方法（来自其他爬虫中间件）引发异常时被调用。

        # 应该返回 None 或一个可迭代的 Request 或 item 对象。
        pass  # 这里未做具体处理

    def process_start_requests(self, start_requests, spider):  # 处理起始请求
        # 使用爬虫的起始请求调用，并且其工作方式类似于 process_spider_output() 方法，只是它没有相关联的响应。

        # 必须只返回请求（不是项目）。
        for r in start_requests:  # 遍历起始请求
            yield r  # 生成

    def spider_opened(self, spider):  # 当爬虫打开时
        spider.logger.info("Spider opened: %s" % spider.name)  # 记录信息


class TempDownloaderMiddleware:  # 定义名为 TempDownloaderMiddleware 的类
    # 并非所有方法都需要定义。如果某个方法未定义，
    # Scrapy 会认为该下载器中间件不会修改传递的对象。

    @classmethod  # 类方法
    def from_crawler(cls, crawler):  # 此方法由 Scrapy 用于创建您的爬虫
        # 这个方法用于创建中间件实例
        s = cls()  # 创建类的实例
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)  # 连接信号
        return s  # 返回实例

    def process_request(self, request, spider):  # 处理请求
        # 针对每个通过下载器中间件的请求被调用。

        # 必须要么：
        # - 返回 None：继续处理此请求
        # - 或返回一个 Response 对象
        # - 或返回一个 Request 对象
        # - 或抛出 IgnoreRequest：已安装的下载器中间件的 process_exception() 方法将被调用
        return None  # 这里返回 None

    def process_response(self, request, response, spider):  # 处理响应
        # 用从下载器返回的响应调用。

        # 必须要么；
        # - 返回一个 Response 对象
        # - 返回一个 Request 对象
        # - 或抛出 IgnoreRequest
        return response  # 这里返回响应

    def process_exception(self, request, exception, spider):  # 处理异常
        # 当下载处理程序或 process_request()（来自其他下载器中间件）引发异常时被调用。

        # 必须要么：
        # - 返回 None：继续处理此异常
        # - 返回一个 Response 对象：停止 process_exception() 链
        # - 返回一个 Request 对象：停止 process_exception() 链
        pass  # 这里未做具体处理

    def spider_opened(self, spider):  # 当爬虫打开时
        spider.logger.info("Spider opened: %s" % spider.name)  # 记录信息
