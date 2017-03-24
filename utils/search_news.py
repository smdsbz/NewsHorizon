#!/usr/bin/env python3




from globalvar import *

import sqlite3



def search_news(direction):

    data = tuple()

    with sqlite3.connect(NEWS_DB) as db:
        SQL = (
            'SELECT title, url, date, src '
            'FROM NEWS '
            'WHERE title LIKE "%{}%"'.format(direction)
        )
        print(SQL)
        cur = db.execute(SQL)
        data = cur.fetchall()

        # db.close()

    return data
