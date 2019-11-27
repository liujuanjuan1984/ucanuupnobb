# 【呕心总结】python 如何与 mysql 实现交互及常用 sql 语句

9 月初，我对 `python 爬虫` 燃起兴趣，但爬取到的数据多通道实时同步读写用`文件`并不方便，于是开始用起`mysql`。这篇笔记，我将整理近一个月的实战中最常用到的 `mysql` 语句，同时也将涉及到如何在`python3`中与 `mysql` 实现数据交换。

关于工具/库，特别说明下：

1、我安装了 `mysql` ，并直接采用管理员身份运行`命令行提示符（cmd）`查看 `mysql`，并没有安装任何 `mysql` 的可视化图形界面工具。

2、在 `python` 脚本中，我采用 `pymysql` 和 `sqlalchemy` 这两个库与 `mysql` 建立连接，用 `pandas` 来处理数据。

## 一、建立连接与数据交互

与 mysql 交互的方式，我目前共使用 4 种。其中采用管理员身份运行`命令行提示符（cmd）`查看 `mysql`，其操作图示可另写一篇。这里就不占篇幅了。mysql 的可视化图形界面工具，我目前并没有用到，也没有迫切使用它的需要。另外 3 种方式都是通过 python 脚本进行。

### 情境 A：python 演算得出数据，想要写入数据库

python 脚本已得到表格类大量数据，想要一次性写入数据库，常用代码如下：

```
import pandas as pd
# 与 mysql 建立连接
from sqlalchemy import create_engine
conn_eng = create_engine('mysql+pymysql://username:password@localhost:3306/databasename',encoding='utf8')  

# 调用 pandas 的方法，数据写入 mysql
pd.io.sql.to_sql(your_df, "table_name", conn_eng, if_exists='append',index=False)

```
表格类数据，我用的是 `pandas` 的 `dataframe` 结构。`pd.io.sql.to_sql()` 的参数还有许多其它用途，但上面这种是我个人使用最高频的。效果是：无需自己提前建表，将自动建新表。美中不足是：表的列属性自动生成，通常不合心意，还需检查和修改。

如果不想用 `pd.io.sql.to_sql()` 或者想更精细、复杂的操作，则用到下面的情境 C。

### 情境 B：python 脚本想从 mysql 拿到数据

如果已经存在某个表格，想要向该表格提交某条指令，需返回数据，我用的是 `pandas`的`read_sql
()` ，返回的数据类型是 `pandas` 的 `dataframe`。sql 查询语句挺好写的，具体总结在本文下方。

```python
import pymysql
# 与 mysql 建立连接
conn = pymysql.connect('localhost','username','password','databasename')
# sql 语句定义为一个字符串
sql_search = 'select question_id from topic_monitor where is_title=0 ;'
# 调用 pandas 的 read_sql() 方法拿到 dataframe 结构的数据
question_ids = pd.read_sql(sql_search,conn)
# 关闭连接
conn.close()
```

### 情境 C：python 脚本单方面向 mysql 发出指令，无需拿到数据

如果已经存在某个表格，想要向该表格提交某条指令而无需返回数据时，比如：建表、对数据的增改删、对列的名称、列的属性修改等，代码如下。


```
import pymysql
# 与 mysql 建立连接
conn = pymysql.connect('localhost','username','password','databasename')
cursor = conn.cursor()
# sql 语句定义为一个字符串，插入一行数据
sql_insert = 'INSERT INTO questions(q_id,q_title,q_description,q_keywords,q_people,q_pageview,time) VALUES( "'\
                + str(quesition_id) + '", "' + str(one[0])+ '", "' + str(one[1]) + '", "' + str(one[2]) + '", "' \
                + str(one[3]) + '", "' + str(one[4]) + '", "' + str(datetime.datetime.now()) + '");' 
# sql 语句定义为一个字符串，修改某个数据（另一个表格）
sql_update = 'update topic_monitor SET is_title="1" where question_id = "' + str(quesition_id) + '";'
# 提交指令
cursor.execute(sql_insert)
cursor.execute(sql_update)
conn.commit()

# 插入一行数据；仅当该数据与表格已有数据不重复时才插入，否则就不会插入
sql_insert = 'INSERT INTO `topic_monitor`(question_id,is_title,q_type,topic_id,time) SELECT "'\
                    + x[0] + '", "0", "0","'  + str(topic_id) + '", "'+ str(now) + '" FROM DUAL WHERE NOT EXISTS(\
                    SELECT question_id FROM topic_monitor WHERE question_id = "' + x[0] + '")'
cursor.execute(sql_insert)
conn.commit()

# 关闭连接
cursor.close()
conn.close()
```

通过上面几种实用情况可以看到，`python` 与 `mysql` 实现交互的过程，通常分为：建立连接、把 sql 语句定义为字符串，提交指令、关闭连接。核心的技能在于 sql 语句；除了定义 sql 语句字符串，其余 3 个处理都是固定的写法。

我在最初一个月的实践中，最常出现的错误有：
- 值的引用没有加上引号；
- 符号错乱：多一个符号，少一个符号；
- 值的类型不符合：不管 mysql 表格中该值是数，还是文本，在定义 sql 语句的字符串时，对每个值都需要转化为字符串；
- 拷贝自己的代码时，忘记修改 databasename。


## 二、sql 语句：搜索查询

搜索是指在数据库的某个表格中查询符合特定条件的数据，并返回查询结果。其基本结构为：

`SELECT 【范围】FROM table_name  【条件】;` 其中，范围是必须指定的，而条件可有可无。

### 变量 A：范围，是指返回查询结果的范围。

返回该表格的所有字段，用 * 表达：

```mysql
SELECT * FROM table_name ;
```
![image](https://user-images.githubusercontent.com/31027645/65767128-93d71580-e15f-11e9-8e4a-e3c52c4e4759.png)


仅返回该表格的某个字段：

```mysql
SELECT column_name FROM table_name ;
```

仅返回该表格的多个字段：

```mysql
SELECT column_name_1,column_name_3,column_name_3 FROM table_name ;
```

![image](https://user-images.githubusercontent.com/31027645/65767152-a2bdc800-e15f-11e9-8759-9479071f20af.png)

仅返回符合条件的数据个数：

```mysql
SELECT count(*) FROM table_name ;
```
![image](https://user-images.githubusercontent.com/31027645/65767216-cc76ef00-e15f-11e9-932c-1fa42fbde121.png)

### 变量 B：条件是指，期望返回的数据满足哪些条件。

不限定条件：

```mysql
SELECT * FROM table_name ;
```
数值类：某个字段（数值类型的，比如 double 或者 int），数值比较的操作符都可以使用比如，大于`>`，小于`<`，等于 `=` ，大于等于 `>=` ，小于等于 `<=` ：

![image](https://user-images.githubusercontent.com/31027645/65767326-211a6a00-e160-11e9-9a82-902c35200d80.png)


```mysql
SELECT * FROM table_name WHERE num_column_name >= 1;
```

文本类：某个字段（字符串类型的，比如 char，text）：

```mysql
SELECT * FROM table_name WHERE str_column_name like “%your_str%”;
```
![image](https://user-images.githubusercontent.com/31027645/65767368-4909cd80-e160-11e9-9cd2-83bc211d714f.png)

也可以表达多个条件，`and`，`or`等可用于表达条件之间的关系：

```mysql
SELECT * FROM table_name WHERE num_column_name_1 >= 1 and  str_column_name like “%your_str%” ;
```
![image](https://user-images.githubusercontent.com/31027645/65767478-938b4a00-e160-11e9-906b-02ccddfbfad0.png)

## 三、sql 语句：修改表属性

横向的一整条数据，叫做行；竖向的一整条数据，叫作列。列的名字，叫做 `column`，这是通用的知识点。

这段时间的实战中，我完全没有用到修改表的名称、重设 index 等知识点。最常用的，就是对列进行操作。每个列具备：列的名称、列的属性、列的数值。

列的名称，需要留心不使用保留词。我的技巧是，尽量用一些`_`来表达该数据，比如 `article_title`，`press_date` 这种命名虽然稍长，但易读，也不会装上保留词。

列的属性包括：类型，最大长度，是否为空，默认值，是否重复，是否为索引。通常，直接通过 `pandas` 的 `pd.io.sql.to_sql()` 一次性创建表格并保存数据时，列的默认属性并不合需求。要么提前自己定义表的结构，设置好每列属性；要么事后检查列属性，并逐列修改。所以，列的属性设定、修改是高频基础知识点。

列的数值，即除了列名称外的、该列其它值。修改某个值，也是高频操作。不过我把这个知识点放到第四部分了。

对列的名称、列的属性进行修改，主要的关键词都是 `ALTER`，具体又分为以下几种情况。

### 情境 A：新增一列。关键词 `ADD` 

在你所指定的 `column_name ` 后面定义列的属性。

```mysql
ALTER TABLE table_name ADD COLUMN column_name char(20);
```
### 情境 B：修改某列的名称。关键词 `CHANGE`

在修改列名的同时也可以重新指定列的属性。

```mysql
ALTER TABLE table_name CHANGE old_column_name new_column_name char(50);
```

### 情境 C：修改某列的属性。关键词是 `MODIFY`

```mysql
ALTER TABLE table_name MODIFY column_name char(100);
```


## 四、sql 语句：数据的增改删

通常提到数据库操作时，四字以蔽之：增删改查。
- 查询，请看第二部分。关键词是 `SELECT`。
- 对数据所依赖的属性的增、改，请看第三部分。关键词是 `ALTER`。
- 数据的增加，在第一部分的数据交互中也给出实例，就不重复了。关键词是`INSERT`。
- 数据的修改，关键词是 `UPDATE`。
- 数据（甚至表格、库）的删除，关键词是`DELETE`。

数据的修改，副关键词是 `set` 。

```mysql
UPDATE table_name SET columns_name = new_value 【条件】;
```

新数值如果是数值类型的，则直接写数值即可；如果是文本类型的，必须要加上双引号，比如，`“your_new_value”`。

如果把【条件】部分不写，就相当于修改整列的值；想要修改特定范围，就要用到条件表达式，这和前面的查询部分是一致的，就不再重复。

数据的删除，对于新手来说，是必须警惕的操作。因为一旦误操作，你将无力挽回。即便是职业程序员，也可能犯下无疑删库的惨剧。其基本语句为：

```mysql
DELETE FROM table_name【条件】;
```

想要修改特定范围，就要用到条件表达式，这和前面的查询部分也是一致的，稍微啰嗦两句：不要对自己设定的条件太自信，最好先用搜索语句检查一下，然后再执行删除语句。

- 删除单行数据：添加能唯一标识该行数据的条件语句。
- 删除多行数据：添加能标识该范围的条件语句。
- 删除整张表格：**你是认真的吗？没有写错表格名字吧？！** 做这项操作前，必须确认清楚自己的意图，毕竟一旦发生，无可挽回。

如果条件留空，将保留表结构，而删除所有数据行。想要删除整张表格，什么都不留下，则执行：

```mysql
DELETE TABLE table_name;
```
俗称的“删库”就是删掉整个数据库，虽然实战中几乎不会用到，但作为新手经常手误，在练习阶段安全起见，最好还是专门创建一个 database 用于练手，练完直接删掉整个练习库：

```mysql
DELETE DATABASE database_name;
```

如果简单总结下过去一个月，使用`mysql`的体验，那就是：除了 mysql 的安装激活太麻烦，数据的增删改查比操作文本方便太多了！！完全值得容忍安装激活的麻烦。另外 mysql 常用语法确实简单、非常有规律。

希望我的总结带给你帮助。鼓励我继续分享，那就请点个赞吧！勘误请留言，或挪步我的 github：[https://github.com/liujuanjuan1984/ucanuupnobb/issues](https://github.com/liujuanjuan1984/ucanuupnobb/issues)