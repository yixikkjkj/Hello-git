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
