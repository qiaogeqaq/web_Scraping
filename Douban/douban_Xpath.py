#!/usr/bin/env python3

import requests
from lxml import etree
page = 1
file = []

while page < 10:
    url = 'http://book.douban.com/subject/1084336/comments/hot?p=' + str(page)
    r=requests.get(url).text

    s = etree.HTML(r)

    #print(s.xpath('//*[@id="comments"]/ul/li[2]/div[2]/p/span/text()'))

    #print(s.xpath('//div[@class="comment"]/p/span/text()'))

    #print(s.xpath('//span[@class="short"]/text()'))

    file += s.xpath('//span[@class="short"]/text()')
    page +=1


#using i/o
with open('xiaowangzi.txt','w',encoding = 'utf-8') as f:
    for i in file:
        print(i)
        f.write(i)



#using pandas
import pandas as pd
df = pd.DataFrame(file)
df.to_csv('xiaowangzi.csv')
