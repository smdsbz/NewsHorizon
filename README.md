# NewsHorizon
A simple website that presents you with latest feats of tech, using source from other news agencies.
## Front-end
### 前端样式
参考[这里](http://news.qq.com/)
当然我们估计用不了那么多。。。。
短时间写不出CSS的话，就用[MaterializeCSS](http://materializecss.com/)吧，这样我也可以帮忙
## Back-end
### 后台函数格式要求
```
def get():
    '''
      统一函数名称，而使用不同的文件名，方便我在主程序中调用！！

      format requirement:
      data = {'NEWS BIGGIE': ['https://..../', '8 March, 2017', 'netease', etc.], 'SECOND FEAT': [...], ...}

      返回格式要求：
      data =
      {'新闻标题': [
           '链接网址（不指望能够把新闻内容也抓下来，有时间可以试试）'
           '时间（格式参照上面，用datetime）',
           '来源（统一小写英文）',
           看看这后面还要什么，毕竟是要进数据库还能被搜出来的东西。。。
       ]，。。。。。
      }

      p.s. 这是标准的函数文档写法，这样写可以直接用 help(函数名) 查看到这段文字
    '''
    # your functioin body here
    pass
```

## But how to ...??
大家可以参考廖雪峰和菜鸟教程，也可以问我（当然上课时间我不能很快就回复就是了）
