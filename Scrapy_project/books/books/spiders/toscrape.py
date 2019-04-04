# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Request
from books.items import BooksItem

class ToscrapeSpider(scrapy.Spider):
    name = 'toscrape'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        item = BooksItem()

        lies = response.css('ol.row >li')
        for li in lies:
            item['title'] = li.xpath('article/div/a/img/@alt').extract()
            item['price'] = li.css('div.product_price p::text').extract()[0]
            item['star'] = li.xpath('article/p/@class').extract()
            yield item
     
        next_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url,callback = self.parse)

