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
