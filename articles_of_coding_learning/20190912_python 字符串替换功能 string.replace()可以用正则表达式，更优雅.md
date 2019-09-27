# python 字符串替换功能 string.replace()可以用正则表达式，更优雅 

说起来不怕人笑话，我今天才发现，`python` 中的`字符串替换操作`，也就是 `string.replace()` 是可以用`正则表达式`的。

之前，我的代码写法如下，粗笨：

![image](https://user-images.githubusercontent.com/31027645/64772646-8af11c00-d583-11e9-99ad-72ef214d1e1c.png)

自从发现了`正则表达式`也生效后，代码变得优雅简洁：

![image](https://user-images.githubusercontent.com/31027645/64772659-90e6fd00-d583-11e9-8e62-8ef10068237a.png)

备注：上图中的`base_info` 是 `pandas` 里的 `dataframe` 数据结构，可以用上述方法使用 `string` 的 `replace` 方法。
