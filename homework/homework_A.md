
## 准备vscode + github，并熟悉github的最少必要操作。

### 第1次：

1、电脑上安装软件 vscode。

请选择官网下载安装： https://code.visualstudio.com/

2、创建一个markdown文件（即以.md为后缀的新文件），然后在文件中写下你遇到的困难，以及如何解决的。

以后的学习记录，都以该方式添加：要么在该文件中添加，要么创建新的文件。

-----

### 第2次：

1、注册github账号。

官网地址：https://github.com/

2、创建一个新项目/新仓库 Create a new repository 。操作入口在右上角你的头像旁边，有个＋号。

3、在新创建的项目/仓库页面，简单熟悉它的 Readme 与 issues 的使用。

readme 是这个项目/仓库的实名说明书；issues 可以当做一个小的论坛使用。

4、继续在vscode上增加你的学习记录。

------

### 第3次：

1、在github 你的项目/仓库页面 <>code 页找到 绿色按钮：clone or download，点击它并复制你的项目/仓库的 url。

2、本地创建文件夹。

2.1 选择你本地电脑的一处地方，建立一个文件夹，比如：codingstudy 作为代码学习专用。

2.2 在vscode中选择file - open fonder 打开上述文件夹。

3、在 vscode 中，打开terminal，并确保terminal的光标所在位置刚好在上述文件夹。

`cd ..` 返回上一层文件夹

`ls` 显示当前目录下的文件/文件夹

`cd 文件夹` 进入当前目录下的某个文件夹

4、在上述文件下使用git clone指令，即把你的新仓库，克隆到你的本地vscode。

`git clone url `

5、完成后，你可以在左侧文件树结构中看到你的项目，你可以添加更多文件夹来管理与此相关的记录。比如创建一个文件夹存放你的学习记录。

主文件夹 /codingstudy/

你的仓库地址 /codingstudy/yours/

你的学习记录 /codingstudy/yours/notes/

6、你可以直接在左侧文件树中拖拽来管理文件，也可以在电脑中打开对应文件夹来剪切粘贴来完成文件管理。

7、继续在vscode上增加你的学习记录。

----

### 第4次：

1、在vscode中，打开terminal，并进入到你的仓库

2、采用以下指令，把你的学习记录上传到github上。（以后你都可以通过vscode来上传，而不直接在github上操作）

`git add 文件名/文件地址 `

`git commit -m "你的注释"`

`git push origin master `

3、你可以对vscode上的文件做小幅度更改，反复练习以上操作。

4、如果你对文件目录相关的指令不熟悉，也可以继续反复练习。

5、继续在vscode上增加你的学习记录。并通过vscode terminal 的git指令来提交上传到github上。


----

### 第5次：

1、复习以上，并把本次所有的学习记录，整理提交到自己的github上。
