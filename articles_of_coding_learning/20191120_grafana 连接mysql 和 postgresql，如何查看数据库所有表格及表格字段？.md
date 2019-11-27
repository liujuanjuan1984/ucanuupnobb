# grafana 连接 mysql 和 postgresql，如何查看数据库所有表格及表格字段？

以 grafana 连接以上不同数据源，mysql 和 postgresql 的处理不同。这是基础操作，简单整理如下。

查看数据库的所有表格：

```mysql
--mysql
show tables;

```

```postgresql
--postgresql
select * from pg_tables;

```

查看某个表格的所有字段：
```mysql
--mysql
describe tablename;
```

```postgresql
--postgresql
select * from tablename limit 10;
```

