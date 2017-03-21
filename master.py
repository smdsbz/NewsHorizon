#!/usr/bin/env python3



from multiprocessing import Process, Pipe
# import threading
import time

from main import app, NewsBuffer
# from utils import NewsBuffer








def buffer_refresh():
    while True:
        NewsBuffer.refresh()
        time.sleep(10)






if __name__ == '__main__':

    # pipe = Pipe()

    view = Process(target=app.run(debug=True), args=())
    buff = Process(target=buffer_refresh, args=())

    buff.start()
    view.start()

    buff.join()
    view.join()
