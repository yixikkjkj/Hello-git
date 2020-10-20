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


def analysis_user_balance_log():
    import json
    import re
    from datetime import datetime
    # [\/a-z\.\:0-9]+
    match_str = r'.*\[([0-9\-\s\:\,]+)\].*user \[([0-9]+)\] balance changed \[([0-9]+)\]->\[([0-9]+)\] \[(.*)\]->\[(.*)\]'
    complied_str = re.compile(match_str)

    uid_list = [
        8298818, 752496429, 208910974, 916582295, 527907889, 374144298,
        446670077, 285162076, 299629400, 477507666, 185972924, 413799007,
        499338949, 7580194, 823344355, 621845104, 751140020, 575725332,
        846808547, 427598183
    ]
    uid2name = {
        7580194: '雅瓷卫浴',
        8298818: '港岛妹妹大卖铺',
        185972924: '清华课外书屋',
        208910974: '冠茗珠宝',
        285162076: '小陶的百宝店',
        299629400: '减龄俏佳人时装店',
        374144298: '冀宠宠物用品官方旗舰店',
        413799007: '鹏的精品店',
        427598183: '铂丽餐具',
        446670077: '依卡妮厂家店',
        477507666: '欣蕊毛绒玩具店',
        499338949: '爱玛女鞋店',
        527907889: '状元百货管',
        575725332: '智能门锁5',
        621845104: '贝兹童装',
        751140020: '健之优品',
        752496429: 'The One男装店',
        823344355: '富七狼男装旗舰店',
        846808547: '顶柔之心',
        916582295: '恒而美数码'
    }
    dir_path = '/Users/wangyijun/ads/log/remote/user_balance/account_balance'
    for uid in uid_list:
        print('用户ID,店名,时间,旧余额,新余额')
        with open(dir_path + 'account_balance_' + str(uid)) as file_obj:
            for line in file_obj.readlines():
                match_rlt = complied_str.match(line)
                if not match_rlt:
                    print(line)
                rlt = match_rlt.groups()
                record_time = datetime.strptime(rlt[0], '%Y-%m-%d %H:%M:%S,%f')
                old_balance = int(rlt[2])
                new_balance = int(rlt[3])
                old_accounts = json.loads(rlt[4].replace('\'', '\"'))
                new_accounts = json.loads(rlt[5].replace('\'', '\"'))
                print(','.join([str(uid), uid2name[uid], record_time, old_balance, new_balance]))
        print('\n')


def count_log_api():
    import re
    request_str = r'\[([^\]]+)\]\[[A-Z]+\]\[([0-9a-z]+)\] call \[([a-z\.]+)\] with (.*)'
    resp_str = r'\[([^\]]+)\]\[[A-Z]+\]\[([0-9a-z]+)\] return \<[0-9]+\> (.*)'
    request_comp = re.compile(request_str)
    resp_comp = re.compile(resp_str)

    file_name = '/Users/wangyijun/ads/log/remote/pdd.log-20201010'
    temp_id = {}
    api_rlt = {}
    with open(file_name, 'r') as file_obj:
        for line in file_obj.readlines():
            req = request_comp.match(line)
            resp = resp_comp.match(line)
            if req:
                data = req.groups()
                req_id = data[1]
                api_str = data[2]
                req_length = len(data[3])
                temp_id[req_id] = api_str
                if api_str not in api_rlt:
                    api_rlt[api_str] = {
                        'line': 0,
                        'req_length': 0,
                        'resp_length': 0,
                    }
                api_rlt[api_str]['line'] += 1
                api_rlt[api_str]['req_length'] += req_length
            elif resp:
                data = resp.groups()
                req_id = data[1]
                resp_length = len(data[2])
                api_str = temp_id.pop(req_id, None)
                if not api_str:
                    print(data)
                    continue
                if api_str not in api_rlt:
                    api_rlt[api_str] = {
                        'line': 0,
                        'req_length': 0,
                        'resp_length': 0,
                    }
                api_rlt[api_str]['line'] += 1
                api_rlt[api_str]['resp_length'] += resp_length
            else:
                print(line)
    rlt = [(api_str, data['line'], data['req_length'], data['resp_length']) for api_str, data in api_rlt.items()]
    rlt.sort(key=lambda x: x[2], reverse=True)
    for data in rlt:
        print(data)
