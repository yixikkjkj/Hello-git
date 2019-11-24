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

sms = c['sms']
act = sms['act_v2']


def show_all(coll):
    for data in coll.find():
        print(data)


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
