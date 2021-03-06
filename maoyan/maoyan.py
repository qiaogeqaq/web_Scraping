#!/usr/bin/env python3
#get top 100 movies
import requests
import re
import os
from requests.exceptions import RequestException
import json

headers = {

    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
}

def get_one_page(url,headers):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestsException:
        return None



def parse_one_page(html):
    pattern = re.compile(r'<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?@160w_220h_1e_1c)".*?name"><a'
         +'.*?">(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)

    items = re.findall(pattern,html)

    for item in items:
        yield{
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }

def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii = False)+'\n')
        f.close()


def save_image_file(url,path):
    jd = requests.get(url)
    if jd.status_code==200:
        with open(path,'wb') as f:
            f.write(jd.content)
            f.close()


def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url,headers)
    if not os.path.exists('covers'):
        os.mkdir('covers')
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)
        save_image_file(item['image'],'covers/'+item['title']+'.jpg')



if __name__=='__main__':
    for i in range(10):
        main(i*10)


