# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import re


class CsdnblogPipeline(object):
    def process_item(self, item, spider):
#        data = re.findall("http://blog.csdn.net/(.*?)/article/details/(\d*)",item['url'])

#        filename = str(data[0])+'_'+str(data[1]) + '.txt'
        filename = 'hello.txt'
        text = "title:"+item['title'] +"\nlink:" + item['url'] + "\nrelease_time:" + str(item['releaseTime']) +"\nreadnumber:"+ str(item['readnum']) +"\n\narticle:" + str(item['article'])

        fp = open(filename, 'w')
        fp.write(text)
        fp.close()

        return item
