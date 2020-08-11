# encoding:utf-8
import random
import pymongo
import logging
from datetime import datetime, timedelta
from bson import ObjectId

c = pymongo.MongoClient("mongodb://localhost:27017")
ntb = c['sms-ntb']

detail = ntb['detail']
plan = ntb['plan']
task = ntb['sender_task']
record = ntb['record']
template = ntb['template']
channel = ntb['channel']

ads = c['pddads']
user = ads['user']

user.find_one({'uid': 425740142})
user.find_one_and_update({'uid': 425740142}, {'$set': {'mobile': ''}})

datetime.fromtimestamp

sms = c['sms']
act = sms['act_v2']

mine = c['mine']
test = mine['test']

a = [{
    'arg1': 1,
    'arg2': 'a',
    'sort': 10,
}, {
    'arg1': 2,
    'arg2': 'b',
    'sort': 9,
}, {
    'arg1': 3,
    'arg2': 'c',
    'sort': 8,
}, {
    'arg1': 4,
    'arg2': 'd',
    'sort': None,
}, {
    'arg1': 5,
    'arg2': 'e',
}]

# arg1
# arg2
# arg3

record.find({
    'user_id': ObjectId('5ceb967f4f9fc9321a88ab59'),
    'schedule_t': {
        '$lt': datetime(2019, 12, 27),
        '$gte': datetime(2019, 1, 1),
    },
}).explain()


def show_all(coll):
    for data in coll.find():
        print(data)

channel.update_many({'_id': ObjectId('5dd3c09468c8d54b6eb09a88')}, {'$pop': {'extends': -1}})

update_result = record.update_many(
    {
        'task_id': ObjectId('5d6f5e9768f3d9da6caa4a27'),
    }, {
        '$set': {
            'mobile': '13000000000',
        },
    })

data = {
    'api_key': '5dae947db5919d416eff7e70',
    'mobile': u'17173940318',
    'text':
    u'\u3010\u9752\u6a59\u79d1\u6280\u3011\u60a8\u7684\u9a8c\u8bc1\u7801\u662f\uff1a123456',
    'ts': 1571899459,
    'sign': 'da563a30a1944dcaa80586195e832279',
}

import requests

res = requests.post('https://www.meixinduanxin.com/hooks/sender/yunpian/reply/5d6cc9c279d6fdf37d4c9', data)
print(res.json())

import requests

data = {
    'text': '【美折】您的验证码是 #code#',
    'api_key': '5daeb6100d21bd6215da5e7d',
}

requests.post('http://localhost:8010/api/sender/template/create', json=data)

'https://www.meixinduanxin.com/hooks/sender/yunpian/reply/5d6cc9c279d6fdb10f37d4c9'


'https://www.meixinduanxin.com/hooks/sender/chuanglan/reply/5d6cc9c279d6fdb10f37d4c3'

def get_unique_id():
    import string
    candidates = 'abcdef' + string.digits
    return ''.join(random.choice(candidates) for _ in range(32))

def check_shenfenzheng(shenfen_str):
    xishu = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    tmp = sum([xishu[index] * int(shenfen_str[index]) for index in range(17)])
    check = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    assert shenfen_str[17] == check[tmp % 11]


def send_yunpian_sms():
    import requests
    url = 'https://sms.yunpian.com/v2/sms/batch_send.json'
    data = {
        'apikey': '0a8761f84c1e39ecbf220eed1abdc71e',
        'mobile': ','.join(['15972096311']),
        'text': '【美折】您的验证码是：3278，如非本人请无视',
        'extend': '101',
    }
    res = requests.post(url, data, timeout=30)
    print(res.status_code)
    print(res.json())

data = {
    'text': '【美折】您的验证码是 #code#',
    'api_key': '5daeb6100d21bd6215da5e7d',
}

def batch_send():
    import time
    import hashlib
    import requests
    data = {
        'mobiles': '15972096311',
        'text': '【美折】您的验证码是2569，请在5分钟内使用'
    }
    data['ts'] = int(time.time())
    data['api_key'] = '5daeb6100d21bd6215da5e7d'
    v = '|'.join(["{}={}".format(k, v) for k, v in sorted(data.items())])
    str_to_sign = "{}_{}".format(v, 'PGG1sdgUCb')
    sign = hashlib.md5(str_to_sign.encode()).hexdigest()
    data.update(sign=sign)

    r = requests.post('http://localhost:8010/api/sender/batch_send', json=data)
    print(r.json())


def reply():
    # import requests
    # from urllib import parse
    # url = 'http://0.0.0.0:8010/hooks/sender/yunpian/reply/5dd3c09468c8d54b6eb09a8a'
    # yunpian_replys = {
    #     "id": "5de860c8da2cac78dc2e0339",
    #     "mobile": "18656053729",
    #     "text": "TD",
    #     "reply_time": "2019-12-05+09:43:36",
    #     "extend": "001",
    #     "base_extend": "552140",
    #     "_sign": "082538102e452ec2ffd7e21006514979",
    # }
    # r = requests.post(url, {'sms_reply': parse.quote(str(yunpian_replys).replace('\'', '\"'))})
    # print(r)
    chuanglan_replys = {
        "receiver": "null",
        "pswd": "null",
        "moTime": "1912090957",
        "mobile": "13739167483",
        "msg": "T",
        "destcode": "10690619198402001",
        "spCode": "10690619198402",
        "notifyTime": "191209095752",
    }
    r = requests.post('http://0.0.0.0:8010/hooks/sender/chuanglan/reply/5dd3c09468c8d54b6eb09a88', chuanglan_replys)
    print(r)


class TheWrapper:
    def call(self, *args, **kwargs):
        print(args)
        print(kwargs)

    def __getattr__(self, func_name):
        def wrapper(*args, **kwargs):
            print(args)
            print(kwargs)
            self.call(*args, **kwargs)

        return wrapper
