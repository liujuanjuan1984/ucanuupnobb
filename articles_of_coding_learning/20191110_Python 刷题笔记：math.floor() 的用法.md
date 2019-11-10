# Python 刷题笔记：math.floor() 的用法

## 1、刷题遇到知识盲区

今天继续在 [xue.cn](https://xue.cn/) 刷题，发现知识盲点：math 模块的 floor() 方法未曾听闻。我有个通用解决办法，搜索：`floor site:python.org` —— python官方文档，是自学python编程最好的资料。这个意识相当重要，我拥有这个意识，完全来自于[《自学是门手艺》](https://xue.cn/)。

题目倒也简单，如下：

> What gets printed by the code snippet below?

```python

import math
print(math.floor(5.5))
```

## 2、搜索python官方文档

搜索结果稍微有点麻烦，推荐链接是 python 2.X版本，且是英文的：
> math.floor(x)
> Return the floor of x as a float, the largest integer value less than or equal to x.

好在这个英文也不困难，能大概读懂，意思是说，输入 float 类型的x，返回 x 的取整数，该取整数将小于等于 x。

有时对自己的英语阅读理解能力不自信，又不想借助翻译工具，我会直接在 xue.cn 上敲入代码并运行，看看结果是否和自己的猜测相符：

![image](https://user-images.githubusercontent.com/31027645/68541668-72637d80-03dd-11ea-9a10-c1618e4500b3.png)

## 3、正确解题

理解了 math.floor() 的作用，现在答案就容易知晓啦。5.5 取整数为 5，正确答案是整数 5。
