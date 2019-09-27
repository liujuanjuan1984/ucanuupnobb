# windows 10 如何设定计划任务自动执行 python 脚本？

我用 `python` 写了一些脚本，有一些是`爬虫`脚本，比如爬取知乎特定话题的热门问题，有一些是定期的`统计分析`脚本，输出统计结果到文档中。之前我都是手动执行这些脚本，现在我希望如何这些脚本能自动定时执行。那么，windows 10 操作系统如何定时自动执行 python 脚本？

我的设备是 windows 10操作系统，自带的“计划任务”可以满足我的需求，具体操作步骤，整理如下。

## 步骤1：打开 “计算机管理” 界面

点击电脑左下角的windows图标，或者键盘的windows按键。

![image](https://user-images.githubusercontent.com/31027645/64669032-87ca3300-d492-11e9-8158-3be079f41812.png)

在弹出的界面中，鼠标移到“此电脑”上右键点击，选择“更多”-‘管理’，点击则可进入“计算机管理”界面。

![image](https://user-images.githubusercontent.com/31027645/64668693-1d64c300-d491-11e9-9ebd-062ce7f02dfe.png)

## 步骤2：开始 “创建基本任务”

在打开的“计算机管理”界面上，依次点击“系统管理”-“任务计划程序”，然后最右侧选择“创建基本任务”，即可开始创建计划任务。

![image](https://user-images.githubusercontent.com/31027645/64669112-d677cd00-d492-11e9-8583-c467922e3751.png)

## 步骤3：输入计划任务的基本属性

计划任务的属性设置分为多个步骤，按照操作提示一步步来即可。即便刚开始弄错了，之后也可以修改或完善。所以不要紧张。第一次使用时，可按照以下截图依次尝试：

#### - 输入该任务的名称和描述。

注意：这是写给自己看的哟，最好标记清楚，避免时间久了自己迷糊了。

![image](https://user-images.githubusercontent.com/31027645/64669135-ef807e00-d492-11e9-8ddd-2d99184ca6bf.png)

#### - 设定计划任务的频率。

注意：根据你的具体需求来设定。比如我的知乎爬虫脚本2小时一次，而统计分析脚本则每天一次即可。

对于每隔2小时一次的计划任务，也可以选择每天，后面可以增加多个时段。比如每天的6,8，10,12,14点等等分别执行。刚开始先设置一个时间点即可。之后再增加其它时间点。下文将详细说明。

对于python脚本来说，它的类型是：程序。

![image](https://user-images.githubusercontent.com/31027645/64669343-cd3b3000-d493-11e9-953f-37898b2e1504.png)

- 程序和脚本：这里填写 python 的安装路径。点击浏览“浏览……”会自动弹出选择界面。
- 添加参数（可选）A： 这里填写我的python 爬虫脚本的绝对路径。比如我的脚本是：

C:\Users\username\python_side_projects\crawler\crawler_base\zhihu_topic_monitor_exe.py

![image](https://user-images.githubusercontent.com/31027645/64669351-d62c0180-d493-11e9-91db-bef6b78fa27e.png)

系统默认打开的路径，并没有我想打开的 python.exe 怎么办？简单……往下看。

![image](https://user-images.githubusercontent.com/31027645/64669364-dd530f80-d493-11e9-93f6-b87287d4ae6d.png)

这里遇到一个小知识点：

## 知识点：如何查找 python 安装在哪里？

启动cmd（命令行提示符），输入：`where python` 即可。下面看到，我的电脑上装了两个python，选择你常用的那个版本即可。

![image](https://user-images.githubusercontent.com/31027645/64669371-e3e18700-d493-11e9-9d2f-81604f6e9218.png)

按照上述路径提示，打开对应文件夹，选中 `python.exe` 即可。

![image](https://user-images.githubusercontent.com/31027645/64669393-f6f45700-d493-11e9-88af-4bc3c29c6f18.png)

按照以上步骤设定好计划任务的属性，点击完成就行啦。等等……我刚才希望爬虫脚本每隔2小时就执行一次，如何设定呢？

## 小技巧：每隔2小时就运行一次，如何设定计划任务。

先新建一条普通的计划任务，或选择已有的计划任务，选择“属性”打开计划任务的属性界面。

![image](https://user-images.githubusercontent.com/31027645/64669421-17241600-d494-11e9-96ba-e1a2d70e22f3.png)

在“触发器”这个页签，按需求，添加更多时间点，然后提交完成即可。

![image](https://user-images.githubusercontent.com/31027645/64669443-2b681300-d494-11e9-96be-d39db509047a.png)

## 经验：遇到报错所指定的账户名称无效，怎么办？

![image](https://user-images.githubusercontent.com/31027645/64669499-5b171b00-d494-11e9-8637-af01eb818b99.png)

简单来说，在计划任务属性页面，点击“更改用户或组”，输入用户名（比如我的“75801”），然后点击“检查名称”，再点击“确定”提交，就可以了。详细的图文说明，请挪步我的另外一篇整理：

> [https://juejin.im/post/5d7881a6e51d453bdb1d9bd9](https://juejin.im/post/5d7881a6e51d453bdb1d9bd9)