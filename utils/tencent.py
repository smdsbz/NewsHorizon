#!/usr/bin/env python3

'''
  the Tencent Crawler
'''
import requests,re,sqlite3
from datetime import datetime


__author__ = 'yjweng01'

# 腾讯的科技类新闻
URL = 'http://tech.qq.com/'

try:
    from globalvar import *
except ImportError:
    NEWS_DB = '../database/data.db'





def get():
    r = requests.get(URL).text
    news = re.findall(
        '<a target="_blank" href="(.*?)">(.*?)<em>'
        ,r)
    oTime = datetime.now()
    sTime = oTime.strftime('%d %B, %Y').lstrip('0')
    treated = []
    for each in news:
        treated.append((each[1],each[0],sTime,'tencent'))


    _write_to_db(treated)
    return treated





#  欸好像匹配出来的不是头条是旁边一个奇怪的排行榜= =不过看上去也差不多那就这样了吧
def _write_to_db(data):
    db = sqlite3.connect(NEWS_DB)
    cur = db.cursor()
    for each in data:
        whether_exist = cur.execute('SELECT * FROM NEWS WHERE url = "{}"'.format(each[1])).fetchall()
        if not whether_exist:
            SQL = (
                'INSERT INTO NEWS '
                '(title, url, date, src) '
                'values ("{}", "{}", "{}", "{}")'.format(
                    each[0], each[1], each[2], each[3]
                )
            )
            # print(SQL, end='\n\n\n')
            cur = db.execute(SQL)


    db.commit()
    cur.close()
    db.close()



if __name__ == '__main__':

    news = get()

    for each in news:
        print(each[0], '@')
        print(each[1], end='\n\n')
