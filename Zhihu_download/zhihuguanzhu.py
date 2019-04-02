import requests 
import pandas as pd
import time


headers = {"user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}

user_data = []


def get_user_data(page):
    for i in range(page):
        url = "https://www.zhihu.com/api/v4/members/ChaselLand/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20".format(i*20)

        response = requests.get(url,headers=headers).json()['data']
        user_data.extend(response)
        print("download page %s" % str(i+1))
        time.sleep(2)


if __name__=='__main__':
    get_user_data(8)
    df = pd.DataFrame.from_dict(user_data)
    df.to_csv("followees.csv",encoding="utf-8-sig")

