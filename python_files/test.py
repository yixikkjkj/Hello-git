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

from datetime import datetime
from bson import ObjectId

first = {'_id': ObjectId('5f900bbe76dac28b83e91f2b'), 'stat': 'plan_data', 't': datetime(2020, 10, 20, 0, 0), 'data': {'plan_uids': [988605952, 193541, 626663430, 693343753, 642878476, 278305298, 637138451, 667293209, 371724315, 685123102, 575866910, 814887971, 717350, 172960806, 471301169, 781908017, 1218101, 517314615, 216567863, 547819071, 135578690, 187787845, 782383174, 941743180, 489537617, 554906197, 715701338, 697731675, 953275489, 968144483, 305776757, 720464003, 842419846, 320443527, 204174989, 721004179, 305359508, 182703252, 845041819, 556992156, 1416861, 856681638, 675570356, 412505271, 495801, 233649340, 770148032, 985315010, 985154244, 954279634, 267080928, 506104544, 676095713, 209101539, 801763555, 129307882, 121025263, 628563703, 328325369, 979011840, 671119619, 434312967, 996035855, 181007, 634805009, 156736786, 172028196, 446631209, 747260208, 184479028, 142367541, 420005694, 971865921, 618080068, 870321988, 109694288, 995447121, 215482706, 117934931, 342605651, 980909910, 846814559, 420947809, 570053475, 169930086, 360717671, 838527338, 226156, 425740142, 644941181, 136321918, 719155069, 898112899, 305053064, 785201035, 545592717, 5057936, 457170324, 705491865, 574439330, 621588391, 796381113, 406404034, 260881860, 267740613, 524928459, 143670777, 297722833, 511150034, 294181332, 271787477, 141276, 989772771, 479367140, 381839334, 718497263, 842858992, 153652721, 358431737, 269964796], 'plan_user': 120, 'plan_times': [{'uid': 425740142, 'info': [1220331, 63]}, {'uid': 916582295, 'info': [49951, 1]}, {'uid': 718497263, 'info': [5972, 3]}, {'uid': 527907889, 'info': [0, 1]}, {'uid': 856681638, 'info': [70986, 4]}, {'uid': 898112899, 'info': [97162, 2]}, {'uid': 717350, 'info': [144349, 2]}, {'uid': 988605952, 'info': [70480, 1]}, {'uid': 693343753, 'info': [251964, 7]}, {'uid': 832005395, 'info': [0, 1]}, {'uid': 267080928, 'info': [26985, 1]}, {'uid': 985154244, 'info': [81534, 2]}, {'uid': 852809445, 'info': [0, 1]}, {'uid': 715701338, 'info': [335, 2]}, {'uid': 489537617, 'info': [79988, 4]}, {'uid': 142367541, 'info': [171035, 4]}, {'uid': 671119619, 'info': [148402, 2]}, {'uid': 144155830, 'info': [0, 1]}, {'uid': 573662515, 'info': [0, 1]}, {'uid': 888973407, 'info': [0, 3]}, {'uid': 328325369, 'info': [72020, 1]}, {'uid': 143670777, 'info': [186087, 3]}, {'uid': 2148257, 'info': [0, 2]}, {'uid': 989772771, 'info': [581739, 7]}, {'uid': 447617424, 'info': [0, 1]}, {'uid': 720464003, 'info': [70332, 2]}, {'uid': 271787477, 'info': [57743, 3]}, {'uid': 537934761, 'info': [0, 4]}, {'uid': 556715002, 'info': [11, 1]}, {'uid': 437102964, 'info': [0, 1]}, {'uid': 592253220, 'info': [0, 1]}, {'uid': 511150034, 'info': [68677, 1]}, {'uid': 156736786, 'info': [65036, 1]}, {'uid': 297722833, 'info': [22682, 3]}, {'uid': 358431737, 'info': [22615, 2]}, {'uid': 153652721, 'info': [35457, 2]}, {'uid': 782383174, 'info': [14470, 2]}, {'uid': 371724315, 'info': [76084, 1]}, {'uid': 610871937, 'info': [51, 1]}, {'uid': 743706326, 'info': [0, 1]}, {'uid': 507649134, 'info': [0, 1]}, {'uid': 747626006, 'info': [0, 1]}, {'uid': 455327361, 'info': [0, 1]}, {'uid': 1416861, 'info': [24182, 3]}, {'uid': 226156, 'info': [80773, 2]}, {'uid': 109694288, 'info': [146472, 3]}, {'uid': 697731675, 'info': [25974, 6]}, {'uid': 390367364, 'info': [0, 1]}, {'uid': 922579043, 'info': [0, 1]}, {'uid': 796381113, 'info': [33080, 3]}, {'uid': 187787845, 'info': [19674, 5]}, {'uid': 278305298, 'info': [14541, 3]}, {'uid': 618080068, 'info': [82443, 1]}, {'uid': 968144483, 'info': [82097, 4]}, {'uid': 874286241, 'info': [0, 1]}, {'uid': 675570356, 'info': [33469, 2]}, {'uid': 193541, 'info': [56477, 2]}, {'uid': 462023210, 'info': [0, 1]}, {'uid': 969752236, 'info': [6231, 1]}, {'uid': 378850799, 'info': [366, 1]}, {'uid': 214228626, 'info': [0, 3]}, {'uid': 492878144, 'info': [0, 1]}, {'uid': 673957747, 'info': [15, 1]}, {'uid': 694954204, 'info': [44, 3]}, {'uid': 172960806, 'info': [52461, 1]}, {'uid': 621588391, 'info': [30705, 1]}, {'uid': 934300778, 'info': [0, 1]}, {'uid': 954279634, 'info': [27472, 1]}, {'uid': 153417515, 'info': [0, 1]}, {'uid': 796596404, 'info': [0, 2]}, {'uid': 403387771, 'info': [0, 1]}, {'uid': 420005694, 'info': [82375, 1]}, {'uid': 355877277, 'info': [0, 1]}, {'uid': 305359508, 'info': [64821, 3]}, {'uid': 635897645, 'info': [0, 1]}, {'uid': 675662159, 'info': [57, 2]}, {'uid': 941743180, 'info': [19505, 1]}, {'uid': 314626531, 'info': [38, 1]}, {'uid': 233649340, 'info': [13494, 1]}, {'uid': 770148032, 'info': [6223, 3]}, {'uid': 314072024, 'info': [316, 3]}, {'uid': 985315010, 'info': [141335, 3]}, {'uid': 916933611, 'info': [265, 1]}, {'uid': 996035855, 'info': [26039, 1]}, {'uid': 574439330, 'info': [14429, 2]}, {'uid': 842858992, 'info': [27242, 2]}, {'uid': 685123102, 'info': [13629, 1]}, {'uid': 495801, 'info': [12667, 3]}, {'uid': 471301169, 'info': [10012, 2]}, {'uid': 53309, 'info': [42, 1]}, {'uid': 305053064, 'info': [25916, 2]}, {'uid': 5057936, 'info': [5763, 1]}, {'uid': 360551073, 'info': [0, 1]}, {'uid': 193985649, 'info': [119, 2]}, {'uid': 357913434, 'info': [0, 1]}, {'uid': 418661552, 'info': [0, 1]}, {'uid': 506104544, 'info': [160693, 2]}, {'uid': 169930086, 'info': [143654, 3]}, {'uid': 994608996, 'info': [177, 1]}, {'uid': 488556693, 'info': [276, 2]}, {'uid': 738573424, 'info': [260, 3]}, {'uid': 517314615, 'info': [18912, 1]}, {'uid': 305776757, 'info': [18039, 1]}, {'uid': 979011840, 'info': [38429, 2]}, {'uid': 451555249, 'info': [0, 2]}, {'uid': 524928459, 'info': [80660, 2]}, {'uid': 966504954, 'info': [0, 1]}, {'uid': 215482706, 'info': [4172, 2]}, {'uid': 896277368, 'info': [0, 1]}, {'uid': 842419846, 'info': [158253, 2]}, {'uid': 878472397, 'info': [0, 2]}, {'uid': 136321918, 'info': [65671, 1]}, {'uid': 870321988, 'info': [267558, 4]}, {'uid': 974647458, 'info': [75, 2]}, {'uid': 814887971, 'info': [34903, 1]}, {'uid': 575866910, 'info': [26991, 1]}, {'uid': 269964796, 'info': [23373, 1]}, {'uid': 105274512, 'info': [0, 2]}, {'uid': 871759052, 'info': [0, 1]}, {'uid': 204174989, 'info': [23697, 2]}, {'uid': 426869161, 'info': [75, 1]}, {'uid': 721004179, 'info': [27659, 2]}, {'uid': 644941181, 'info': [611, 1]}, {'uid': 406404034, 'info': [74422, 3]}, {'uid': 642878476, 'info': [81136, 2]}, {'uid': 764105159, 'info': [0, 1]}, {'uid': 513624222, 'info': [215, 1]}, {'uid': 846374210, 'info': [65, 2]}, {'uid': 667293209, 'info': [71310, 2]}, {'uid': 676095713, 'info': [61407, 1]}, {'uid': 420947809, 'info': [27205, 1]}, {'uid': 110609858, 'info': [0, 1]}, {'uid': 637138451, 'info': [24074, 1]}, {'uid': 942777999, 'info': [136, 2]}, {'uid': 1144672, 'info': [87, 1]}, {'uid': 842426009, 'info': [0, 1]}, {'uid': 479367140, 'info': [98137, 2]}, {'uid': 816711906, 'info': [0, 1]}, {'uid': 932957682, 'info': [4611, 1]}, {'uid': 547819071, 'info': [576, 1]}, {'uid': 434312967, 'info': [157867, 4]}, {'uid': 267740613, 'info': [233163, 6]}, {'uid': 141276, 'info': [77048, 1]}, {'uid': 209101539, 'info': [76993, 1]}, {'uid': 239556011, 'info': [0, 3]}, {'uid': 320443527, 'info': [135052, 2]}, {'uid': 785201035, 'info': [27305, 3]}, {'uid': 305149251, 'info': [864, 1]}, {'uid': 884346966, 'info': [141, 2]}, {'uid': 738594991, 'info': [792, 1]}, {'uid': 679825462, 'info': [268, 1]}, {'uid': 556992156, 'info': [4607, 1]}, {'uid': 747260208, 'info': [3947, 1]}, {'uid': 181007, 'info': [3101, 1]}, {'uid': 260881860, 'info': [71124, 2]}, {'uid': 121025263, 'info': [61897, 1]}, {'uid': 733715940, 'info': [0, 1]}, {'uid': 117934931, 'info': [38645, 1]}, {'uid': 320527704, 'info': [0, 1]}, {'uid': 570053475, 'info': [17958, 1]}, {'uid': 554906197, 'info': [148166, 3]}, {'uid': 412505271, 'info': [2741, 2]}, {'uid': 343997115, 'info': [516, 2]}, {'uid': 953275489, 'info': [8459, 1]}, {'uid': 975104688, 'info': [82, 2]}, {'uid': 846814559, 'info': [4276, 1]}, {'uid': 440589546, 'info': [0, 1]}, {'uid': 293882493, 'info': [14, 1]}, {'uid': 216567863, 'info': [83059, 3]}, {'uid': 634805009, 'info': [82195, 1]}, {'uid': 360717671, 'info': [153145, 3]}, {'uid': 980909910, 'info': [72154, 1]}, {'uid': 294181332, 'info': [54998, 1]}, {'uid': 342605651, 'info': [27537, 1]}, {'uid': 545592717, 'info': [40520, 3]}, {'uid': 457170324, 'info': [16307, 1]}, {'uid': 626663430, 'info': [14249, 1]}, {'uid': 380033656, 'info': [0, 1]}, {'uid': 446631209, 'info': [9592, 1]}, {'uid': 706836891, 'info': [0, 1]}, {'uid': 705491865, 'info': [5099, 1]}, {'uid': 719155069, 'info': [167, 2]}, {'uid': 720912114, 'info': [268, 1]}, {'uid': 801763555, 'info': [159654, 3]}, {'uid': 184479028, 'info': [71808, 1]}, {'uid': 949042313, 'info': [66, 1]}, {'uid': 831940237, 'info': [127, 2]}, {'uid': 971865921, 'info': [251219, 6]}, {'uid': 628563703, 'info': [35698, 1]}, {'uid': 1218101, 'info': [66721, 2]}, {'uid': 781908017, 'info': [25645, 2]}, {'uid': 838527338, 'info': [15215, 2]}, {'uid': 995447121, 'info': [15084, 3]}, {'uid': 135578690, 'info': [13089, 1]}, {'uid': 537593456, 'info': [387, 3]}, {'uid': 845041819, 'info': [8403, 1]}, {'uid': 381839334, 'info': [82236, 1]}, {'uid': 172028196, 'info': [73630, 1]}, {'uid': 129307882, 'info': [143968, 2]}, {'uid': 182703252, 'info': [67638, 1]}]}}
second = {'_id': ObjectId('5f90abdc76dac28b83d0b162'), 'stat': 'plan_data', 't': datetime(2020, 10, 21, 0, 0), 'data': {'plan_uids': [988605952, 424452, 193541, 626663430, 494519815, 693343753, 642878476, 278305298, 637138451, 336047635, 667293209, 371724315, 685123102, 575866910, 814887971, 717350, 172960806, 781908017, 1218101, 517314615, 216567863, 547819071, 135578690, 187787845, 782383174, 941743180, 809815036, 648685646, 489537617, 715701338, 697731675, 953275489, 968144483, 746341483, 361267312, 305776757, 842419846, 320443527, 125006985, 204174989, 262518417, 721004179, 305359508, 182703252, 845041819, 556992156, 1416861, 856681638, 683071145, 675570356, 412505271, 495801, 233649340, 770148032, 985315010, 985154244, 954279634, 267080928, 506104544, 676095713, 209101539, 801763555, 129307882, 440589546, 121025263, 628563703, 328325369, 979011840, 671119619, 434312967, 996035855, 181007, 634805009, 156736786, 721788690, 172028196, 446631209, 458730283, 747260208, 882259760, 184479028, 142367541, 420005694, 971865921, 329641283, 618080068, 870321988, 109694288, 995447121, 215482706, 117934931, 342605651, 980909910, 846814559, 420947809, 570053475, 169930086, 360717671, 838527338, 226156, 425740142, 343354745, 694681979, 644941181, 136321918, 719155069, 898112899, 305053064, 785201035, 545592717, 5057936, 457170324, 705491865, 574439330, 621588391, 796381113, 466982330, 177660353, 406404034, 260881860, 267740613, 524928459, 297722833, 511150034, 294181332, 271787477, 708408789, 192523224, 141276, 479367140, 381839334, 718497263, 842858992, 153652721, 358431737, 269964796], 'plan_user': 136, 'plan_times': [{'uid': 425740142, 'info': [3595589, 63]}, {'uid': 916582295, 'info': [57993, 1]}, {'uid': 718497263, 'info': [171914, 3]}, {'uid': 361267312, 'info': [219135, 3]}, {'uid': 527907889, 'info': [60431, 1]}, {'uid': 856681638, 'info': [288741, 4]}, {'uid': 898112899, 'info': [114342, 2]}, {'uid': 717350, 'info': [75129, 2]}, {'uid': 988605952, 'info': [35870, 1]}, {'uid': 693343753, 'info': [424514, 7]}, {'uid': 832005395, 'info': [68376, 1]}, {'uid': 267080928, 'info': [78775, 1]}, {'uid': 985154244, 'info': [84416, 2]}, {'uid': 852809445, 'info': [35629, 1]}, {'uid': 715701338, 'info': [52125, 2]}, {'uid': 489537617, 'info': [235358, 4]}, {'uid': 142367541, 'info': [153186, 4]}, {'uid': 671119619, 'info': [79182, 2]}, {'uid': 144155830, 'info': [64522, 1]}, {'uid': 573662515, 'info': [60756, 1]}, {'uid': 888973407, 'info': [85793, 3]}, {'uid': 328325369, 'info': [37409, 1]}, {'uid': 271787477, 'info': [213113, 3]}, {'uid': 537934761, 'info': [0, 4]}, {'uid': 556715002, 'info': [11, 1]}, {'uid': 437102964, 'info': [83071, 1]}, {'uid': 592253220, 'info': [83739, 1]}, {'uid': 511150034, 'info': [34067, 1]}, {'uid': 156736786, 'info': [30426, 1]}, {'uid': 297722833, 'info': [218817, 3]}, {'uid': 358431737, 'info': [126195, 2]}, {'uid': 153652721, 'info': [139037, 2]}, {'uid': 782383174, 'info': [118049, 2]}, {'uid': 371724315, 'info': [41474, 1]}, {'uid': 610871937, 'info': [77208, 1]}, {'uid': 743706326, 'info': [73659, 1]}, {'uid': 507649134, 'info': [0, 1]}, {'uid': 747626006, 'info': [62272, 1]}, {'uid': 455327361, 'info': [59548, 1]}, {'uid': 1416861, 'info': [181753, 3]}, {'uid': 226156, 'info': [89871, 2]}, {'uid': 109694288, 'info': [109988, 3]}, {'uid': 697731675, 'info': [397211, 6]}, {'uid': 390367364, 'info': [74576, 1]}, {'uid': 922579043, 'info': [70137, 1]}, {'uid': 796381113, 'info': [201682, 3]}, {'uid': 187787845, 'info': [309437, 5]}, {'uid': 278305298, 'info': [174486, 3]}, {'uid': 618080068, 'info': [47833, 1]}, {'uid': 968144483, 'info': [244128, 4]}, {'uid': 874286241, 'info': [36717, 1]}, {'uid': 675570356, 'info': [168879, 2]}, {'uid': 193541, 'info': [160057, 2]}, {'uid': 462023210, 'info': [77237, 1]}, {'uid': 969752236, 'info': [6231, 1]}, {'uid': 378850799, 'info': [366, 1]}, {'uid': 214228626, 'info': [226594, 3]}, {'uid': 492878144, 'info': [56157, 1]}, {'uid': 673957747, 'info': [49038, 1]}, {'uid': 694954204, 'info': [115722, 3]}, {'uid': 172960806, 'info': [17851, 1]}, {'uid': 621588391, 'info': [82495, 1]}, {'uid': 934300778, 'info': [77675, 1]}, {'uid': 954279634, 'info': [79262, 1]}, {'uid': 153417515, 'info': [57480, 1]}, {'uid': 796596404, 'info': [89584, 2]}, {'uid': 403387771, 'info': [49526, 1]}, {'uid': 420005694, 'info': [47765, 1]}, {'uid': 355877277, 'info': [34840, 1]}, {'uid': 305359508, 'info': [101048, 3]}, {'uid': 635897645, 'info': [83420, 1]}, {'uid': 675662159, 'info': [155807, 2]}, {'uid': 941743180, 'info': [71295, 1]}, {'uid': 314626531, 'info': [67514, 1]}, {'uid': 233649340, 'info': [65284, 1]}, {'uid': 770148032, 'info': [113495, 3]}, {'uid': 314072024, 'info': [130097, 3]}, {'uid': 985315010, 'info': [100470, 3]}, {'uid': 916933611, 'info': [83825, 1]}, {'uid': 996035855, 'info': [77829, 1]}, {'uid': 574439330, 'info': [129864, 2]}, {'uid': 842858992, 'info': [130822, 2]}, {'uid': 685123102, 'info': [65419, 1]}, {'uid': 495801, 'info': [189169, 3]}, {'uid': 471301169, 'info': [118194, 2]}, {'uid': 53309, 'info': [42, 1]}, {'uid': 305053064, 'info': [133633, 2]}, {'uid': 5057936, 'info': [57553, 1]}, {'uid': 360551073, 'info': [23739, 1]}, {'uid': 193985649, 'info': [88117, 2]}, {'uid': 357913434, 'info': [43089, 1]}, {'uid': 418661552, 'info': [40866, 1]}, {'uid': 506104544, 'info': [91473, 2]}, {'uid': 169930086, 'info': [109136, 3]}, {'uid': 994608996, 'info': [33865, 1]}, {'uid': 488556693, 'info': [155112, 2]}, {'uid': 738573424, 'info': [187796, 3]}, {'uid': 517314615, 'info': [70702, 1]}, {'uid': 305776757, 'info': [69829, 1]}, {'uid': 979011840, 'info': [142009, 2]}, {'uid': 451555249, 'info': [115477, 2]}, {'uid': 524928459, 'info': [106031, 2]}, {'uid': 966504954, 'info': [55678, 1]}, {'uid': 215482706, 'info': [108413, 2]}, {'uid': 896277368, 'info': [46282, 1]}, {'uid': 842419846, 'info': [89033, 2]}, {'uid': 878472397, 'info': [83419, 2]}, {'uid': 136321918, 'info': [31061, 1]}, {'uid': 870321988, 'info': [126484, 4]}, {'uid': 974647458, 'info': [75, 2]}, {'uid': 814887971, 'info': [293, 1]}, {'uid': 575866910, 'info': [78781, 1]}, {'uid': 269964796, 'info': [75163, 1]}, {'uid': 105274512, 'info': [101516, 2]}, {'uid': 871759052, 'info': [70831, 1]}, {'uid': 204174989, 'info': [124595, 2]}, {'uid': 426869161, 'info': [39939, 1]}, {'uid': 721004179, 'info': [131845, 2]}, {'uid': 644941181, 'info': [52401, 1]}, {'uid': 406404034, 'info': [129796, 3]}, {'uid': 642878476, 'info': [90805, 2]}, {'uid': 764105159, 'info': [43887, 1]}, {'uid': 513624222, 'info': [42219, 1]}, {'uid': 846374210, 'info': [79808, 2]}, {'uid': 667293209, 'info': [70860, 2]}, {'uid': 676095713, 'info': [26797, 1]}, {'uid': 420947809, 'info': [78995, 1]}, {'uid': 110609858, 'info': [74158, 1]}, {'uid': 637138451, 'info': [75864, 1]}, {'uid': 942777999, 'info': [45110, 2]}, {'uid': 1144672, 'info': [87, 1]}, {'uid': 842426009, 'info': [65594, 1]}, {'uid': 479367140, 'info': [101832, 2]}, {'uid': 816711906, 'info': [58440, 1]}, {'uid': 932957682, 'info': [51907, 1]}, {'uid': 547819071, 'info': [52366, 1]}, {'uid': 434312967, 'info': [172334, 4]}, {'uid': 267740613, 'info': [249554, 6]}, {'uid': 141276, 'info': [42438, 1]}, {'uid': 209101539, 'info': [42383, 1]}, {'uid': 239556011, 'info': [48070, 3]}, {'uid': 320443527, 'info': [65832, 2]}, {'uid': 785201035, 'info': [217689, 3]}, {'uid': 305149251, 'info': [68934, 1]}, {'uid': 884346966, 'info': [135310, 2]}, {'uid': 738594991, 'info': [64187, 1]}, {'uid': 679825462, 'info': [63553, 1]}, {'uid': 556992156, 'info': [56397, 1]}, {'uid': 747260208, 'info': [55737, 1]}, {'uid': 181007, 'info': [54891, 1]}, {'uid': 260881860, 'info': [70350, 2]}, {'uid': 121025263, 'info': [27287, 1]}, {'uid': 733715940, 'info': [85066, 1]}, {'uid': 117934931, 'info': [4035, 1]}, {'uid': 320527704, 'info': [74661, 1]}, {'uid': 570053475, 'info': [69748, 1]}, {'uid': 554906197, 'info': [184285, 3]}, {'uid': 412505271, 'info': [114969, 2]}, {'uid': 343997115, 'info': [59793, 2]}, {'uid': 953275489, 'info': [60249, 1]}, {'uid': 975104688, 'info': [112385, 2]}, {'uid': 846814559, 'info': [56066, 1]}, {'uid': 440589546, 'info': [118527, 2]}, {'uid': 293882493, 'info': [14, 1]}, {'uid': 216567863, 'info': [139018, 3]}, {'uid': 634805009, 'info': [47585, 1]}, {'uid': 360717671, 'info': [194271, 4]}, {'uid': 980909910, 'info': [37544, 1]}, {'uid': 294181332, 'info': [20388, 1]}, {'uid': 342605651, 'info': [79327, 1]}, {'uid': 545592717, 'info': [213455, 3]}, {'uid': 457170324, 'info': [68097, 1]}, {'uid': 626663430, 'info': [66039, 1]}, {'uid': 380033656, 'info': [60495, 1]}, {'uid': 446631209, 'info': [61382, 1]}, {'uid': 706836891, 'info': [58554, 1]}, {'uid': 705491865, 'info': [56889, 1]}, {'uid': 719155069, 'info': [101360, 2]}, {'uid': 720912114, 'info': [43549, 1]}, {'uid': 801763555, 'info': [133937, 3]}, {'uid': 184479028, 'info': [37198, 1]}, {'uid': 949042313, 'info': [30179, 1]}, {'uid': 831940237, 'info': [59644, 2]}, {'uid': 971865921, 'info': [389159, 6]}, {'uid': 628563703, 'info': [1088, 1]}, {'uid': 1218101, 'info': [170301, 2]}, {'uid': 781908017, 'info': [77435, 2]}, {'uid': 838527338, 'info': [131542, 2]}, {'uid': 995447121, 'info': [193249, 3]}, {'uid': 135578690, 'info': [64879, 1]}, {'uid': 537593456, 'info': [57815, 3]}, {'uid': 845041819, 'info': [60193, 1]}, {'uid': 381839334, 'info': [47626, 1]}, {'uid': 172028196, 'info': [39020, 1]}, {'uid': 129307882, 'info': [74748, 2]}, {'uid': 182703252, 'info': [33028, 1]}, {'uid': 882259760, 'info': [2451, 1]}, {'uid': 648685646, 'info': [76313, 1]}, {'uid': 177660353, 'info': [145297, 3]}, {'uid': 494519815, 'info': [71512, 1]}, {'uid': 125006985, 'info': [70674, 1]}, {'uid': 694681979, 'info': [67216, 1]}, {'uid': 343354745, 'info': [64476, 1]}, {'uid': 329641283, 'info': [63373, 1]}, {'uid': 845187427, 'info': [60107, 1]}, {'uid': 424452, 'info': [61649, 1]}, {'uid': 485310807, 'info': [58414, 1]}, {'uid': 708408789, 'info': [57889, 1]}, {'uid': 458730283, 'info': [114652, 2]}, {'uid': 466982330, 'info': [57504, 1]}, {'uid': 683071145, 'info': [56163, 1]}, {'uid': 262518417, 'info': [45952, 1]}, {'uid': 192523224, 'info': [45310, 1]}, {'uid': 336047635, 'info': [175933, 4]}, {'uid': 721788690, 'info': [123240, 3]}, {'uid': 139402679, 'info': [72568, 2]}, {'uid': 809815036, 'info': [37374, 1]}, {'uid': 746341483, 'info': [108677, 3]}]}}
first.pop('_id')
second.pop('_id')

def plan_data_compare():
    first_info = {data['uid']: data['info'] for data in first['data']['plan_times']}
    second_info = {data['uid']: data['info'] for data in second['data']['plan_times']}
    rlt = {}
    total,count = 0, 0
    user = 0
    for uid, data2 in second_info.items():
        if uid == 425740142:
            continue
        if int(data2[0] / data2[1]) > 52236:
            user += 1
        total += data2[0]
        count += data2[1]

    print(total/count)
    print(user)

    #     if uid not in first_info:
    #         rlt[uid] = data2
    #         continue
    #     data1 = first_info[uid]
    #     rlt[uid] = [data2[0] - data1[0], data2[1] - data1[1]]
    # for uid, data1 in first_info.items():
    #     if uid not in rlt:
    #         rlt[uid] = [-data1[0], -data1[1]]
    # rlt_items = list(rlt.items())
    # rlt_items.sort(key=lambda x: x[1][0], reverse=True)
    # for data in rlt_items:
    #     print(data)


class TestA:
    def __new__(cls, *args, **kwargs):
        print(args, kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print(args, kwargs)


args = [1,'a', 'z']
kwargs = {
    'a': 1,
    'b': 'z',
}

test_a = TestA(*args, **kwargs)

import pydantic
from datetime import datetime

class DateTimeRange(pydantic.BaseModel):
    start_t: datetime = None
    end_t: datetime = None

    @pydantic.root_validator
    def validator_datetime(cls, values):
        st, et = values.get('start_t'), values.get('end_t')
        if not st or not et:
            raise ValueError('start_t and end_t should be supplied.')
        if st > et:
            raise ValueError('start_t should less than end_t')
        return values

    def __new__(cls, *args, **kwargs):
        print(args, kwargs)
        start_t_default_func = args[-1]
        end_t_default_func = args[-2]
        args = args[2:]
        return super().__new__(cls, *args, **kwargs)
