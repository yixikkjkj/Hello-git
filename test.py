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
task = ntb['task']

sms = c['sms']
act = sms['act_v2']


def insert_some_data():
    """
    设定一些用户发的少一些，总数10失败9
    设定一些用户发的少一些，总数10失败1
    设定一些用户发的多一些，总数1000失败990
    设定一些用户发的多一些，总数1000失败10
    """
    less_fail1 = (696944147, 10, 9)
    less_fail2 = (696944151, 10, 9)
    less_succ = (696944148, 10, 1)
    more_fail = (696944149, 1000, 990)
    more_succ = (696944150, 1000, 10)
    plan.remove({})
    start = datetime(2018, 12, 18)
    end = datetime(2018, 12, 18, 23, 50)
    failstatus = (1, 3, 0x20)
    succstatus = 2
    data = {
        'uid': 696944147,
        'act_id': 0,
        'mobile': 15972096311,
        'buyer_nick': '测试活动_taovip',
        'tid': '',
        'text': '测试短信',
        'sent_t': datetime.now(),
        'status': succstatus,
        'sender': 0,
        'count': 1,
        'sub_account': 2
    }
    for info in (less_fail1, less_fail2, less_succ, more_fail, more_succ):
        data.update({'uid': info[0]})
        for i in range(info[2]):
            tmp = data.copy()
            tmp['sent_t'] = start + timedelta(seconds=(i + 1) * 60)
            tmp['status'] = failstatus[random.randint(0, 2)]
            plan.insert(tmp)
        for i in range(info[1] - info[2]):
            tmp = data.copy()
            tmp['sent_t'] = start + timedelta(seconds=(i + 1) * 60)
            plan.insert(tmp)


# insert_some_data()


def insert_one_data():
    start = datetime(2018, 1, 1)
    end = datetime.now()
    failstatus = (1, 3, 4)
    succstatus = 2
    data = {
        'uid': 696944147,
        'act_id': 0,
        'mobile': 15972096311,
        'buyer_nick': '测试活动_taovip',
        'tid': '',
        'text': '测试短信',
        'sent_t': datetime.now(),
        'status': succstatus,
        'sender': 0,
        'count': 1,
        'sub_account': 4
    }
    data['sent_t'] = start
    if random.randint(0, 5) != 0:
        data['status'] = failstatus[random.randint(0, 3)]
    plan.insert(data)


# if we do this with redis to mongodb

import abc


class TextMeta(type):
    def __new__(cls, name, bases, cls_dict, **kwargs):
        return type.__new__(cls, name, bases, cls_dict)


class Text(metaclass=TextMeta):
    """
    TYPE:类型
    CONSTANTS:常量
    """
    TYPE = 1
    CONSTANTS = 2


class Normal:
    def __new__(cls, *args, **kwargs):
        print(cls)
        print(args)
        print(kwargs)
        return super(Normal, cls).__new__(cls)

    def __init__(self, args):
        print('in initttt')
        self.args = args
        print(self.__class__.__name__)


from collections import namedtuple

import typing


class NamedContent(typing.NamedTuple):
    name: str


if __name__ == "__main__":
    a = NamedContent()
