# 在这里定义你的Spider中间件模型
#
# 参考文档：
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# 用于使用单一接口处理不同类型Item的模块
from itemadapter import is_item, ItemAdapter


class TempSpiderMiddleware:
    # 并非所有方法都需要定义。如果未定义方法，
    # Scrapy将表现为Spider中间件不修改传递的对象。

    @classmethod
    def from_crawler(cls, crawler):
        # Scrapy用于创建Spider的方法。
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # 每个通过Spider中间件进入Spider的响应都会调用此方法。

        # 应返回None或引发异常。
        return None

    def process_spider_output(self, response, result, spider):
        # 在Spider处理响应后，处理Spider返回的结果。

        # 必须返回Request或Item对象的可迭代对象。
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # 当Spider或process_spider_input()方法（来自其他Spider中间件）引发异常时调用。

        # 应返回None或Request或Item对象的可迭代对象。
        pass

    def process_start_requests(self, start_requests, spider):
        # 与Spider的起始请求一起调用，与process_spider_output()方法类似，
        # 但不需要关联响应。

        # 应只返回请求（不是Item）。
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TempDownloaderMiddleware:
    # 并非所有方法都需要定义。如果未定义方法，
    # Scrapy将表现为Downloader中间件不修改传递的对象。

    @classmethod
    def from_crawler(cls, crawler):
        # Scrapy用于创建Spider的方法。
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # 每个通过下载器中间件的请求都会调用此方法。

        # 必须：
        # - 返回None：继续处理此请求
        # - 或返回Response对象
        # - 或返回Request对象
        # - 或引发IgnoreRequest：将调用已安装的下载器中间件的process_exception()方法
        return None

    def process_response(self, request, response, spider):
        # 与下载器返回的响应一起调用。

        # 必须：
        # - 返回Response对象
        # - 返回Request对象
        # - 或引发IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # 当下载处理程序或process_request()
        # （来自其他下载器中间件）引发异常时调用。

        # 必须：
        # - 返回None：继续处理此异常
        # - 返回Response对象：停止process_exception()链
        # - 返回Request对象：停止process_exception()链
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
