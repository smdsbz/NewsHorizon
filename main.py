#!/usr/bin/env python3

'''
  News Horizon 新闻整合网 - 专注科技板块30年（雾
'''

from flask import Flask
from flask import redirect, url_for, render_template

# 引入全局变量
from globalvar import *

# 注册 reddit.get() 功能
# from utils import reddit, sina

# from multiprocessing import Process, Queue
# import time


import threading, time


from utils import NewsContainer, _INTERVAL


######## initialization ########

app = Flask(__name__)

NewsBuffer = NewsContainer()



######## NewsBuffer ########

# TODO: threading

class BufferThread(threading.Thread):

    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name


    def run(self):

        # if self.name == 'view':
        #     app.run(host='127.0.0.1', debug=True)

        if self.name == 'buffer':
            global NewsBuffer
            while True:
                NewsBuffer.refresh()
                print("NewsBuffer refreshed")
                time.sleep(10)






######## views ########

@app.route('/')
def index():
    '''
      函数返回值直接进入前端，不需要再次加工
      前端直接用jinja2方法读取:

        <div class="content-wrapper" id="reddit-news">
        {% for each in reddit_news %}
          <div class="news-content">
            <!--
              直接用 {{ each[x] }} 获取每条新闻的相应信息：
                {{ each[0] }} 被新闻标题替代
                {{ each[1] }} 被新闻链接替代
            -->
          </div>
        {% endfor %}
        </div>

      就像这样
    '''

    # 话说我的前端啥时候好啊 /托腮
    return render_template(
        'demo.html',
        data = NewsBuffer
        )




######## starter ########

if __name__ == '__main__':

    thread_buff = BufferThread(2, 'buffer')

    thread_buff.start()
    time.sleep(5)
    app.run(host='127.0.0.1', debug=True)

    thread_buff.join()

    print("Sevice stopped") # this should not show

    # you may exit by ^C multiple times
