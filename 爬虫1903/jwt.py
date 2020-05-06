import base64
import hmac
import json
import time
import copy
class JWT:
    def __init__(self):
        pass

    @staticmethod
    def b64encode(content):
        return base64.urlsafe_b64encode(content).replace(b'=',b'')

    @staticmethod
    def b64decode(b):
        sem = len(b) % 4
        if sem > 0:
            b += b'=' * (4 - sem)
        return base64.urlsafe_b64decode(b)

    @staticmethod
    def encode(payload, key, exp=300):
        header = {'alg': 'HS256', 'typ': 'JWT'}
        header_json = json.dumps(header, separators=(',', ':'), sort_keys=True)  # 紧凑性加有序性
        header_bs = JWT.b64encode(header_json.encode())

        # init payload
        payload_self = copy.deepcopy(payload)  # 复制一份,防止影响到原来的参数
        if not isinstance(exp, int) and not isinstance(exp, str):
            raise TypeError("Exp must be int or str !!")
        payload_self['exp'] = time.time() + int(exp)
        payload_json = json.dumps(payload_self, separators=(',', ':'), sort_keys=TypeError)
        payload_bs = JWT.b64encode(payload_json.encode())

        # init_sign
        if isinstance(key, str):
            key = key.encode()
        hm = hmac.new(key, header_bs + b'.' + payload_bs, digestmod='SHA256')
        sign_bs = JWT.b64encode(hm.digest())

        return header_bs + b'.' + payload_bs + b'.' + sign_bs

    @staticmethod
    def decode(token, key):

        header_bs,payload_bs,sing_bs = token.split(b'.')
        # payload_json = base64.b64decode(payload_bs)
        # payload = json.loads(payload_json)
        # print(payload)
        # exp = payload['exp']
        # if time.time() - int(exp) > 300:
        #     return '已经过期'
        # return payload['user']

        if isinstance(key, str):
            key = key.encode()
        # hm = hmac.new(key, header_bs + b'.' + payload_bs, digestmod='SHA256')
        hm = hmac.new(key, header_bs + b'.' + payload_bs, digestmod='SHA256')
        # 比较两次的sign结果
        if sing_bs != JWT.b64encode(hm.digest()):
            raise
        payload_json = JWT.b64decode(payload_bs)
        payload = json.loads(payload_json)

        if 'exp' in payload:
            now = time.time()
            if now > payload['exp']:
                raise
        return payload



if __name__ == "__main__":
    t = JWT.encode({'user': 'zxm'}, '12345', 300)
    print(t)
    print(JWT.decode(t,'12345'))

# 有过期时间的token
payload = {'username':'zxm','exp':time.time()+30}

a = jwt.encode(payload, '123456', algorithm='HS256')
jwt.decode(a,'123456',algorithm='HS256') # --{'username': 'zxm', 'exp': 1566990566.4177103}


# 基本的token
token = jwt.encode({'user':'zxm'},'123456',algorithm='HS256')
jwt.decode(a,'123456',algorithm='HS256') # ---{'user': 'zxm'}

# 带有签发者的token
payload = {'username':'zxm','iss':'wo'}
a = jwt.encode(payload, '123456', algorithm='HS256')
jwt.decode(a,'123456',algorithm='HS256',issuer='wo')
# 如果两个issuer的值等于iss的则可以校验成功,否则失败


