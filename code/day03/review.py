"""
    day02 复习
    数据基本运算
        变量：关联一个对象的标识符
            变量名　＝　？　
            　变量没有类型
        数据类型:
            None
            int       1      2
            float　　　1.0   2.5
            str      ""    "字符"
            bool　　　True  False
            复数　complex

        类型转换
            int(数据)　　float(数据)
            str(数据)    bool(数据)
            如果数据的格式不正确，会错误。
                例如：int("100+")
            如果数据表示"没有",转换结果为Ｆａｌｓｅ
                bool(1) --> True
                bool("") -->False

        运算符
            算数运算符：＋　－　＊　　／　／／　％　**
            增强运算符:＋=　－=　＊=　　／=　／／=　％=　**=
                a = 10
                a = a + 5
                a += 5
            比较运算符:>  <  >=  <=  ==  !=
            逻辑运算符: 1 > 2   "a" == "b"
                       False or False
                      与　and : 一假俱假
                      或　or :一真俱真
"""

a = 1
a = "ａ"
a = True

# 问题：控制台中会出现什么
# 短路逻辑：逻辑运算时，尽量将复杂(耗时)的判断放在后边。
num = 1
# and 发现Ｆａｌｓｅ，就有了结论,后续条件不再判断。
# re = num > 1 and input("请输入：") == "a"

# or 发现Ｔｒｕｅ，就有了结论,后续条件不再判断。
re = num + 1 > 1 or input("请输入：") == "a"