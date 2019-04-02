#!/usr/bin/env python3
#-*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import pandas


r = requests.get('http://book.douban.com/subject/1084336/comments').text

soup = BeautifulSoup(r,'lxml')
pattern = soup.find_all('p','comment-content')

comments = []

for item in pattern:
    comments.append(item)



df = pandas.DataFrame(comments)
df.to_csv('xiaowangzi.csv',encoding = "utf-8-sig")
print(df)


