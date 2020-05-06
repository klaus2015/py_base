# 顺序存储,遍历速度快插入删除元素速度稍慢,原因为紧密排列,增加删除后,其他元素都要往后移动腾出或补齐位置
# 链表遍历速度慢,插入删除效率高
# 1,2,3进栈,不可能出栈的顺序是3,1,2
# 当对象内用__dict__ 保存的实例变量时，通过修改__dict__的字典可以完成增、删、改、查实例变量
#Python中元组是不可变数据类型，和字符串，列表一样属于序列的一种，可迭代；支持下标索引，支持切片访问。
# 5>3==True 相当于5>3 and  3 == True。
# dict内有__getitem__方法
# 字典是Python中内建的一种映射类型，采用键值对存储数据，字典是无序的，字典的Key需要时不可变、可哈希的类型，值可以是任意类型
# a = frozenset((1,2,3))，b = {2, 3, 4}以下操作可正确执行的是？（）

#迭代器必须用__next__方法来实现迭代器协议  __iter__方法是可迭代对象用来返回迭代器  任何对象都能进行bool(x)取值，
# 当有__bool__方法时，取__bool__方法的返回值，没有__bool__方法时用__len__方法的值进行判定，如果再没有__len__方法，则返回True

#Python是强类型语言，字符串和整数不能直接+/-运算，字符串支持+（连接）操作、*（复制）操作。int可以将浮点数转换成整数（取整），
#可以把合法数字字符串转换成整数，字符串中不能含有数字意外的字符，如小数点等

#str函数是把一个数字类型对象转换成一个字符串类型对象，
# float是把一个字符串（只含有数字和小数点）的对象转换成一个浮点型对象，
# int是把浮点对象或者只含有数字字符的字符串对象转换成一个整数对象
def check_brace(str_raw):
    # 如果传入为空，直接返回True
    if str_raw == "":
        return True

    # 定义一个空列表，模拟栈。
    stack = []

    while str_raw != "":
        # 获取本次循环的字符串的第一个字符
        thisChar = str_raw[0]
        # ^_^去掉第一个元素
        str_raw = str_raw[1:]
        # 如果本次循环的第一个字符是左括号，将其压栈
        if thisChar == "(" or thisChar == "{" or thisChar == "[":
            stack.append(thisChar)
        # 如果本次循环的第一个字符是右括号，检测栈是否为空，栈长为空表示栈内没有可以匹配的左括号，返回false
        # 如果栈长不为空，且栈内最后一个元素是相匹配的左括号，此次匹配成功，将其弹出，进入下一轮循环。
        elif thisChar == ")" or thisChar == "}" or thisChar == "]":
            # 提高效率
            len_stack = len(stack)
            if len_stack == 0:
                return False
            else:
                if thisChar == ")" and stack[len_stack - 1] == "(":
                    stack.pop(len_stack - 1)
                elif thisChar == "]" and stack[len_stack - 1] == "[":
                    stack.pop(len_stack - 1)
                elif thisChar == "}" and stack[len_stack - 1] == "{":
                    stack.pop(len_stack - 1)
                else:
                    return False
    # 循环结束，如果栈为空，则表示全部匹配完成
    if stack == []:
        return True
    else:
        return False


print(check_brace("abc(defg[hahah]),and [today is a good day],now i (will go to [school])"))









