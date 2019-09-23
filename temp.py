import blinker
from bson import ObjectId
from datetime import datetime

signal = blinker.Namespace()

test_signal = signal.signal('test_singal_one')


@test_signal.connect
def once_signal_sent(param_one, param_two, *args, **kwargs):
    print(param_one)
    print(param_two)
    print(args)
    print(kwargs)


if __name__ == "__main__":
    test_signal.send({
        'param_one': 1,
        'param_two': 'two',
        'other': 'nonononono',
    })

{
    '_id':
    ObjectId('5ceb967f4f9fc9321a88ab59'),
    'created_t':
    datetime(2019, 5, 27, 15, 49, 19, 646000),
    'balance':
    97550,
    'frozen':
    1295,
    'used':
    1155,
    'user_name':
    'taovip',
    'password_hash':
    'pbkdf2:sha256:150000$Ziw7ZC8L$e2fda666129c5abd8e512eea8136ef407beb0699df92ab640bfbae1de78eebbe',
    'last_login':
    datetime(2019, 5, 27, 15, 49, 19, 646000)
}
{
    'name': '活动 910035',
    'text': '【Hand Of God】test for回T退订',
    'schedule_t': datetime(2019, 8, 6, 15, 15),
    'plan_type': 2,
    'cache_key': 'mobile_upload_5ceb967f4f9fc9321a88ab59_1565075436649_226',
    'user_id': ObjectId('5ceb967f4f9fc9321a88ab59')
}


@cli.command()
def duplicate_marker_test():
    from datetime import datetime
    from app.models.constants import ACT
    from app.ext.cache import cache_service
    from app.utils.cache_list import DictListCache
    from app.base.marker import DuplicateCacheMarker
    from app.base.predictor.order.constants import ORDER_FILTERS_KEYS, START_KEY, END_KEY
    mobiles = []
    start_mobile = 13000000000
    count = 100002

    for mobile_num in range(start_mobile, start_mobile + count):
        tmp = {
            ACT.DEFAULT_DATA_KEY: str(start_mobile),
            'buyer_nick': 'w2589031968',
            'tid': '262192353564100243'
        }
        mobiles.append(tmp)

    with DictListCache(cache_service, 'duplicated_marker_test', 'w',
                       ACT.DEFAULT_DATA_KEY) as cache:
        cache.extend(mobiles)
        click.echo('>> duplicate marker starting...')
        with DuplicateCacheMarker(cache) as marker:
            marker.mark(exact=True)
    click.echo('>> duplicate marker done!')


@cli.command()
def duplicated_marker_test():
    from app.tasks.basic_act import duplicate_marker_test
    duplicate_marker_test.delay()


@cli.command()
def json_loads_order_test():
    import json
    import time
    from datetime import datetime, date
    from app.utils.mongo_json_encoder import MongoJsonEncoder
    from app.utils.cache_list import DictListCache
    from app.ext.cache import cache_service
    from app.models.constants import ACT
    from app.base.marker import DuplicateCacheMarker
    from app.base.predictor.order.common import filter_order_useless_keys
    example = {
        'trade_order_id':
        1,
        'tid':
        283392932288651697,
        'seller_id':
        696944147,
        'pay_date':
        date(2019, 6, 13),
        'pay_time':
        datetime(2019, 6, 13, 9, 32, 47),
        'created_date':
        date(2019, 6, 13),
        'created':
        datetime(2019, 6, 13, 9, 32, 40),
        'consign_time':
        '0000-00-00 00:00:00',
        'end_time':
        datetime(2019, 8, 26, 8, 59, 10),
        'modified':
        datetime(2019, 8, 26, 8, 59, 9),
        'payment':
        100,
        'post_fee':
        0,
        'seller_flag':
        0,
        'status':
        8,
        'sys_status':
        0,
        'trade_order_status':
        3,
        'buyer_uuid':
        1566787615735104279,
        'receiver_mobile':
        '$wwNJN7cOR8zs/FKXPj3EjA==$VoTd3d3hRsI6HBhMce/YfQ==$1$$',
        'buyer_nick':
        '',
        'receiver_state':
        '贵州省',
        'receiver_city':
        '遵义市',
        'receiver_district':
        '播州区',
        'create_time':
        datetime(2019, 8, 26, 10, 46, 55),
        'modify_time':
        datetime(2019, 8, 26, 10, 46, 55),
    }
    mobiles = []
    start_mobile = 13000000000
    count = 100000
    for mobile_num in range(start_mobile, start_mobile + count):
        tmp = example.copy()
        tmp['receiver_mobile'] = str(mobile_num)
        tmp['buyer_nick'] = 'buyer_%s' % mobile_num
        mobiles.append(tmp)

    with DictListCache(cache_service, 'test_order_json_load', 'w',
                       'receiver_mobile') as cache:
        mobiles = filter_order_useless_keys(mobiles)
        cache.extend(mobiles)

    with DictListCache(cache_service, 'test_order_json_load', 'r',
                       'receiver_mobile') as cache:
        for page in range(cache.total_page):
            cache.get_range(page * cache.page_size, cache.page_size)

    with DictListCache(cache_service, 'duplicated_marker_test', 'w',
                       ACT.DEFAULT_DATA_KEY) as cache:
        cache.extend(mobiles)
        with DuplicateCacheMarker(cache) as marker:
            marker.mark(exact=True)

    st = time.time()
    mobiles_json = json.dumps(mobiles, cls=MongoJsonEncoder)
    dumps_et = time.time()
    mobiles = json.loads(mobiles_json)
    loads_et = time.time()
    print('cost time is dumps [%s] loads [%s]' % (dumps_et - st,
                                                  loads_et - dumps_et))

    channel.create_channel({
        'api_key': 'ada7dbdc3738234eb6b342486e1ac6e4'
    }, 300, BASE_SENDER.PROVIDER.YUNPIAN, BASE_SENDER.MESSAGE_TYPE.MARKETING)


@cli.command()
def fix_process_notice_report():
    from datetime import datetime, timedelta
    from app.actions.act import process_notice_detail_msg
    now = datetime.now()
    end = datetime(now.year, now.month, now.day)
    start = end - timedelta(days=1)
    return process_notice_detail_msg(start, end)


@cli.command()
def build_notice_test_data():
    from datetime import datetime, timedelta
    from app.models.constants import SUB_ACCOUNT, DETAIL_STATUS
    from app.models import db
    sent_t = datetime.now() - timedelta(days=1)

    details = []
    for x in range(90):
        detail = db.Detail()
        detail.update({
            'sub_account': SUB_ACCOUNT.TONGZHI,
            'status': DETAIL_STATUS.DELIVERED,
            'uid': 696944148,
            'sent_t': sent_t,
        })
        details.append(detail)
    for x in range(100):
        detail = db.Detail()
        detail.update({
            'sub_account': SUB_ACCOUNT.TONGZHI,
            'status': DETAIL_STATUS.SENDING,
            'uid': 696944149,
            'sent_t': sent_t,
        })
        details.append(detail)
    rlt = db.Detail.insert_many(details)
    print(rlt)


import sys


def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 00.
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj,
                                                     (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size


data_list = []
for mobile in range(13000000000, 13000110000):
    tmp = {
        'receiver_mobile': str(mobile),
        'buyer_nick': 'w2589031968',
        'tid': '262192353564100243',
    }
    data_list.append(tmp)

get_size(data_list)
