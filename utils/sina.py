#!/usr/bin/env python3

import requests, re, sqlite3
from datetime import datetime

__author__ = 'guess'

URL='http://tech.sina.com.cn/'

if __name__!='__main__':
    import globalvar
else:
    NEWS_DB = '../database/data.db'
    
def get():
    rep=requests.get(URL)

    if rep.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(rep.text)
        if encodings:
            rep.encoding = encodings[0]
        else:
            rep.encoding = rep.apparent_encoding

    raw = re.findall('<h2 class=".*?"><a target="_blank" href="(.*?)">(.*?)</a>',rep.text)
    
    pre_raw1=re.findall('<div class="newsRankCon"><ul id="newsRankTabC1">(.*?)</ul>',rep.text)

    if pre_raw1:
        raw1=re.findall('<a href="(.*?)" target="_blank">(.*?)</a>',pre_raw1[0][0])
        raw.extend(raw1)

    '''
        print(rep.headers['content-type'])
        print(rep.encoding)
        print(rep.apparent_encoding)
    '''

    _write_to_db(raw)

    return raw
    
def _write_to_db(data):
    '''
      internal function:
        write to database
    '''
    oTime = datetime.now()
    sTime = oTime.strftime('%d %B, %Y').lstrip('0')
    
    with sqlite3.connect(NEWS_DB) as db:
        for each in data:
            SQL = 'SELECT * FROM NEWS WHERE url = "{}"'.format(each[0])
            cur = db.execute(SQL).fetchall()

            if not cur:
                SQL = 'INSERT INTO NEWS (title, url, date, src) values ("{}", "{}", "{}", "{}")'.format(each[1], each[0], sTime, 'sina')
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
        print(each[1], '@')
        print(each[0], end='\n\n')
