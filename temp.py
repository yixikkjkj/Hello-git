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


@cli.command()
def build_some_details():
    from bson import ObjectId
    from datetime import datetime, timedelta
    from app.models.constants import DETAIL_STATUS, SUB_ACCOUNT
    from app.models import db
    uid = 696944147
    act_id = ObjectId()
    text = 'recent_sent_test_text'
    sent_t = datetime.now()
    sub_account = SUB_ACCOUNT.YINGXIAO
    success_status = DETAIL_STATUS.DELIVERED
    fail_status = DETAIL_STATUS.FAILED  # DELIVERED
    count = 1

    start_t = datetime.now() - timedelta(days=21)
    start_mobile_num = 13000000000
    success_mobile_count = 10000
    fail_mobile_count = 10000
    for day in xrange(20):
        details = []
        sent_t = start_t + timedelta(days=day)
        for mobile_index in xrange(success_mobile_count):
            detail = db.Detail()
            detail.update({
                'uid': uid,
                'act_id': act_id,
                'mobile': str(start_mobile_num + mobile_index),
                'text': text,
                'sent_t': sent_t,
                'status': success_status,
                'sub_account': sub_account,
                'count': count,
            })
            details.append(detail)

        for mobile_index in xrange(success_mobile_count,
                                   success_mobile_count + fail_mobile_count):
            detail = db.Detail()
            detail.update({
                'uid': uid,
                'act_id': act_id,
                'mobile': str(start_mobile_num + mobile_index),
                'text': text,
                'sent_t': sent_t,
                'status': fail_status,
                'sub_account': sub_account,
                'count': count,
            })
            details.append(detail)

        db.Detail.insert_many(details)


@cli.command()
def recent_marker_test():
    from datetime import datetime
    from app.models.constants import ACT
    from app.ext.cache import cache_service
    from app.utils.cache_list import DictListCache
    from app.base.marker import RecentFailedMarker
    mobiles = []
    start_mobile = 13000000000
    count = 100002

    for mobile_num in range(start_mobile, start_mobile + count):
        tmp = {
            ACT.DEFAULT_DATA_KEY: str(mobile_num),
            'buyer_nick': 'w2589031968',
            'tid': '262192353564100243'
        }
        mobiles.append(tmp)

    with DictListCache(cache_service, 'duplicated_marker_test', 'w',
                       ACT.DEFAULT_DATA_KEY) as cache:
        cache.extend(mobiles)
        click.echo('>> duplicate marker starting...')
        with RecentFailedMarker(696944147, 7) as marker:
            marker.mark_seq(cache, data_key='receiver_mobile', exact=True)
    click.echo('>> duplicate marker done!')


@cli.command()
def fix_parse_upload_file():
    from app.actions.oss import download_oss_file
    file_key = 'Sms_2200696743476_1569400847780.txt'
    download_oss_file(file_key)


def teeeee(*args):
    print(dict(*args))

def example_funccc(name, wid):
    teeeee(name)\


@cli.command()
@click.option('--fix', is_flag=True, default=False)
def fix_user_data(fix):
    from datetime import datetime
    vas_order_list = list(db.VasOrder.find())
    uid2expire = {}
    for vas_order in vas_order_list:
        expire = uid2expire.get(vas_order['mall_id'])
        order_expire = datetime.fromtimestamp(vas_order['pay_ts'] / 1000 + vas_order['time_length'])
        if not expire or expire <= order_expire:
            uid2expire[vas_order['mall_id']] = order_expire
    click.echo(uid2expire)


@cli.command()
def get_acc():
    import re
    acc_re = re.compile('.*access_token\": \"([a-z0-9]+)')
    accs = set()
    with open('./log/app_remote/pdd.log-20200421') as log_file:
        for line in log_file.readlines():
            if "pdd.ad.history.report.get" in line:
                rlt = acc_re.match(line)
                if not rlt:
                    click.echo(line)
                    continue
                accs.add(rlt.groups()[0])
    click.echo(accs)


@cli.command()
def fix_createt():
    import re
    from datetime import datetime

    acc_re = re.compile(r'[a-z\-\:\.0-9]+\[([0-9\-\,\:\s]+)\].*uid \[([0-9]+)\].*access_token \[([a-z0-9]+)\].*access_expire_at \[([0-9]+)\]')
    accs = {}
    with open('./log/app_remote/signal_user_login.log') as log_file:
        for line in log_file.readlines():
            rlt = acc_re.match(line)
            if not rlt:
                click.echo(line)
                continue
            uid, access_token, access_token_expire_ts = rlt.groups()
            accs[uid] = (access_token, access_token_expire_ts)

    click.echo(accs)



@cli.command()
def make_the_table():
    import re
    regx = re.compile('.*def (ad_api_[a-z_]+)')
    rlt = ''
    with open('app/ext/pdd_client_v2.py') as api_file:
        for line in api_file.readlines():
            match = regx.match(line)
            if match:
                rlt += '| pdd.' + match.groups()[0].replace('_', '.') + ' |  |\n'
    print(rlt)



@cli.command()
def testttt():
    from datetime import datetime
    from app.ext.pdd_client_v2 import ads_client, OrderBy, ReportQueryType
    from app.models import constants
    from pdd.pdd import PDDError

    uid = 425740142
    user = db.User.find_one({'uid': uid})
    if not user:
        click.echo("搞毛呢，没有用户" + str(uid))
        return
    access_token = user['access_token']

    # plan_id = 27087426
    # plan_name = '虎虎推广_推广123'
    start_t = datetime(2020, 5, 29)
    end_t = datetime(2020, 5, 29)
    # for i in range(6, 14):
    #     try:
    #         res = ads_client.ad_api_plan_query_list(
    #             access_token,
    #             start_t,
    #             end_t,
    #             PLAN.SCENE_TYPE.SEARCH_ADV,
    #         )
    #     except PDDError as error:
    #         click.echo('failed query %s %s' % (str(error), i))

    # plan_id = 24564102
    # max_cost = 240000
    # discounts = [
    #     {'index': 8, 'rate': 1400},
    #     {'index': 12, 'rate': 2000},
    #     {'index': 17, 'rate': 1000},
    # ]
    # plan_name = "推广男鞋_213"
    unit_id = 162514380
    # unit_name = '生日礼物abcdef'
    plan_id = 24559051
    deliver_type = 4
    reference_type = 1
    goods_id = 76163390719
    # creative_title = '手工制作精美生日礼物'
    # creative_id = 144815024
    # creative_image = 'https://t00img.yangkeduo.com/goods/images/2019-12-13/d35871d8-9787-4c10-bc80-761afeed9bc1.jpg'
    error_list = []
    # res = ads_client.ad_api_unit_creative_update_smart_creative(
    #     access_token,
    #     creative_id,
    #     '手工制作精致生日礼物'
    # )
    # for i in OrderBy.values():
    #     try:
    #         res = ads_client.plan_query_list(access_token,
    #             start_t,
    #             end_t,
    #             order_by=i,
    #         )
    #         click.echo(res)
    #     except PDDError as error:
    #         click.echo('failed query %s %s' % (str(error), i))
    #         error_list.append(i)
    # click.echo('error_list %s' % error_list)
    res = ads_client.unit_creative_query_flow_rate(
        access_token,
        unit_id,
    )
    click.echo(res)
