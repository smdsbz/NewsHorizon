#!/usr/bin/env python3

'''
  the NewsContainer class - used as a buffer for the index page only
'''


import time

import reddit, tencent, sina





__author__ = 'smdsbz'




__buffer_template = dict(
    reddit = [],
    tencent = [],
    sina = []
)




class NewsContainer(object):
    '''
      the buffer class
    '''


    # buffer size
    _size = 5




    def __init__(self, debug=False):
        '''
          with the 'debug' trigger
        '''
        # write in data later
        self._store_room = dict(
            reddit = [],
            tencent = [],
            sina = []
        )




    def __getitem__(self, key):
        return self._store_room[key]





    def get(self, key, default=None):
        '''
        covers KeyError, will return the default value
        (default is None by default)
        '''
        try:
            return self._store_room[key]
        except KeyError:
            return default






    def __setitem__(self, key, value):
        self._store_room[key] = value






    def refresh(self):
        '''
          up to _size for each source
        '''

        tmp_buffer = dict(
            reddit  = reddit.get(),
            tencent = tencent.get(),
            sina    = sina.get()
        )

        for each in tmp_buffer:

            if len(tmp_buffer[each]) < _size:
                # show all if there is not much to show
                self._store_room[each] = tmp_buffer[each]

            else:
                # to avoid a long list of information on the index page
                self._store_room[each] = tmp_buffer[each][:_size]






NewsBuffer = NewsContainer()

while (True):
    NewsBuffer.refresh()
    # refresh every minute
    time.sleep(60)
