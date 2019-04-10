# -*- coding: utf-8 -*-
import scrapy
from doubantop.items import DoubantopItem

class Doubantop250Spider(scrapy.Spider):
    name = 'doubantop250'
    allowed_domains = ['movie.douban.com/top250']
    start_urls = ['http://movie.douban.com/top250/']

#    def start_requests(self):
#        for url in self.start_urls:
#            yield scrapy.Request(url = url ,callback=self.parse)

    def parse(self,response):
        item = DoubantopItem()
        res = response.xpath('//div[@class="item"]')
        for data in res:
            item['name'] = data.xpath('div/div/a/span/text()').extract()
            item['score'] = data.xpath('div[2]/div[2]/div/span[2]/text()').extract()
            item['introduction'] = data.xpath('div/div/p/span/text()').extract()
            yield item
        

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()[0]
        if next_url:
            next_url=response.urljoin(str(next_url))
            yield scrapy.Request(next_url,callback = self.parse,dont_filter=True)

