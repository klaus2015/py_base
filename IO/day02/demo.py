
f = open('haha','w+')

f.write('hell')
print(f.tell())
f.flush()
f.seek(0,0)

data = f.read()

print(data)

f.close()