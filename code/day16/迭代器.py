tuple01 = ("铁扇公主","铁锤公主","扳手王子")
iterable = tuple01.__iter__()
print(iterable)
while True:
    try:
        item = iterable.__next__()
        print(item)
    except StopIteration:
        break

dict01 = {"铁扇公主":101,"铁锤公主":102,"扳手王子":103}
iterable = dict01.__iter__()
while True:
    try:
        key = iterable.__next__()

        print(key,dict01[key])
    except StopIteration:
        break


