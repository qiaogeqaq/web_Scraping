# -*- coding: utf-8 -*-
import scrapy
from w3school.items import W3SchoolItem

class W3schoolXmlSpider(scrapy.Spider):
    name = 'w3school_xml'
    allowed_domains = ['www.w3school.com.cn']
    start_urls = ['http://www.w3school.com.cn/xml/index.asp']

    def parse(self, response):
        item = W3SchoolItem()
        sel = response.xpath('//div[@id="course"]/ul/li')
        for se in sel:
            item['title'] = se.xpath('a/text()').extract()[0]
            item['link'] = se.xpath('a/@href').extract()[0]
            item['desc'] = se.xpath('a/@title').extract()[0]
            yield item
