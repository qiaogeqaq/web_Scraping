# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Request
from csdnblog.items import CsdnblogItem



class SpiderCsdnblogSpider(scrapy.Spider):
    name = 'spider_csdnblog'
    allowed_domains = ['csdn.net']
    start_urls = ['https://blog.csdn.net/oscer2016/article/details/78007472']

    def parse(self, response):
        item = CsdnblogItem()

        item['url'] = response.url
        item['title'] = response.xpath('//h1[@class="title-article"]/text()').extract()[0]
        item['releaseTime'] = response.xpath('//span[@class="time"]/text()').extract()[0]
        item['readnum'] = response.xpath('//span[@class="read-count"]/text()').extract()
        data = response.xpath('//div[@id="content_views"]')
        item['article'] = data.xpath('string(.)').extract()[0]

        yield item
