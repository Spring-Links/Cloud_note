**查看数据库**
> show databases;

**创建数据库**
> create database database_name;

**使用数据库**
> use database_name;

**创建表**
> create table table_name (id int(10),name varchat(16));

**查看创建的表字段**
> desc table_name;

**插入新的字段**
> alter table table_name add column column_name data_type;

**向表中插入数据(已知表字段结构)**
> insert into table_name(column_name) values('values1','values2')

**查看表中的数据**
> select * from table_name

**根据条件进行查询**
> select * from table_name where name='tom';

**删除表中的数据**
> delete from table_name where name='jack';

**删除表中的数据**
> delete from table_name;

**删除表**
> drop table table_name;

**修改表中的数据**
> update table_name set name='李四' where id='0001';

**修改已有字段类型**
> alter table table_name modify column column_name data_type;

**修改表的字符集**
> alter table student convert to character set utf8mb4 collate utf8mb4_unicode_ci;

insert
delete
update
select