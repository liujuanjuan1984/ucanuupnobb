# 整理总结 python 中时间日期类数据处理与类型转换（含 pandas）

我自学 `python` 编程并付诸实战，迄今三个月。 `pandas`可能是我最高频使用的库，基于它的易学、实用，我也非常建议朋友们去尝试它。——尤其当你本身不是程序员，但多少跟表格或数据打点交道时，`pandas` 比 `excel` 的 `VBA` 简单优雅多了。

`pandas` 善于处理`表格类数据`，而我日常接触的数据天然带有时间日期属性，比如用户行为日志、爬虫爬取到的内容文本等。于是，使用 `pandas` 也就意味着相当频繁地与时间日期数据打交道。这篇笔记将从我的实战经验出发，整理我常用的时间日期类数据处理、类型转换的方法。

与此相关的三个库如下。

```python

import time
import datetime
import pandas as pd

```

其中，`time` 和`datetime`都是 `python` 自带的，`pandas`则是一个第三方库。换言之，前两者无需额外安装，第三方库则需要通过`pip install pandas`命令行自行安装。如何检查自己是否安装了某个库，如何安装它，又如何查看和更新版本，对新手来说是一个比较大的话题，也是基础技能，值得另外整理一篇笔记，就不在这里占篇幅了。当然，如果你不想自己本地折腾，也可电脑浏览器访问[https://xue.cn](https://xue.cn) 这样的网站，网页上直接写代码并运行它们。

## 一、time模块

对`time`模块，我最常用到的功能就三个：
- 指定程序休眠；
- 获取当前时间戳；
- 时间戳与本地时间的互相转换

### `time.sleep(s)` 指定程序休眠 s 秒

指定程序休眠时间，通常是在长时间运行的循环任务中进行。比如爬虫任务，控制读取网页的时间间隔；自循环任务的时间间隔，调用浏览器打开网页的时间间隔等等。

先用两个打印语句，辅助观察和理解`time.sleep()`的效果：

```python
print(datetime.datetime.now())
time.sleep(5)
print(datetime.datetime.now())
```

至于长时间运行的循环任务，我通常是把核心业务逻辑封装好，利用`jupyter lab`自带的多进程特定，建一个 `notebook` 放入下面这个函数去持续运行。

```python

def repeat_myself(how_many_times = 10):
    print('--------',how_many_times,'----------')
    # 被封装的核心代码
    your_main_def() 

    # 自循环减 1 ；如果剩余次数是0，则终止自循环
    how_many_times += -1
    if how_many_times == 0:
        print(datetime.datetime.now(),'stop it.')
        return

    # 每次调用设定一个时间间隔
    print(datetime.datetime.now(),'have a rest')
    how_long = random.randint(30,120)
    time.sleep(how_long)
    return repeat_myself(how_many_times)

repeat_myself(12)

```

### `time.time()`获取当前时间戳

最初我认为无需急于掌握时间戳这个技能点，但实战中，1) 我的爬虫有时爬取到时间戳类型的数据，为了易读，要把它转换为正常人能看懂的方式；2) 使用 `mysql` 时我关心存储所占用的空间以及读写效率，并获知一个时间数据存成 `char` 不如时间戳更节省空间。好吧，实战需要，那么赶紧掌握起这个小技能吧。

先了解下如何生成时间戳。通过`time.time()`得到的时间戳，是一个有着10位整数位 + 6位小数位的浮点数，可根据需要简单运算转换为需要的 10、13、16 位整数时间戳。

```python
# 获取当前时间戳

# 值是 1569642653.1041737 ,float
a = time.time()
# 1569642653，得到 10位时间戳，int
b = int(a)
# 1569642653104，得到 13位时间戳，int
c = int(a * 1000)
# 1569642653104173，得到 16位时间戳，int
d = int(a * 1000000)

```

接下来，了解一下时间戳和人类易读的时间之间的转换。

### 时间戳与人类易读的时间互相转换

如上面所示，时间戳是一个`float`或`int`类型的数值，至少有 10 位整数。把时间戳转换为人类易读的时间，用到的是`localtime()`，与其相反的是`mktime()`能把人类易读的时间转换为时间戳。

```python

# 时间戳转换为人类易读的时间
# 结果是：time.struct_time(tm_year=2019, tm_mon=9, tm_mday=28, tm_hour=12, tm_min=12, tm_sec=1, tm_wday=5, tm_yday=271, tm_isdst=0)
# 数据类型是 time.struct_time
e = time.localtime(a)
f = time.localtime(b)
g = time.localtime(c//1000)
h = time.localtime(d//1000000)

# 人类易读的时间转换为时间戳
# 结果是：1569643921.0,float
i = time.mktime(e)
j = time.mktime(f)
k = time.mktime(g)
l = time.mktime(h)

```

经`type()`检查，`localtime()` 得到的结果，是 `time.struct_time` 类型，直观可见这个类型对人类依然不是最友好的。最友好的表达将用到 `strftime` 和 `strptime` 这两个方法，处理 `time.struct_time` 与`string`字符串 两个类型的互换。

```python

# 把 struct_time 转换为指定格式的字符串
# '2019-09-28 12:12:01 Saturday'
good = time.strftime("%Y-%m-%d %H:%M:%S %A", e)

# 把字符串转换为 struct_time
# 结果是：time.struct_time(tm_year=2019, tm_mon=9, tm_mday=28, tm_hour=12, tm_min=12, tm_sec=1, tm_wday=5, tm_yday=271, tm_isdst=-1)
nice = time.strptime(good,"%Y-%m-%d %H:%M:%S %A")

```

在我的笔记中，仅整理总结自己常用的方法，至于我自己从未用到或很少用到的方法，并不罗列其中。如有小伙伴希望系统完整地了解，可直接搜：`time site:python.org` 或点击[访问官方文档](https://docs.python.org/zh-cn/3/library/time.html) 能查看完整说明。

## 二、datetime 模块

datetime获取到的时间数据是非常易读的，在和人交互时，比 time 更好用一些。我通常把 `datetime` 用于以下 2 个场景。

### 场景A：log时间戳，打印信息监控代码运行情况

新手写代码，变相就是写bug，以我自己来说，使用不熟模块或写新业务时，写代码和调试修复错误，占用时间常常各半。采用 `jupter lab`的 notebook，让写代码和调试方便许多，但依然需要 `print()` 打印信息方便监控代码运行情况。比如下方这个代码片段：

```python
# 显示效果：2019-09-28 12:44:36.574576 df_rlt ...
print(datetime.datetime.now(),'df_rlt ...')
for one in df_rlt.values:
    print(datetime.datetime.now(),one,'for circle ...')
    try:
        sql_insert = 'INSERT INTO questions(q_id,q_title,q_description,q_keywords,q_people,q_pageview,time) VALUES( "'\
            + str(quesition_id) + '", "' + str(one[0])+ '", "' + str(one[1]) + '", "' + str(one[2]) + '", "' \
            + str(one[3]) + '", "' + str(one[4]) + '", "' + str(datetime.datetime.now()) + '");' 
        sql_update = 'update topic_monitor SET is_title="1" where question_id = "' + str(quesition_id) + '";'
        cursor.execute(sql_insert)
        cursor.execute(sql_update)
        conn.commit()
        print(datetime.datetime.now(),'sql_insert ...')
    except:
        print(datetime.datetime.now(),'sql_insert error...')
        continue

```

### 场景B：文件名时间戳，文件名中增加当前日期

文件名中增加当前日期作为参数，既避免文件相互覆盖（比如数据每天更新，每天导出一次），也方便直观地查看文件版本。当然啦，如果处理的是超级频繁导出的文件，精确到天并不满足需求，可自行精确到时分秒，或直接用`int(time.time())`时间戳作为文件名中的参数。

```python
# 效果：'d:/out_put/xuecn_comments_statistics_2019-09-28.xlsx'
comms_file = output_path + 'xuecn_comments_statistics_' + str(datetime.datetime.now())[:10] + '.xlsx'
```

直接搜：`datetime site:python.org` 或者点击访问 [python 官方文档](https://docs.python.org/zh-cn/3/library/datetime.html)查看超多方法说明。

与官方文档对比，我已经用到的知识点真是九牛一毛。不过也没关系，从需要和兴趣出发就好，没必要硬着头皮把自己打造成移动字典，很多方法呢都是用多了自然记住了，无需反复死记硬背。

## 三、pandas 中的时间处理

我写这篇笔记，本就是奔着精进 `pandas` 来的，前面花了很大篇幅先整理了`time`和`datetime`这些基础功，现在进入重头戏，即 `pandas` 中与时间相关的时间处理。

前面两个部分举例，处理的均是单个值，而在处理 `pandas` 的 `dataframe` 数据类型时，事情会复杂一点，但不会复杂太多。我在实战中遇到的情况，总结起来无非两类：
- 数据类型的互换
- 索引与列的互换

需要留意的是，数据类型应该靠程序判断，而非我们人肉判断。`python pandas` 判断数据类型，常用`type()` 和 `df.info()` 这两个方法。

### 首先，我们构造一个简单的数据示例 df

构造这个实例，只是为了方便后面的展开。构造一个 `dataframe` 的方法有非常多。这里就不展开了。

```python
import random
df = pd.DataFrame({
    'some_data' : [random.randint(100,999) for i in range(1,10)],
    'a_col' : '2019-07-12',
    'b_col' : datetime.datetime.now().date(),
    'c_col' : time.time()},
    index=range(1,10))

```

### 然后，我们逐项查看它的数据类型

刚学着用`pandas`经常会因为想当然地认为某个对象是某个数据类型，从而代码运行报错。后来学乖，特别留心数据类型。

某个数据是什么类型，如何查看，某个方法对数据类型有什么要求，如何转换数据类型，这些都是实战中特别关心的。

```python
# pandas.core.frame.DataFrame
type(df)
# pandas.core.series.Series
type(df['some_data'])
# numpy.ndarray
type(df['some_data'].values)
# numpy.int64
type(df['some_data'].values[0])
# str
type(df['a_col'].values[0])
# datetime.date
type(df['b_col'].values[0])
# numpy.float64
type(df['c_col'].values[0])

df.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9 entries, 1 to 9
Data columns (total 4 columns):
some_data    9 non-null int64
a_col        9 non-null object
b_col        9 non-null object
c_col        9 non-null float64
dtypes: float64(1), int64(1), object(2)
memory usage: 420.0+ bytes
"""

```

### 为什么要转换数据类型，有什么用途

为什么要把时间日期之类的数据转换为 `pandas` 自带的 `datetime64` 类型呢？这当然不是强迫症整洁癖，而且即便不做转换也不会带来任何报错。

最重要的原因是，数据分析将会高频用到基于时间的统计，比如：每天有多少用户注册、登录、付费、留言……产品运营通常按日统计，把`dt.date`改成`dt.week`、`dt.month`、`dt.hour`就能输出周统计、月统计、分时统计……当然官方文档介绍的方法还有更多，我提到的仅是自己高频使用的方法。

```python

df.groupby(df['c_col'].dt.date).some_data.agg('sum')

```

次要的原因是，输出数据到 excel 表格中发给其它同事时，咱们还是得考虑文件的易读、简洁吖。比如，时间戳得转换为人能看懂的文本，比如仅显示日期，无需把后面时分秒之类的冗余数据也显示出来等等。

通过不同方式拿到的数据类型，通常相互之间并不一致，而我们想要使用某些方法提高生产力，必须遵循该方法所要求的数据类型。于是数据类型转换就成了刚需。

### 如何转换为 pandas 自带的 datetime 类型

在上方示例中，肉眼可见 `a_col`、`b_col` 这两列都是日期，但 `a_col` 的值其实是`string 字符串`类型，`b_col`的值是`datatime.date`类型。想要用`pandas` 的按时间属性分组的方法，前提是转换为 `pandas` 自己的 `datetime`类型。

转换方法是一致的：

```python
# 字符串类型转换为 datetime64[ns] 类型
df['a_col'] = pd.to_datetime(df['a_col'])
# datetime.date 类型转换为 datetime64[ns] 类型
df['b_col'] = pd.to_datetime(df['b_col'])
# 时间戳（float） 类型转换为 datetime64[ns] 类型
df['c_col'] = pd.to_datetime(df['c_col'].apply(lambda x:time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(x))))

# 查看转换后的属性
df.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9 entries, 1 to 9
Data columns (total 4 columns):
some_data    9 non-null int64
a_col        9 non-null datetime64[ns]
b_col        9 non-null datetime64[ns]
c_col        9 non-null datetime64[ns]
dtypes: datetime64[ns](3), int64(1)
memory usage: 420.0 bytes
"""

```

其中，难点是 `c_col` 这列。其实不难，只是几个嵌套，显得有点复杂而已：

1. y = `time.localtime(x)`，把 x 从时间戳（10个整数位+6个小数位的那串数字）类型转换为`struct_time`
2. z = `time.strftime('%Y-%m-%d %H:%M:%S',y) ` 把上一步得到的 `struct_time` 转换为 字符串
3. `lambda x:z` 匿名函数，输入一个值x，得到字符串z
4. `df['c_col'].apply()` 对整列每个值做上述匿名函数所定义的运算，完成后整列值都是字符串类型
5. `pd.to_datetime()` 把整列字符串转换为 pandas 的 datetime 类型，再重新赋值给该列（相当于更新该列）

我其实非常希望有个过来人告诉我，这个知识点用的频繁吗，在什么时期是否应该掌握？于是我自己写的笔记，通常都会留意分享自己实战过来的这个判断。当然啦，每个人实战的方向不太一样，大家可作参考，无需完全照搬。具体说来：
- 第 1、2 步是第一部分 `time` 模块总结到基础技能。
- 第 3 步的匿名函数 `lambda` 是相当风骚的知识点，[`xue.cn 《自学是门手艺》`](https://xue.cn)有一节专门讲到它，建议掌握。
- 第 4 步结合匿名函数`lambda`，是对 `dataframe` 整列进行统一操作的重要技能点，多用几次就熟练了。
- 第 5 步 无需死记硬背。为啥我总说 `pandas` 易学好用呢？因为它的很多方法，都能直接见文生义，几乎没有记忆负担。

关于时间日期处理的[pandas 官方文档](https://pandas.pydata.org/pandas-docs/version/0.22.0/10min.html)篇幅也挺长的，没中文版，大家想要系统了解，直接点开查阅吧~

### 关于索引与列的互换

不管何种原因导致，通常使用 `pandas` 时会经常对索引与列进行互换。比如把某列时间数据设为索引，把时间索引设为一列……这些操作并没有额外的特别之处，都统一在`pandas 如何进行索引与列的互换` 这个技能点之下。限于篇幅，我这里就不展开啦。不过索引与列的转换是高频操作，值得另写一篇笔记。

有一点反复强调都不过为，即，我的笔记仅记录自己实战中频繁遇到的知识技能，并非该模块全貌。如需系统掌握或遇到笔记之外的疑问，请善用搜索技能哟：`你的关键词们 site:python.org`。

如果我的整理带给你帮助，请点个赞鼓励我继续分享。如需勘误请留言，或挪步到[我的 github 提issues](https://github.com/liujuanjuan1984/ucanuupnobb/issues)。
