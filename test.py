# encoding:utf-8
import random
import pymongo
from datetime import datetime, timedelta


c = pymongo.MongoClient("mongodb://localhost:27017")
db = c['sms']

coll = db['detail_v2']


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
    coll.remove({})
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
        for i in xrange(info[2]):
            tmp = data.copy()
            tmp['sent_t'] = start+timedelta(seconds=(i+1)*60)
            tmp['status'] = failstatus[random.randint(0, 2)]
            coll.insert(tmp)
        for i in xrange(info[1]-info[2]):
            tmp = data.copy()
            tmp['sent_t'] = start+timedelta(seconds=(i+1)*60)
            coll.insert(tmp)


insert_some_data()


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
    coll.insert(data)

# insert_one_data()


class IterA(object):
    def __iter__(self):
        try:
            yield 1
            raise IOError
        except Exception as e:
            print "its an error"
            return


class IterB(object):
    def __init__(self, lmt):
        self.lmt = lmt

    def __iter__(self):
        is_lmt = False
        it = IterA()
        for i in it.__iter__():
            is_lmt = True
            yield i
        if is_lmt:
            return
        for i in xrange(100):
            yield i


class WithA(object):

    def __enter__(self):
        print "witha enter"
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "witha exit"

    def dosth(self):
        self.num = 123
        print 'witha num is', self.num


def UseWithA():
    with WithA() as wa:
        wa.dosth()
        return wa.num


# CELERYBEAT_SCHEDULE = Config.CELERYBEAT_SCHEDULE.copy()
# CELERYBEAT_SCHEDULE.update(
#     {
#         'do_notice_detail_msg': {
#             'task': 'app.tasks.act.daily_notice_detail_msg',
#             'schedule': crontab(minute="*")
#         },
#     }
# )


def writeabigfile():
    with open("/Users/wangyijun/Documents/大联系号码3.txt", "a+") as f:
        for i in xrange(450000):
            f.writelines("%s\n" % (15972096311+i))


# 300+1200+2200+100=3800k
