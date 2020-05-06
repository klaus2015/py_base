import json

item = [{'name':'小米'},{'age':20}]

with open('app.json','w') as f:
    json.dump(item,f,ensure_ascii=False)

with open('app.json') as f:
    data = json.load(f)
print(data)