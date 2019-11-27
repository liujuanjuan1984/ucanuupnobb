## 一、准备工作

### 解决动力：为什么学？

知道 pandas ，来源于可靠的人强烈推荐。（我们团队中擅长 python 的程序员，甚至我们的 CTO 都推荐。）

后来我搜一下发现，pandas 并非程序员的必需，反而是很多需要做数据分析岗位的利器，比如运营、产品或增长黑客。

通常我们还没有开始学一样新技能时，会被“它太难了吧”，“我可能学不会”这样的念头吓到。但“鸡贼的”pandas 官网居然自己出了一篇面向新手的攻略，名字如此吸引人：

[10 minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html)

### 准备工作：学习材料

好的教程，是开始的第一步。但官网的教程可能让英文不好的人产生困惑。为了适时调控自己的学习体验，我另外准备了两个备查的网址：

[10 分钟搞定 pandas](https://blog.csdn.net/matrix_laboratory/article/details/50704160)

[Python 数据处理：关于 Pandas 你需要知道的都在这里了](https://zhuanlan.zhihu.com/p/28085204)

当然必不可少的，还有一本书：《利用 python 进行数据分析》，我用的是微信读书的电子版。

### 准备工作：安装环境

我用的是 windows10 64 位操作系统，之前已经安装好了 anaconda, python3.7, pip 等。这次需要新增安装 3 个库。

你可能会困惑，我如何得知应该安装哪些库呢？很简单，顺着官方的 10 分钟搞定文档逐行尝试，最初的 3 行就是答案。

```python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 在我的本地编辑器输入这 3 行代码后，import 部分被打了红色波浪线，这就是提示我未安装相应模块。

```

我的本地编辑器用的是 vscode，如果我未安装某个模块，它会有如下提示。但用 anaconda prompt 安装以上 3 个库时并不顺利，一方面终端告诉我已经安装好了，另一方面编辑器中依然有未安装的提示。

![img](https://user-images.githubusercontent.com/31027645/62598685-cc573180-b91c-11e9-8eb0-eeeb8e2d0cd7.png)

在网上搜并尝试了后，最终是通过 windows 10 自带的 cmd 调出终端执行 pip install 才搞定。

![img](https://user-images.githubusercontent.com/31027645/62598883-4c7d9700-b91d-11e9-9fe5-feace692fba9.png)

如何验证自己是否安装成功呢？作为新手我也曾困惑于此，这个经验分享如下。

方式一，是启用 python 自带的 IDE 输入 `import pandas as pd`并回车，如无报错，才说明 pandas 安装成功了。

方式二，是 vscode 中创建新的 `.py` 类型的文件，输入 `import pandas as pd` 后无任何红线提示。

### 准备工作：python 基础

学 pandas 的最少必要知识是什么呢？完全没学过 python 恐怕非常困难。

我自己是仅掌握了 python 的基础知识，对部分进阶知识有所了解，即《自学是门手艺》中的内容。这个程度，到底够不够，我没办法预判，但我可以边走边看。

当然，学习新技能的最大资源其实是时间和精力。这个就不再多说。

准备工作就到此为止。

## 二、找到入口

### 太难没耐心，换姿势找线索

接下来的学习过程，每个人有自己特定的方法论或习惯。我的方法或节奏不一定适合你，仅供参考。

最初我先顺着官网的 10 分钟文档，在自己的本地编辑器逐行敲下代码并运行。除了对于 output 感到小惊喜外，整个过程一脸懵逼。花了半小时左右，学了数据的创建和获取，我便没耐心逐行尝试了。

没耐心当然不是不学，而是换一个姿势学。我快速浏览了官方的 10 分钟文档下面的内容，大概是讲数据的增删改查文件读取绘图之类的处理。我的一个基本判断是：

> 我遇到的第一个难点，在最前面。我应该优先解决这个难点，要不然后面只会如同天书。

于是我检索了一些中文的文章，并快速找到一个关键信息：

> 最好对 python，pandas 和 numpy 有一丢丢的小了解，最起码对 series, array, dataframe 等基本概念有所了解。

我对 python 当然是有一丢丢的小了解，但对 pandas 这不刚接触呢。numpy 更是首次听说，`series, array, dataframe` 这三个概念很陌生啊！

——慌什么！这不刚抓到了最重要的线索？大喜事啊。所谓线索，就是作为关键词去搜索别人的好文章来读，筛选并构建自己所需的知识。

得出判断：

> **我的入门关键，就是先理解 `series, array, dataframe` 这三个概念。**


### 用已知理解未知

从第一个概念开始：series 是什么呢？

欠缺背景知识的人，通常比较难抽象地理解新知识。我的办法是：写一些代码来让自己形象地认知。既然在官网的 10 分钟文档最初部分创建对象时，也用到了列表 list 和字典 dict，那么，我就用这 2 个数据容器，来理解 series。

以下这段代码，我逐步写然后运行，理解后再继续写，再运行……

```python

"""
形象地理解 list 与 series 的关联和区别。
"""

import pandas as pd
import numpy as np

list_a = [1,3,5,6,'好','good']
series_x = pd.Series(list_a)

print(list_a)
print(type(list_a))
print()

print(series_x)
print(type(series_x))
print()

```


```python

"""
形象地理解 dict 与 series 的关联与区别。
"""

import pandas as pd
import numpy as np

dict_a = {'Ohio':35000,'Texax':71000,'Oregon':16000,'Utah':5000}
series_y = pd.Series(dict_a)

print(dict_a)
print(type(dict_a))
print()

print(series_y)
print(type(series_y))
print()

```


有了形象的认知，再继续读别人有关 `series` 的文章，就比较好懂一些。通常 `series` 的文章也会提及`dataframe`，关于两者的区别与关联，让我好理解的一个说法是：
> 区别：
> series，只是一个一维数据结构，它由 index 和 value 组成。
> dataframe，是一个二维结构，除了拥有 index 和 value 之外，还拥有 column。
> 联系：
> dataframe 由多个 series 组成，无论是行还是列，单独拆分出来都是一个 series。
> 来源：[pandas 中 Series()和 DataFrame()的区别与联系](https://blog.csdn.net/missyougoon/article/details/83301712)

通读一些文章后，我现在能清晰一些理解 `series` 和 `dataframe` 了，不再像之前那样模糊。此时面临 2 个选择，其一是继续按官网文档挨个尝试它的各种方法，其二是从一个具体需求切入，看看怎么用。

我已经知道 pandas 大概有哪些功能或方法，能做些什么，只是还不知道具体怎么做。目前备查的材料充分且可靠，我对材料的结构也比较清晰，于是我选择方向二，找一个具体的需求来动手实操。实操的过程中，来搜查使用以上知识点。

