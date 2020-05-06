"""
二分查找
"""
def search(list_,key):
    low, high = 0 ,len(list_)-1
    while low <= high:
        mid = low + high // 2
        if key > list_[mid]:
            low = mid + 1
        elif key < list_[mid]:
            high = mid - 1
        else:
            return mid

l = [1,2,3,4,5,6,7,8,9,10]
print(search(l,4))

