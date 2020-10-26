
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


@cli.command()
def testttt():
    from datetime import datetime, timedelta

    from app.ext.pdd_client_v2 import ads_client, ReportQueryType
    from app.tasks import account as account_tasks

    uid = 961007696
    user = db.User.find_one({'uid': uid})

    # account_tasks.sync_user_plans(uid, user['access_token'])

    ads_client.report_daily_report_query(
        user['access_token'],
        datetime(2020, 6, 7), datetime(2020, 6, 8) - timedelta(seconds=1),
        ReportQueryType.Keyword, 1557590162, unit_id=79940251
    )



def analysis_nginx_logs():
    import re
    from datetime import datetime
    old_log_str = r'([0-9\.]+) - - \[([^\]]+)\] "([^\"]+)" ([0-9]+) ([0-9]+) "([^\"]+)" "([^\"]+)"'
    log_str = r'([0-9\.]+) - - \[([^\]]+)\] "([^\"]+)" ([0-9]+) ([0-9]+) ([0-9\.]+) "([^\"]+)" "([^\"]+)"'
    old_comp = re.compile(old_log_str)
    log_comp = re.compile(log_str)

    file_path = '/Users/wangyijun/ads/log/remote/nginx/access.log-20200923'
    rlt = []
    with open(file_path, 'r') as file_obj:
        for line in file_obj.readlines():
            old_match = old_comp.match(line)
            match = log_comp.match(line)
            if old_match:
                data = old_match.groups()
                rlt.append({
                    'remote_addr': data[0],
                    'time_local': datetime.strptime(data[1], '%d/%b/%Y:%H:%M:%S +%f'),
                    'request': data[2],
                    'status': data[3],
                    'bytes_sent': data[4],
                    'request_time': None,
                    'refer': data[5],
                    'user_agent': data[6],
                })
            if match:
                data = match.groups()
                rlt.append({
                    'remote_addr': data[0],
                    'time_local': datetime.strptime(data[1], '%d/%b/%Y:%H:%M:%S +%f'),
                    'request': data[2],
                    'status': data[3],
                    'bytes_sent': data[4],
                    'request_time': data[5],
                    'refer': data[6],
                    'user_agent': data[7],
                })
    return rlt


def cb_and_vendors_and_post_cb():
    import re
    logs = analysis_nginx_logs()
    cb_state_str = r'GET /cb\?code=([0-9a-z]+)&state=([^\s]+)'
    cb_str = r'GET /cb\?code=([0-9a-z]+)'
    vendors_str = r'GET /vendors'
    post_cb_str = r'POST /api/user/cb'

    cb_state_comp = re.compile(cb_state_str)
    cb_comp = re.compile(cb_str)
    vendors_comp = re.compile(vendors_str)
    post_cb_comp = re.compile(post_cb_str)

    rlt = {}

    for data in logs:
        if not data['remote_addr'] in rlt:
            rlt[data['remote_addr']] = {
                'woda_cb': 0,
                'normal_cb': 0,
                'vendors': 0,
                'vendors_bytes': 0,
                'post_cb': 0,
            }
        cb_state_match = cb_state_comp.match(data['request'])
        cb_match = cb_comp.match(data['request'])
        vendors_match = vendors_comp.match(data['request'])
        post_cb_match = post_cb_comp.match(data['request'])
        if cb_state_match:
            match_data = cb_state_match.groups()
            if match_data[1] == '%2Fb%3Ffrom%3Dwoda':  # woda
                rlt[data['remote_addr']]['woda_cb'] += 1
            else:
                rlt[data['remote_addr']]['normal_cb'] += 1
        if cb_match:
            rlt[data['remote_addr']]['normal_cb'] += 1
        if vendors_match:
            rlt[data['remote_addr']]['vendors'] += 1
            rlt[data['remote_addr']]['vendors_bytes'] += int(data['bytes_sent'])
        if post_cb_match:
            rlt[data['remote_addr']]['post_cb'] += 1

    post_cb_count, woda_count = 0, 0
    for remote_addr, data in rlt.items():
        if data['woda_cb'] > 0:
            print(remote_addr, data['woda_cb'], data['vendors'], data['post_cb'])
            if data['post_cb'] <= 0:
                print(data['vendors_bytes'])
            woda_count += 1
            if data['post_cb'] > 0:
                post_cb_count += 1
    print(woda_count, post_cb_count)


def user_agent():
    import json
    logs = analysis_nginx_logs()
    rlt = {}
    for data in logs:
        if not data['user_agent'] in rlt:
            rlt[data['user_agent']] = 0
        rlt[data['user_agent']] += 1
    print(json.dumps(rlt))


def app_log():
    import re
    app_log = r'\[([^\]]+)\]\[([A-Z]+)\]\[[^\]]+\]\[[^\]]+\]\[[^\]]+\]: (.*)'
    app_comp = re.compile(app_log)

    error_log = r'user \[([0-9]+)\]\[([0-9]+)\]\[([0-9]+)\] ([a-z\s]+) error: (.*)'
    error_comp = re.compile(error_log)

    user_error = {}

    plan_ids = set()
    with open('/Users/wangyijun/ads/log/remote/app_error.log') as file_obj:
        for line in file_obj.readlines():
            log_match = app_comp.match(line)
            if not log_match:
                print(line)
                continue
            data = log_match.groups()
            log_t = data[0]  # datetime.strptime(data[0], '%Y-%m-%d %H:%M:%S,%f')
            log_level = data[1]
            log_str = data[2]
            error_match = error_comp.match(log_str)
            if not error_match:
                print(line)
                continue
            data = error_match.groups()
            uid = int(data[0])
            plan_id = int(data[1])
            unit_id = int(data[2])
            error_str = data[3]
            plan_ids.add(plan_id)
            if not error_str in user_error:
                user_error[error_str] = {}
            if not uid in user_error[error_str]:
                user_error[error_str][uid] = {}
            if not plan_id in user_error[error_str][uid]:
                user_error[error_str][uid][plan_id] = {}
            if not unit_id in user_error[error_str][uid][plan_id]:
                user_error[error_str][uid][plan_id][unit_id] = []
            user_error[error_str][uid][plan_id][unit_id].append(log_t)

    print(list(plan_ids))

    for error_str, user_data in user_error.items():
        print(error_str)
        for uid, plan_data in user_data.items():
            print(uid)
            for plan_id, unit_data in plan_data.items():
                print(plan_id)
                for unit_id, time_data in unit_data.items():
                    print(unit_id, len(time_data))
                    print(time_data)
            print('\n')
        print('\n\n')
