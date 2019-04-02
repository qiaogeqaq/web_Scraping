# -*- coding: utf-8 -*-
import scrapy
from budejie_txt.items import BudejieTxtItem

class BudejieSpider(scrapy.Spider):
    name = 'budejie'
    allowed_domains = ['www.budejie.com']
    start_urls = ['http://www.budejie.com/text/']
    total_page = 1

    def parse(self, response):
        item = BudejieTxtItem()

        current_page = int(response.css('a.z-crt::text').extract_first())
        lies = response.css('div.j-r-list >ul >li')
        for li in lies:
            item['username'] = li.css('a.u-user-name::text').extract()
            item['content'] = li.css('div.j-r-list-c-desc a::text').extract()
            yield item

        if current_page < self.total_page:
            yield scrapy.Request(self.start_urls[0]+str(current_page+1))
