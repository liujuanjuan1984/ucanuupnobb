![banner](https://press.one/thumbnail?width=792.0000171661377&url=https://static.press.one/05/b8/05b8cd6f7762d4f0668557a80d0c30f241b4617f5be6dd0decf3b74ed5341dc3.jpg)

## 回顾一下昨天的学习笔记

在[适合新手的 python pandas 学习笔记(1)](https://mp.weixin.qq.com/s/87FsOZE2AVAP5fD7dbOdXw)中，准备工作已经完成。同时我也通过探索找到了适合自己的学习入口：先了解 pandas 所特有的数据结构`series`与`dateframe`。

昨天，我并没有按照官方的[`10 minutes to pandas`](https://pandas.pydata.org/pandas-docs/version/0.22.0/10min.html)完整地练习一遍，但我已经知道这两种数据容器**有**增删改查、IO 处理等各种方法，只是还没用过。我决定，结合一个实际的需求试着把 pandas 先用起来。我预料到这个过程中将会遇到很多新知识，但我心中有数一点不慌，无非是根据实际所需在手头材料中检索而已，现学现用吧。

这种不会就敢用的学习方法，其实非常“大胆”，并不适合绝大多数人。为什么呢？因为有些人善于把遇到的困难经自己的大脑认知加工成挫败体验，而我似乎很善于解决问题和主动调控成长体验，于是我在拆解和反复地找到答案的过程中，收获的是持续的成就感。

回顾和整理昨天顺手做的学习笔记，使之可读性加强到可公开发布，是我做心理建设的一种方法。完成这一步后，我就开始聚焦今天的学习。

## 用什么姿势解决什么需求？

实际需求如下：

> 通过 api url 读取 json 数据，对数据进行统计分析后，输出结果到 excel。

上上个周末，我已经完成了该需求，下文所指代的原有实现方法即是指该脚本。代码有 300 行，有一半是用 `xlwt` 把处理结果写入 excel 文件。另外 150 行代码，处理的是数据的提取、数据指标的定义与演算。未来我还将统计更多具体的数据指标，可以预想到逻辑会更加复杂，代码只会更加臃肿。

昨晚临睡前，我用手机浏览了一点《利用 python 做数据分析》中的代码，简洁而优雅，我非常期待用 `pandas` 重新满足我的需求。

今天的心理建设已经完成，动力很足。然后我写下了需求，然后按惯例把需求拆解，思考每个步骤如何用 `pandas` 实现，……但我突然意识到这种做法是错误的。——这是一个重要的思维岔道口，这个思维过程是一闪即过的，所幸我还是抓到了。

电光闪石之间，我意识到，我原来的做法是在用零散的方法处理零散的数据，但 pandas 的关键就是结构化的数据。 `api url` 提供的 `json` 数据就是结构化的！想法涌现，有些甚至来不及显现为语言，我只是模糊地意识到，自己的原有实现是低纬度、低效率的，我不能再把结构化的数据打散，我应该用 pandas 特有的做法。

我再次看了看` api url` 所展现的 `json` 数据结构。

## 源数据的结构

从 api url 获取到的 json 数据结构是这样的：

```json

{
    "comments" : [{},{},…,{}],
    "total" : 123,
}

```

然后 `comments`的值，是个由字典构成的列表。每个字典就是一条`comment`，它再次嵌套了一个`user`字典（为了节省篇幅，我已经简化了很多字段），是这样的：

```json

{
    "created_at": "2019-07-31 22:15:29.658500+08:00",
    "up_vote_count": 0,
    "id": 447,
    "user":{
        "admin" : false,
        "username" : "liujuanjuan1984",
    },
}

```

无论是字典，还是列表，在`pandas`处理为`series` 或者`datafrome`，都是容易的。

## 今日的学习成果

为了完成这个需求，我读`pandas`官网文档，不仅仅是 10 分钟上手部分，更多看的是 IO tools 那部分。`pandas`的方法如此简约、直白。相关的方法，拿来即用。只不过必须要知道自己想要什么。比如，“如何从 url 获取数据？”或者“如何从嵌套的字典中，取出内层的字典，然后把数据和外层字典数据合并？”在获取此类疑问的答案时，我也走了些弯路，但一旦知道答案后，就再次惊喜于`dataframe`作为数据容器，如此好用。

没有花太多时间，我就用`pandas`完成了从 api url 获取数据，并与文件读写交互这个需求。

调试完代码后，我哭笑不得，和我原来的实现方法相比，简直一个在天，一个在地。揣摩了许久，我越来越惊喜，自己昨晚怎么就一下子抓到了重点：**用 pandas 的核心，应该是把数据整理为结构化的数据后再用它的方法处理**。

代码仅有区区 10 行。

```python

import pandas as pd
import os.path

url = 'https://url.path'# api url 不能公开，现在放的这个是假数据
rlt_file = 'd:/pandas_rlt.xls'

df1 = pd.read_json(url) #读出来的数据，就是 dataframe
df2 = pd.DataFrame([x for x in df1['comments']])#把 comments 抽出来
df3 = pd.DataFrame([x for x in df2['user']])#把 comments 内嵌的 user 抽出来
df = pd.concat([df2,df3], axis=1)#把 user 数据和 comments 数据合并
df.to_excel(rlt_file, encoding='utf-8') #数据写 excel 文件
xdf = pd.read_excel(rlt_file, encoding='utf-8') #从 excel 文件读数据

```

你或许好奇我原来怎么写。下面是比较臃肿的原实现方法。在上上周末，我能写出下面的脚本，且是首次根据需要检索到并安装使用 `urllib.request`，`json`,`xlrd`,`xlwt`，也挺不容易的。

## 原有的实现方法

我原有的实现方法是，通过 `urllib.request` 读取 `api url` 网页拿到 `string` 格式的数据，并用`json.loads`方法转换为字典数据。且为了降低后续每次从 `api url` 获取的数据量，已有的数据会保管在本地的，于是需要处理 `dict` 字典数据到文件的读写处理。这一部分代码如下：

```python
# 读取 api url 内容并返回为字典
def read_url_to_dict(url):
    import urllib.request as request
    webpage = request.urlopen(url)
    data = webpage.read() #<class 'bytes'>
    content_str = data.decode("utf-8") #<class 'str'>
    #如果你的编辑器提醒你没有安装 json，你搜索一下安装即可
    import json
    content_dict = json.loads(content_str)
    return content_dict
# 字典内容写入.json 文件
def dict_write_json_file(content_dict,file_url="d:/json_file.json"):
    import json
    import os.path
    with open(file_url,'w',encoding='utf-8') as write_f:
        json.dump(content_dict,write_f,ensure_ascii=False,sort_keys=True, indent=4)
    print('数据 dict 已写入文件：',file_url)
# 读取 .json 文件 生成 dict 字典
def read_json_file_to_dict(file_url="d:/json_file.json"):
    import json
    import os.path
    with open(file_url,'r',encoding='utf-8') as read_f:
        content_dict = read_f.load(read_f)
    return content_dict

```

通过以上处理，我拿到的原始数据即是字典形式。然后我开始了对数据的肢解和拼接……来定义统计数据指标。下面粘贴的代码只是一部分。这部分在掌握了 pandas 的写法后再来看，真是“小小幼儿学走路，歪歪扭扭真可爱”。

```python

how_many_comms = data_dic['total']#总的留言条数，int
all_comms_list = data_dic['comments']#总的留言列表，list

content_list = []
date_list = [] #留言不为 0 的日期，list
time_list = []
urs_list=[]#留言的用户列表,list
up_vote_list=[]
comms_at_questions = 0 #在习题下的留言条数，int
comms_at_posts = 0 #在章节下的留言条数，int

for comm in all_comms_list:
    content = comm['content']#留言的内容,str 
    created_at = comm['created_at']#留言创建日期时间,str
    created_date = created_at[:10]#留言创建日期
    created_time = created_at[11:13]#留言创建时间，仅取小时位
    object_type = comm['object_type']#留言的类型，习题/章节,str
    up_vote_count = comm['up_vote_count']#留言的点赞数,int
    user = comm['user']#留言的用户数据，dic
    urs_name = user['name']#留言的用户名,str

    content_list.append(content)
    date_list.append(created_date)
    time_list.append(created_time)
    urs_list.append(urs_name)
    up_vote_list.append(up_vote_count)

    #用户列表：已留言的用户列表,list
    urs_name_list = list(set(urs_list.copy()))
    #用户数：已留言的用户总数,int
    urs_num = len(urs_name_list)
    #用户的留言条数：每个用户的累计留言条数,list
    comms_by_urs = list_count(urs_list.copy())
    comms_by_urs.sort(key=lambda x:x[1],reverse=True)

```

原实现方法最臃肿的，就是有关 `xlwt` 的处理了…… 

```python

#设置表格样式
def set_style(name,height,bold=False):
    import xlwt
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style

#创建子表
import xlwt
f = xlwt.Workbook()
sheet1 = f.add_sheet('留言总览',cell_overwrite_ok=True)
sheet2 = f.add_sheet('留言用户',cell_overwrite_ok=True)
style = set_style('宋体',220,False)

sheet1.write(0,0,"统计日期",style)
sheet1.write(0,1,date_today,style)
sheet1.write(0,2,time_now,style)

sheet1.write(2,0,"留言的内容分布",style)
sheet1.write(3,0,"ALL",style)
sheet1.write(4,0,"习题",style)
sheet1.write(5,0,"章节",style)
sheet1.write(3,1,how_many_comms,style)
sheet1.write(4,1,comms_at_questions,style)
sheet1.write(5,1,comms_at_posts,style)
sheet1.write(3,2,'%.2f%%'%100,style)
sheet1.write(4,2,'%.2f%%'%(100*comms_at_questions/how_many_comms),style)
sheet1.write(5,2,'%.2f%%'%(100*comms_at_posts/how_many_comms),style)
# 还有一百多行 sheet1.write 语句没贴
f.save(saved_url)

```

特别可笑的是，在设置 sheet.write()的行列参数时，要一条条在 excel 表格中布好，然后小心翼翼逐个修改对应的参数值。

为`pandas`作为数据统计与分析领域的最佳实践而干杯！

## 下一步学习计划

通过第 2 天的以用促学，我对`pandas`代码的简约，`dataframe`数据结构的好用，印象深刻，赞誉不断。我掌握了`pandas`创建`dataframe`的方法，也掌握了`pandas`部分 IO 处理的方法。

接下来我依然围绕自己的这个实际需求，用`pandas`来处理数据的统计与分析。我能预料到的是，这将反复练习增删改查中的“查”，相关的具体方法是什么？我不会，但我不着急，因为准备工作中的学习材料中都有，我想用，立即查就是了。用多几次，我自然就懂了。

我的学习笔记并不罗列到处可以查到的知识点，即便罗列的再好也不如官方文档权威全面。我想记录的，是自己的学习过程与学习思路，一些重要的资源或者坑。这些是对我非常有价值的东西，对大家也或许有一些借鉴意义。
