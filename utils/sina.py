#!/usr/bin/env python3

import requests, re, sqlite3
from datetime import datetime

try:
    from globalvar import *
except ImportError:
    NEWS_DB = '../database/data.db'




__author__ = 'guess'

URL='http://tech.sina.com.cn/'

try:
    from globalvar import *
except ImportError:
    NEWS_DB = '../database/data.db'

def get():
    rep=requests.get(URL)

    if rep.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(rep.text)
        if encodings:
            rep.encoding = encodings[0]
        else:
            rep.encoding = rep.apparent_encoding

    raw = re.findall('<h2 class=".*?"><a target="_blank" href="(.*?)".*?>(.*?)</a>',rep.text)

    pre_raw1=re.findall('<div class="newsRankCon"><ul id="newsRankTabC1">(.*?)</ul>',rep.text)
    #always empty
    if pre_raw1:
        raw1=re.findall('<a href="(.*?)" target="_blank">(.*?)</a>',pre_raw1[0][0])
        raw.extend(raw1)

    '''
        print(rep.headers['content-type'])
        print(rep.encoding)
        print(rep.apparent_encoding)
    '''

    oTime = datetime.now()
    sTime = oTime.strftime('%d %B, %Y').lstrip('0')

    treated = []
    for each in raw:
        treated.append((each[1], each[0], sTime, 'sina'))

    _write_to_db(treated)


    return treated





def _write_to_db(data):
    '''
      internal function:
        write to database
    '''

    with sqlite3.connect(NEWS_DB) as db:
        for each in data:
            SQL = 'SELECT * FROM NEWS WHERE url = "{}"'.format(each[1])
            cur = db.execute(SQL).fetchall()

            if not cur:
                # TODO: IndexError: tuple index out of range
                SQL = (
                    'INSERT INTO NEWS '
                    '(title, url, date, src) '
                    'values ("{}", "{}", "{}", "{}")'.format(
                        each[0], each[1], each[2], each[3]
                    )
                )

                '''
                here's something I get:
                  INSERT INTO NEWS (title, url, date, src) values ("亚马逊CEO贝索斯驾驶世界首款载人机器人", "http://tech.sina.com.cn/it/2017-03-21/doc-ifycnpit2475039.shtml" class="videoNewsLeft", "21 March, 2017", "sina")
                '''

                # print(SQL, end='\n\n\n')
                cur = db.execute(SQL)

        db.commit()

if __name__ == '__main__':
    '''
        import io
        import sys
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
        一次不必要的尝试
    '''
    result = get()

    for each in result:
        print(each[0], '@')
        print(each[1], end='\n\n')
