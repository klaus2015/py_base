from day02.sstack import *
st = SStack()



def check_brace(str_raw):
    if str_raw == "":
        return True

    st._elems = []
    count = 0
    while count <len(str_raw):
        l_item = str_raw[count]
        count += 1
        if l_item in ["(","[","{"]:
            st.push(l_item)

        elif l_item in [")","]","}"]:
            len_stack = len(st._elems)
            if len_stack == 0:
                return False
            else:
                if l_item == ")" and st._elems[len_stack - 1] == "(":
                    st._elems.pop(len_stack - 1)
                elif l_item == "]" and st._elems[len_stack - 1] == "[":
                    st._elems.pop(len_stack - 1)
                elif l_item == "}" and st._elems[len_stack - 1] == "{":
                    st._elems.pop(len_stack - 1)
                else:
                    return False

    if st._elems == []:
        return True
    else:
        return False

print(check_brace("abc(d[efg[hahah])],and [today is a good day],now i (will go to [school])"))


