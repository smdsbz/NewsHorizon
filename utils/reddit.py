#!/usr/bin/env python3

'''
  the Reddit Crawler
'''

__author__ = 'smdsbz'




# 数码电子科技类新闻
URL = 'https://www.reddit.com/r/tech/'


import requests, re, sqlite3
from datetime import datetime

if __name__ != '__main__':
    from globalvar import * # will be imported while running main.py
else:
    NEWS_DB = '../database/data.db'  # debugging - using *nix style path expression




########  functions  ########

def get():

    # 网页源代码: all HTML-safe
    source = requests.get(URL).text

    # 食材: [(href, title), (..., ...), ... ]
    raw = re.findall(
        '<p class="title"><a class="title may-blank outbound" '
        'data-event-action="title" href="(.*?)" '
        '.*?>(.*?)</a>',
        source
    )

    # 因为我们只搜集头条，所以时间就用运行该函数的时间也没什么大问题
    oTime = datetime.now()
    sTime = oTime.strftime('%d %B, %Y').lstrip('0')


    # 做饭
    treated = []
    for each in raw:
        # 打算把所有的新闻都搜集到数据库的一个table里面，方便搜索
        treated.append((each[1], each[0], sTime, 'reddit'))

    # 写入数据库
    _write_to_db(treated)

    return treated





def _write_to_db(data):
    '''
      internal function:
        write to database
    '''
    with sqlite3.connect(NEWS_DB) as db:
        for each in data:

            # 判断数据库中是否已有该新闻
            SQL = 'SELECT * FROM NEWS WHERE url = "{}"'.format(each[1])
            cur = db.execute(SQL).fetchall()

            # 如果没有，则写入数据库
            if not cur:
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





########  debug & test-run  ########

if __name__ == '__main__':

    result = get()

    for each in result:
        print(each[0], '@')
        print(each[1], end='\n\n')
