# 反向打印列表时，不要用切片（切片会重新复制列表），要用索引（倒着）
# 容器的目的，储存、管理多个数据
# 列表名称实际指向的是 表头，表头再指向存储在其中的变量的地址，扩容的时候，只是表头的指向改变，省去列表名称的变化（接口）
# 哈希算法------> 所有容器中的查找，字典的查找是最快的，但是所需空间较大（即利用空间（内存）换取时间（cpu计算时间））
# 创建空列表、空元组、龙字典中的相同操作
# 字典键值 修改时，查看键是否已经存在很重要
# 字典列表组合重新学习练习