#!/usr/bin/env python3

'''
  the Reddit Crawler
'''

__author__ = 'smdsbz'




# 数码电子科技类新闻
URL = 'https://www.reddit.com/r/tech/'


import requests, re
from datetime import datetime




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
    treated = dict()
    for each in raw:
        # 打算把所有的新闻都搜集到数据库的一个table里面，方便搜索
        treated[each[1]] = [each[0], sTime, 'reddit']


    return treated





########  debug & test-run  ########

if __name__ == '__main__':

    result = get()

    for each in result:
        print(each, '@')
        print(result[each][0], end='\n\n')

    try:
        first = result[list(result.keys())[0]]
    except IndexError:
        print('You\'ve got NOTHING!!!')
    else:
        print(
            '\n==============================================================================\n'
            'called on:', first[1],
            '\t\t',
            'source site:', first[2],
            end='\n==============================================================================\n\n'
        )
        del first
