
def sub_sort(list_,low,high):
    x = list_[low]
    while low < high:
        # 从前往后
        while list_[high] >= x and high >low:
            high -= 1
        list_[low] = list_[high]

        while list_[low] < x and high > low:
            low += 1
        list_[high] = list_[low]
    list_[low] = x
    return low



def quick(list_,low,high):
     if low < high:
        key = sub_sort(list_,low,high)
        quick(list_,low,key-1)
        quick(list_,key+1,high)



l = [5,5,3,2,15,8,4,13,7,6]
#sub_sort(l,0,len(l)-1)
quick(l,0,len(l)-1)
print(l)