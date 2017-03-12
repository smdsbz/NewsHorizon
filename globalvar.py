#!/usr/bin/env python3

'''
  here stores all the global variables
'''



import os

NEWS_FOLDER = os.path.join(os.curdir, 'database')
NEWS_DB = os.path.join(NEWS_FOLDER, 'data.db')



if __name__ == '__main__':
    print(NEWS_FOLDER)
    print(NEWS_DB)
