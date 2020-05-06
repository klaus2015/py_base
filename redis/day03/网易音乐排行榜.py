'''网易音乐播放量排行榜 前三'''

import redis

r = redis.Redis(host='localhost',port=6379,db=0,password='123456')

# song:rank

r.zadd('song:rank',{'song1':1,'song2':1,'song3':1,'song4':1,'song5':1,'song6':1})

# 增加分值
r.zincrby('song:rank',50,'song1')
r.zincrby('song:rank',60,'song5')
r.zincrby('song:rank',20,'song4')

# 查看排名

res = r.zrevrange('song:rank',0,-1,withscores=True) # [(b'song5', 61.0), (b'song1', 51.0), (b'song4', 21.0),
# (b'song6', 1.0), (b'song3', 1.0), (b'song2', 1.0)]
i = 1
print(res)
for re in res:
    print('第{}名:{} 播放次数{}'.format(i,re[0].decode(),re[1]))
    i += 1