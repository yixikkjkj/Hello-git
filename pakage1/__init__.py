# encoding:utf-8
import random
import pymongo
import logging
from bson import ObjectId
from datetime import datetime, timedelta

c = pymongo.MongoClient("mongodb://localhost:27017")
db = c['sms']
coll = db['act_conversion_order_v2']

uid = 696944147
act_id = ObjectId('5cb986c67ba1f13f49cdf240')
order = {
    'buyer_nick': '毅兮爱晚秋',
    'receiver_mobile': '15972096311',
    'tid': '1234567890ab',
}
order_created = datetime.now()


def save_act_conversion(act_id, uid, order, order_created, status):
    doc = {
        'payment': 0,
        'status': 0,
    }
    doc.update({
        'act_id': act_id,
        'tid': order['tid'],
        'buyer_nick': order.get('buyer_nick', ''),
        'mobile': order.get('receiver_mobile', 0),
        'payment': order.get('payment', 0),
        'created_t': order_created,
        'uid': uid,
        'status': status
    })
    coll.insert_one(doc)
    return doc


if __name__ == "__main__":
    save_act_conversion(act_id, uid, order, order_created, 0)
