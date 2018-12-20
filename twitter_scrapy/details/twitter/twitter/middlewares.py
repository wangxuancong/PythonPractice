# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

class TwitterSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):

        return None

    def process_spider_output(self, response, result, spider):

        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):

        pass

    def process_start_requests(self, start_requests, spider):

        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TwitterDownloaderMiddleware(object):
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):

        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):

        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

from scrapy.http import HtmlResponse
class JSPageMiddleware(object):

    # requset url page by JS
    def prosess_request(self,request,spider):
        spider.browser.get(request.url)
        import time
        time.sleep(3)
        print('visit:{0}',format(request.url))
        return HtmlResponse(url= spider.browser.current_url,body=spider.browser.page_source,encoding='UTF-8',request= request)
class ProxyMiddelware(object):
    def prosess_request(self,request,spider):
        request.meta['proxy'] = 'http://127.0.0.1:45282'