import urllib2

#目标：写个爬虫玩，把掘金沸点最近1年的热门推荐都收录到文档中。

'''
# 方法：关键词搜“python3 爬虫”，找别人的代码试用。

https://www.cnblogs.com/linshuhe/p/5733333.html
疑问：我没有 urllib2 库

Python3 安装bulitwith 和urllib2包
https://blog.csdn.net/qq_27657429/article/details/52653164

我不太能理解vscode，python3语言，与urllib2的库的关系。

'''

def getHtml(url):
    response = urllib2.urlopen(url)
    html = response.read()
    return html

print(getHtml("http://www.baidu.com"))
