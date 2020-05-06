#         -4  -3  -2  -1
list01 = [9, 25, 12, 8]
for i in range(-1,-len(list01)-1,-1): # for i range(-1,-5,-1)
    if list01[i] > 10:
        list01.remove(list01[i])
print(list01) # [9, 8]