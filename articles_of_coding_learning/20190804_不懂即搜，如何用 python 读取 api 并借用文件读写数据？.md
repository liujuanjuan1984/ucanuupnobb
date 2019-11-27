# 不懂即搜，如何用 python 读取 api 并借用文件读写数据？

人类天生有一种本领，即便不懂那原理，居然也能拿来就用。李笑来在提出这个观点时，举了很多生动的例子。我呢，恰好最近搜索了好几个第三方库并拿来就用。如果你和我一样，正在自学 python，想试试新玩意，不妨顺着我的笔记来尝鲜。即便你暂时没有自学编程的习惯，那么也祝愿你能从下述过程中和我一样发现：不懂即搜，原来可以帮助我们解决好多“难题”。

起因是这样的，上周尾，我向同事要一些未经统计的原始数据，想要周末自行尝试写脚本做统计分析。工程师同事开放了一个 api 给我。以前我只知 api 这个词汇，但并没有见过 api 长什么样子。第一次拿到 api 一看，哟，居然只是一个 url 链接。用浏览器打开，是一个网页，而我想要的内容数据，都呈现在那网页上。

于是我去搜索`“python 如何读取网页内容 site:csdn.net”`，后面这一小串字符，表示我仅想查阅 csdn.net 网站上的内容。当然你也可以改成别的网站。下文提到搜索时，我将不再重复后面这一小串。但这一小串作为一个实用的搜索技巧，能很好地提高你的搜索成效。

搜索到结果后，我依葫芦画瓢，在 vscode 中写了以下几行代码。

```python

def read_url_to_str(url):
    import urllib.request as request
    webpage = request.urlopen(url)
    data = webpage.read() #<class 'bytes'>
    content_str = data.decode("utf-8") #<class 'str'>
    return content_str

```

但 urllib 被编辑器自动画了红色的波浪线，这是在提醒我，我并没有安装它。它是什么？打个类比吧，我们去买奶茶，默认的奶茶仅有水、茶末、奶的混合体就相当于 python 本尊，但你可以选择加的各种料，芒果粒、椰果、红豆等等，你把它们想成是 python 的各种第三方模块啊库啊包啊之类，更讲究的人会自制果粒放到自己的奶茶让它更好喝，那就是你自定义的模块啊库啊包啊之类。

用什么方式能简便地安装 python 的第三方库呢？我用的是 anaconda，你可以搜`“anaconda windows 10 如何安装”`，windows 10 是我的操作系统，你也可以换成自己的操作系统。装好后，搜 `“anaconda 如何安装 urllib” `即可。其实简单的就只有一句话，即，打开 anaconda powershell prompt ，输入命令行并回车就行。如果问你 Y/N ，输入 Y 并回车即可。

> pip install urllib

以上操作完全无需记忆，只需要懂的如何搜索到答案即可。每次需要用到时，直接去互联网搜。本文我会反复提到“搜索”，它简直是自学编程的最佳伴侣。

在《自学是门手艺》的`Jupyterlab 的安装与配置` 这一节，具体讲到了 anaconda 的安装与更新，以及如何检查已安装的版本。如果你有需要，也可以直接照着做吖：

![image](https://user-images.githubusercontent.com/31027645/62422517-831d9c80-b6e6-11e9-9a85-ba506dd8ec86.png)

<center> xue.cn 内容截图 </center>

经检查，我的 urllib 已安装成功， 那么上面一段程序已可运行。于是调用试试看吧。

```python

# 上述 api 不便公开，我另找 url 也可演示该功能
url_a = 'https://static.press.one/e5/2d/e52d0c03fc7b8587ec73412519a76f13177ada09f8b8a9810724e3f018ee50ff.md'

content_str = read_url_to_str(url_a)
print(content_str)

```

嗯，但是这样直接在终端打印，会产生刷屏的效果吖。那干脆定义一个简单的函数，用来把页面内容保存在 txt 文件中吧。相信你也能简单理解下面这几行代码：

```python

def write_str_to_txt_file(content_str):
    import os.path
    import random
    x = random.randint(10000,99999)
    txt_file_url = 'd:/file'+str(x)+'.txt' #增加随机数功能，方便多次调用时生成的文件不同。
    with open(txt_file_url,'at',encoding='utf-8') as tf:
        tf.write(content_str)
    print('内容已写入文件',txt_file_url)
```

我的工程师同事给我的 api 其数据的格式是 json 的，后来我又检索了`“python 如何读取 json 数据”` ，这样一来，代码读了网页之后返回的，不再是 string 类型，而是 json 与 python 都兼容的 字典类型。

其后我又遇到了数据写入 txt 文件，再读取使用时，变成了“列表”的问题。如果你用过 python 的 `fileobject.readlines()` 就会明白我在讲什么。好在我去搜了 `“python 如何处理 json 数据 文件读写”`并顺利掌握。

```python

def read_url_to_dict(url):
    import urllib.request as request
    webpage = request.urlopen(url)
    data = webpage.read() #<class 'bytes'>
    content_str = data.decode("utf-8") #<class 'str'>
    #如果你的编辑器提醒你没有安装 json，你搜索一下安装即可
    import json
    content_dict = json.loads(content_str)
    return content_dict

def dict_write_json_file(content_dict,file_url="d:/json_file.json"):
    import json
    import os.path
    with open(file_url,'w',encoding='utf-8') as write_f:
        json.dump(content_dict,write_f,ensure_ascii=False,sort_keys=True, indent=4)
    print('数据 dict 已写入文件：',file_url)

def read_json_file_to_dict(file_url="d:/json_file.json"):
    import json
    import os.path
    with open(file_url,'r',encoding='utf-8') as read_f:
        content_dict = read_f.load(read_f)
    return content_dict

```

但这并不算完。我又试着用最初的`read_url_to_str(url)` 去读了更多网页并调用`write_str_to_txt_file(content_str)`然后发现，很多网页读出来的，并非网页上肉眼可见的中文内容，而是各种代码。

我试了以下几种网页。如果你好奇，拷贝我的代码到你本地的编辑器，运行试试看吧。

``` python
#读出来一个汉字也没有，全是代码
url_a = 'https://press.one/'

#能完整读完整个网页的内容，整个网页的内容就是一个 markdown 文件内容
url_b = 'https://static.press.one/e5/2d/e52d0c03fc7b8587ec73412519a76f13177ada09f8b8a9810724e3f018ee50ff.md'

#仅能读到部分标题文本，其余也都是代码
url_c = 'https://www.zhihu.com/question/338250156'

#阮一峰老师的个人博客 RSS 订阅网址，能读不少内容
url_d = 'https://feeds.feedburner.com/ruanyifeng'

#github 的一个旧版本的 api
url_e = 'https://api.github.com/graphql'

```

少量网页能读出来中文内容，而绝大多数网页读出来的仅仅只有掺杂了 JavaScript 或其它语言的 html 代码。到底为什么呢，我现在并不理解，倒也不妨碍我**善用搜索技能**从而掌握了部分用法。未来我还想要纯靠自学掌握 python 爬虫技巧。你觉得我能办到吗？

其实吖，搜索本身并不困难。困难的是，对于自学编程的人来说，常常不懂用专业词汇描述自己的问题。如果你曾遇到这类困难，不妨加入我的 python 自学小群，和大家切磋“搜索”时如何描述问题吧~ 我的微信号：qiaoanlu，暗号：编程自学

