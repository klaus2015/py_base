"""
时间如果不需要比较大小,可以直接传入字符串表示时间
now() 返回服务器当前时间 ---datatime
curdate() 返回当前日期----data
curtime() 返回当前时间 只有时间,并返回当前日期-----time
date(date) 返回指定时间的日期
time(date) 返回指定时间的时间
模糊查询---只针对字符串有效
UNION 操作符语法格式 效率比and高
mysql> select * from class_1;
+----+------+-----+------+-------+--------------+
| id | name | age | sex  | score | 入学时间     |
+----+------+-----+------+-------+--------------+
|  1 | Abby |  18 | w    |  89.5 | 2019-05-06   |
|  2 | Tom  |  10 | m    |   100 | 2019-02-28   |
|  3 | mark |  19 | m    |     0 | 2019-03-18   |
|  4 | lucy |  18 | w    |  91.7 | 2019-03-08   |
+----+------+-----+------+-------+--------------+
mysql> select * from class_1 order by score desc limit 3; 按成绩前三查询
+----+------+-----+------+-------+--------------+
| id | name | age | sex  | score | 入学时间     |
+----+------+-----+------+-------+--------------+
|  2 | Tom  |  10 | m    |   100 | 2019-02-28   |
|  4 | lucy |  18 | w    |  91.7 | 2019-03-08   |
|  1 | Abby |  18 | w    |  89.5 | 2019-05-06   |
+----+------+-----+------+-------+--------------+

mysql> select * from class_1 where sex='m' order by 入学时间 limit 1; 查找第一个入学的男
+----+------+-----+------+-------+--------------+
| id | name | age | sex  | score | 入学时间     |
+----+------+-----+------+-------+--------------+
|  2 | Tom  |  10 | m    |   100 | 2019-02-28   |
+----+------+-----+------+-------+--------------+




"""