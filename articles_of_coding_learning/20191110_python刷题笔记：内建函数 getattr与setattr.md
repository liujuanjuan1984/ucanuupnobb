# Python 刷题笔记：内建函数 getattr 与 setattr

## 1、刷题遇到知识盲区

今天继续在 [xue.cn](https://xue.cn/) 刷题，发现知识盲点：getattr 与 setattr 未曾听闻。我有个通用解决办法，搜索：`getattr  site:python.org` —— python 官方文档，是自学 python 编程最好的资料。这个意识相当重要，我拥有这个意识，完全来自于[《自学是门手艺》](https://xue.cn/)。

暂时难住我的题目如下：

> What gets printed?
```python
class A:
    def __init__(self, a, b, c):
        self.x = a + b + c

a = A(1,2,3)
b = getattr(a, 'x')
setattr(a, 'x', b+1)
print(a.x)

```

## 2、搜索 python 官方文档

搜索结果表明，getattr, setattr, hasattr, delattr 这四个相关函数都是 [python 的内置函数](https://docs.python.org/3/library/functions.html)。如果英文不太好，可在 python 官网左上角选择简体中文。以下摘抄自 python 官方文档：

### **getattr(object, name[, default])**

> 返回对象命名属性的值。name 必须是字符串。如果该字符串是对象的属性之一，则返回该属性的值。例如， getattr(x, 'foobar') 等同于 x.foobar。如果指定的属性不存在，且提供了 default 值，则返回它，否则触发 AttributeError。

### **hasattr(object, name)**

> 该实参是一个对象和一个字符串。如果字符串是对象的属性之一的名称，则返回 True，否则返回 False。（此功能是通过调用 getattr(object, name) 看是否有 AttributeError 异常来实现的。）

### **setattr(object, name, value)**

> 此函数与 getattr() 两相对应。 其参数为一个对象、一个字符串和一个任意值。 字符串指定一个现有属性或者新增属性。 函数会将值赋给该属性，只要对象允许这种操作。 例如，setattr(x, 'foobar', 123) 等价于 x.foobar = 123。

### **delattr(object, name)**

> setattr() 相关的函数。实参是一个对象和一个字符串。该字符串必须是对象的某个属性。如果对象允许，该函数将删除指定的属性。例如 delattr(x, 'foobar') 等价于 del x.foobar 。

## 3、正确解题
浏览 python 官方文档 以上 四个函数的说明后，就很好理解啦。

```python

#定义一个类，并设置初始化方法
class A:
    def __init__(self, a, b, c):
        self.x = a + b + c 

#生成一个实例
a = A(1,2,3) 
# 获取对象 a 的属性 x 的值，根据类定义，应为 1 + 2 + 3 即 6
b = getattr(a, 'x') 
# 设置对象 a 的属性 x 的值为 b+1，b 上面计算得出为 6，所以 x 被设置为 6+1 即 7
setattr(a, 'x', b+1) 
# 打印对象 a 的属性 x ，值为 7
print(a.x) 
```

所以，正确答案为 7 ~