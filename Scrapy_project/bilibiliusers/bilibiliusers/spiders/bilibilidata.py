# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Request
from bilibiliusers.items import BilibiliusersItem

class BilibilidataSpider(scrapy.Spider):
    name = 'bilibilidata'
    allowed_domains = ['www.bilibili.com']
#    start_urls = ['https://api.bilibili.com/x/space/acc/info?mid=1&jsonp=jsonp']
    
    
    def start_requests(self):
        start_urls = []
        follow_urls = []
        vmid = 0
        for mid in range(1,2000000):
            start_urls.extend(['https://api.bilibili.com/x/space/acc/info?mid='+str(mid) +'&jsonp=jsonp'])
#            follow_urls.extend(['https://api.bilibili.com/x/relation/stat?vmid='+str(mid)+'&jsonp=jsonp'])

        for url in start_urls:
            vmid +=1
            yield scrapy.Request(url,meta={'mid':vmid},callback=self.parse,dont_filter=True)



    
    def parse(self, response):
        vmid = response.meta['mid']
        
        follow_urls = 'https://api.bilibili.com/x/relation/stat?vmid='+str(vmid)+'&jsonp=jsonp'

        item = BilibiliusersItem()
        js = json.loads(response.body.decode())
        jsdata = js['data']
        item['name'] = jsdata['name']
        item['sex'] = jsdata['sex']
        item['level'] = jsdata['level']
        item['birthday'] = jsdata['birthday']       
        yield Request(follow_urls,meta={'item':item},callback=self.parse_r,dont_filter=True)
#request  url的域名不能和文件中自己配置的allowed_domains不一致，否则会被过滤掉。
#停用过滤功能

    def parse_r(self,response):
        item = response.meta['item']
        js = json.loads(response.body.decode())
        jsdata = js['data']
        item['follower'] = jsdata['follower']
        item['following'] = jsdata['following']
        yield item
'''        
        for mid in range(1,10):
            url = 'https://api.bilibili.com/x/space/acc/info?mid='+str(mid) +'&jsonp=jsonp'
            yield scrapy.Request(url,callback=self.parse,dont_filter=True)
    
'''
    


