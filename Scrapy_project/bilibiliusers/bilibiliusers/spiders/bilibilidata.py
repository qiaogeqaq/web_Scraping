# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Request
from bilibiliusers.items import BilibiliusersItem

class BilibilidataSpider(scrapy.Spider):
    name = 'bilibilidata'
    allowed_domains = ['www.bilibili.com']
    start_urls = ['https://api.bilibili.com/x/space/acc/info?mid=1&jsonp=jsonp']

    
    def parse(self, response):
        follow_urls = 'https://api.bilibili.com/x/relation/stat?vmid=1&jsonp=jsonp'

        item = BilibiliusersItem()
        js = json.loads(response.body.decode())
        jsdata = js['data']
        item['name'] = jsdata['name']
        item['sex'] = jsdata['sex']
        item['level'] = jsdata['level']
        item['birthday'] = jsdata['birthday']       
        yield Request(url = follow_urls,meta={'item':item},callback=self.parse_r,dont_filter=True)

    def parse_r(self,response):
        item = response.meta['item']
        js = json.loads(response.body.decode())
        jsdata = js['data']
        item['follower'] = jsdata['follower']
        item['following'] = jsdata['following']
        yield item

