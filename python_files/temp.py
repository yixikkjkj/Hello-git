
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

def old_analysis_nginx_log():
    import re
    old_log_str = r'([0-9\.]+) - - \[([^\]]+)\] "([^\"]+)" ([0-9]+) ([0-9]+) "([^\"]+)" "([^\"]+)"'
    old_comp = re.compile(old_log_str)
    file_path = '/Users/wangyijun/ads/log/remote/access.log-20201027'
    rlt = []
    with open(file_path, 'r') as file_obj:
        for line in file_obj.readlines():
            old_match = old_comp.match(line)
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

def analysis_nginx_logs(file_path):
    import re
    from datetime import datetime
    log_str = r'([0-9\.]+) - - \[([^\]]+)\] "([^\"]+)" ([0-9]+) ([0-9]+) ([0-9\.]+) "([^\"]+)" "([^\"]+)"'
    log_comp = re.compile(log_str)

    rlt = []
    with open(file_path, 'r') as file_obj:
        for line in file_obj.readlines():
            match = log_comp.match(line)
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


def cb_why_users_not_come():
    import re
    file_path = '/Users/wangyijun/ads/log/remote/access.log-20201027'
    logs = analysis_nginx_logs(file_path)
    cb_state_str = r'GET /cb\?code=([0-9a-z]+).*'
    cb_state_comp = re.compile(cb_state_str)

    rlt = {}
    for data in logs:
        cb_state_match = cb_state_comp.match(data['request'])
        if cb_state_match:
            if not data['user_agent'] in rlt:
                rlt[data['user_agent']] = set()
            rlt[data['user_agent']].add(data['remote_addr'])

    print('total infofofofo', len(rlt))
    for user_agent, data in rlt.items():
        print(user_agent)
        print(len(data))

"""
    "106.114.140.85" # xxxx
    "218.1.238.15"  # todo
    "223.74.213.32"
    "59.110.161.188"
    "223.74.207.137"
    "39.105.57.43"
    "47.94.230.236"
"""


def cb_and_vendors_and_post_cb():
    import re
    file_path = '/Users/wangyijun/ads/log/remote/access.log-20200923'
    logs = analysis_nginx_logs(file_path)
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


def is_that_the_test(acc, status, *plan_id):
    print(acc, status, plan_id)


def airuiwang():
    """
https://www.iresearch.cn/include/ajax/user_ajax.ashx?work=idown&rid=3679
    """
    urls = ''



# %%
# vas_orders = list(db.VasOrder.find({
#     'end_t': {'$gte': today},
# }))
# vas_uids = [order['mall_id'] for order in vas_orders]

# not_exists_uids = list(set(vas_uids).difference(set(uids)))

users = list(db.User.find({
    'expires_at.access': {'$gte': int(today.timestamp())},
}))

uids = list({user['uid'] for user in users})
reports = db.Report.find({'uid': {'$in': uids}})
uid2spend = {}

for report in reports:
    uid2spend[report['uid']] = uid2spend.get(report['uid'], 0) + report['spend']

spend_total = {
    '0': [],
    '0-50': [],
    '50-100': [],
    '100-200': [],
    '200-300': [],
    '300-400': [],
    '400-500': [],
    '500-1000': [],
    '1000-2000': [],
    '2000-5000': [],
    '5000+': []
}

for uid, spend in uid2spend.items():
    if spend == 0:
        spend_total['0'].append(uid)
    elif spend <= 50000:
        spend_total['0-50'].append(uid)
    elif spend <= 100000:
        spend_total['50-100'].append(uid)
    elif spend <= 200000:
        spend_total['100-200'].append(uid)
    elif spend <= 300000:
        spend_total['200-300'].append(uid)
    elif spend <= 400000:
        spend_total['300-400'].append(uid)
    elif spend <= 500000:
        spend_total['400-500'].append(uid)
    elif spend <= 1000000:
        spend_total['500-1000'].append(uid)
    elif spend <= 2000000:
        spend_total['1000-2000'].append(uid)
    elif spend <= 5000000:
        spend_total['2000-5000'].append(uid)
    else:
        spend_total['5000+'].append(uid)

spend_total['0'].extend(list(set(uids).difference(set(uid2spend.keys()))))

print(len(uids))
for key, val in spend_total.items():
    print(key, len(val))


users = list(db.User.find({
    'expires_at.access': {'$gte': int(today.timestamp())},
}))

mobile_uids = [user['uid'] for user in users if user.get('mobile')]
accounts = db.Account.find({'uid': {'$in':uids}})
noopen = []
opened = []
for account in accounts:
    if account['has_open_account']:
        opened.append(account['uid'])
    else:
        noopen.append(account['uid'])

print(len(noopen), len(opened))


# %%
def query_target_report():
    uid = 961996663
    user = db.User.find_one({'uid': uid})
    plan_id = 77746538
    unit_id = 300916456
    start_t = datetime(2020,11,27)
    end_t = datetime(2020,11,28)-timedelta(seconds=1)
    report_list = ads_client.report_entity_report_query(user['access_token'], PLAN.SCENE_TYPE.TARGET_ADV, start_t, end_t, ReportQueryType.Audience, ReportQueryType.Unit, unit_id, plan_id=plan_id)
    print(report_list)


def query_target_hourly_report():
    uid = 961996663
    user = db.User.find_one({'uid': uid})
    plan_id = 77746538
    unit_id = 300916456
    start_date = datetime(2020,11,28)
    report_list = ads_client.report_hourly_report_query(user['access_token'], PLAN.SCENE_TYPE.TARGET_ADV, start_date, ReportQueryType.User, uid)
    print(report_list)


def process_hourly_report():
    uid = 961996663
    process = report_tasks.SyncHourlyReportProcess(now)
    if process.init_data([uid], now):
        report_tasks.sync_hourly_report.delay(now)

uid = 961996663
db.HourlyReport.find_one({'uid': uid, 'scene_type': 2})


# %%
vases = list(db.VasOrder.find({
    'end_t': {'$gte': datetime(2020, 11,30), '$lt': datetime(2020, 12, 6)},
}))

uids = list({vas['mall_id'] for vas in vases})
print('uids lenggggg', len(uids))
users = list(db.User.find({
    'uid': {'$in': uids},
}))
uid2vas = {vas['mall_id']: vas for vas in vases}
print('users lenggggg', len(users))
for user in users:
    data_list = ','.join([str(user['uid']), user['mall_name'], uid2vas[user['uid']]['end_t'].strftime('%Y-%m-%d %H:%M:%S'), user.get('mobile', '')])
    print(data_list)


# %%
from app.tasks import monitor as monitor_tasks

monitor_tasks.update_daily_pdd_serivers.delay()

# db.GoodsAnalysis.remove({})

uid = 444951560
unit_id = 287994597
keyword_stat = list(db.KeywordStatistics.find({
    'uid': uid,
    'unit_id': unit_id,
    'd': datetime(2020,10,24),
}))


# %%
def fugoulv():
    vas_orders = list(db.VasOrder.find({
        'created_ts': {'$gte': int((today - timedelta(days=365)).timestamp() * 1000)},
        'pay_status': 1,
        'amount': {'$gt': 0}
    }))
    uidcountmap={}
    for order in vas_orders:
        if not order['mall_id'] in uidcountmap:
            uidcountmap[order['mall_id']] = 0
        uidcountmap[order['mall_id']] += 1
    valid_uids = [uid for uid, count in uidcountmap.items() if count > 1]
    uids = {order['mall_id'] for order in vas_orders}
    print(len(valid_uids), len(uids), len(valid_uids)/len(uids))

fugoulv()


# %%
from app.forms.account import PlanListForm
from wsgi import create_app
from settings import config
from werkzeug.datastructures import CombinedMultiDict, ImmutableMultiDict

print(PlanListForm)
print(PlanListForm.plan_type)

app = create_app(config, 'app')
values = CombinedMultiDict([ImmutableMultiDict([]), ImmutableMultiDict([('plan_type', '[]')])])
print(values)
with app.app_context() as context:
    form = PlanListForm(values)
    print(form)
    print(dir(form))
    print(form.start_t)
    print(dir(form.start_t))
    print(form.data)
    print(form.start_t.populate_obj)


# %%
# keyword_id_list = [4548806807, 4548806819, 4548806810, 4548806806, 4548806805, 4548806811]
# spec ={'unit_id': 257750425, 'status': 1, 'keyword_id': {'$in': [4548806807, 4548806819, 4548806810, 4548806806, 4548806805, 4548806811]}}
# spec['keyword_id'] = {'$nin': keyword_id_list}
# db.Keyword.count(spec, skip=max(0, 20 - len(keyword_id_list)), limit=14)
# db.User.find({'created_t': {'$exists': False}})
# db.VasOrder.find({'start_t': {'$lt': datetime(2020,4,7)}})

vas_order_list = list(db.VasOrder.find(
    {'start_t': {'$gte': yesterday + timedelta(hours=17)}}
))
uid2vasorderlist = {}
for vas_order in vas_order_list:
    if vas_order['mall_id'] not in uid2vasorderlist:
        uid2vasorderlist[vas_order['mall_id']] = []
    uid2vasorderlist[vas_order['mall_id']].append(vas_order)

user_list = list(db.User.find({'uid': {'$in': list(uid2vasorderlist.keys())}}))
for user in user_list:
    info_list = [str(user['uid']), user['mall_name'], user['created_t'].strftime('%Y-%m-%d %H:%M:%S'), user.get('mobile', '')]
    order_str = ''
    free, month, quater, half, year = 0,0,0,0,0
    for vas_order in uid2vasorderlist[user['uid']]:
        if vas_order['sku_id'] == 19336:
            free += 1
        elif vas_order['sku_id'] == 19337:
            month += 1
        elif vas_order['sku_id'] == 19338:
            year += 1
        elif vas_order['sku_id'] == 19339:
            quater += 1
        elif vas_order['sku_id'] == 19340:
            half += 1
    if free:
        order_str += f'订购免费版{free}次'
    if month:
        order_str += f'订购1个月{month}次'
    if quater:
        order_str += f'订购免费版{quater}次'
    if half:
        order_str += f'订购免费版{half}次'
    if year:
        order_str += f'订购免费版{year}次'
    info_list.append(order_str)
    print(','.join(info_list))


# %%
user = db.User.find_one({'uid': bengou})
goods = db.Goods.find_one({'uid': user['uid']})
plan_id = 48299329
unit_id = 248898107
# ads_client.unit_query_list(user['access_token'], 32185950, datetime(2020, 8, 17), datetime(2020,9,16))
# ads_client.unit_bid_query_list(user['access_token'], unit_id, BidReferenceType.Location)
from app.actions import account as account_actions

account_actions.get_unit_bid_list(user['access_token'], bengou, plan_id, unit_id, UNIT_BID.REFERENCE_TYPE.LOCATION)
# db.UnitBid.find_one({'unit_id': unit_id})


# %%
# [{'uvString': '', 'targetName': '商品潜力人群', 'targetType': 11100},
#  {'uvString': '', 'targetName': '相似商品定向', 'targetType': 103},
#  {'uvString': '', 'targetName': '访客重定向', 'targetType': 102},
#  {'uvString': '', 'targetName': '相似店铺定向', 'targetType': 11200},
#  {'uvString': '', 'targetName': '叶子类目定向', 'targetType': 11300},
#  {'uvString': '', 'targetName': '折扣/低价偏好人群', 'targetType': 11400},
#  {'uvString': '', 'targetName': '高品质商品偏好人群', 'targetType': 11401},
#  {'uvString': '', 'targetName': '爆品偏好人群', 'targetType': 11402},
#  {'uvString': '', 'targetName': '新品偏好人群', 'targetType': 11403},
#  {'uvString': '', 'targetName': '高消费人群', 'targetType': 11404},
#  {'uvString': '', 'targetName': '平台活跃人群', 'targetType': 11406},
#  {'uvString': '', 'targetName': '地域', 'targetType': 8}]

# 搜索推广可用的基础人群定向

user = db.User.find_one({'uid': bengou})
# ads_client.plan_query_list(user['access_token'], datetime(2020,8,16), datetime(2020,9,15), 2)
goods = db.Goods.find_one({'uid': user['uid']})
ads_client.unit_bid_query_base_target_profile(user['access_token'], goods['goods_id'], 2)


# %%
user = db.User.find_one({'uid': bengou})
# ads_client.plan_query_list(user['access_token'], datetime(2020,8,16), datetime(2020,9,15), 2)
goods = db.Goods.find_one({'uid': user['uid']})
ads_client.unit_bid_query_targeting_tag_list(user['access_token'])

# 地域定向标签，各种地级市的tagid


# %%
# list(db.PlanStatistics.find({'d': today - timedelta(days=2), 'plan_id': 41448399}))

from app.ext.pdd_client_v2 import ads_client, ReportQueryType

uid = 856681638
user = db.User.find_one({'uid':uid})
# db.User.find_one_and_update({'uid': uid}, {'$set': {'access_token': 'ec56dfcad1a843718fb521c9b614f15ca9476260', 'is_expired': 0}})
plan_id = 41448399
unit_id = 237921157

# ads_client.report_daily_report_query(user['access_token'], today, now, ReportQueryType.Plan, plan_id)

# ads_client.report_entity_report_query(user['access_token'], today, now, ReportQueryType.Keyword, ReportQueryType.Unit, unit_id, plan_id=plan_id)
# db.User.find_one_and_update({'uid': uid}, {'$set': {'access_token': 'b69866a2d2284f0c91fa3301e95dd8129b2eadb6'}})
# ads_client.report_hourly_report_query(user['access_token'], now, ReportQueryType.User, uid)
# ads_client.report_daily_report_query(user['access_token'], datetime(2020,8,30), datetime(2020,8,31) -timedelta(seconds=1), ReportQueryType.Plan, 35245353)
# ads_client.report_entity_report_query(user['access_token'], datetime(2020, 8, 29), datetime(2020, 8,30)-timedelta(seconds=1), ReportQueryType.Plan, ReportQueryType.User)
# ads_client.report_hourly_report_query(user['access_token'], today, ReportQueryType.Plan, plan_id)
# ads_client.plan_query_list(user['access_token'], datetime(2020,8,1), now)
ads_client.plan_query_list(user['access_token'], datetime(2020, 8, 15), datetime(2020, 9, 14))


# %%
from app.actions.account import account_actions
user = db.User.find_one({'uid': bengou})
unit_data_list = [
    {
        'name': '推广单元_698',
        'goods': 76163390719,
        'smart_creative': {
            'title': '手工制作生日礼物',
            'enable': 1,
        },
        'audience': [
            {'reference_id': 1, 'sub_reference_id': 0, 'bid': 100},
        ],
        'location': [
            {'reference_id': UNIT_BID.LOCATION_ID.GOODS_CAT, 'bid': 10000},
            {'reference_id': UNIT_BID.LOCATION_ID.GOODS_DETAIL, 'bid': 10000},
            {'reference_id': UNIT_BID.LOCATION_ID.PROMO_ACT, 'bid': 10000},
            {'reference_id': UNIT_BID.LOCATION_ID.OUTSTAND_ACT, 'bid': 10000},
        ]
    }
]
account_actions.create_scene_plan(user['access_token'], bengou, '虎虎推广_场景_2334', 100, PLAN.PLAN_TYPE.MANUAL, unit_data_list)


# %%
uid = 856681638
user = db.User.find_one({'uid': uid})
date_ts = int(now.timestamp() / 86400) * 86400 - 8 * 3600
process = report_tasks.SyncDailyProcess(date_ts, page=0)
if process.init_data(date_ts, [uid]):
    report_tasks.sync_daily_report.delay(date_ts, {'page': 0})


# %%
user_list = list(db.User.aggregate([
    {'$match': {'expires_at.access': {'$lte': int(today.timestamp())}, 'mobile': {'$exists': True}}},
    {'$sort': {'expires_at.access': -1}}
]))
uid_list = [data['uid'] for data in user_list]
uid_report = list(db.Report.aggregate([
    {'$match': {'status': REPORT_STATUS.NORMAL, 'spend': {'$gte': 0}, 'uid': {'$in': uid_list}}},
    {'$group': {'_id': '$uid', 'spend': {'$sum': '$spend'}}},
]))

uid2spend = {data['_id']: data['spend'] for data in uid_report}
target_list = []
for data in user_list:
    if not data['uid'] in uid2spend:
        continue
    data['spend'] = uid2spend[data['uid']]
    target_list.append(data)

for data in target_list:
    print(','.join([str(data['uid']), data['mall_name'], data['mobile'], datetime.fromtimestamp(data['expires_at']['access']).strftime('%Y-%m-%d %H:%M:%S'), str(data['spend']/1000)]))


user_list = list(db.User.find({'expires_at.access': {'$gte': int(today.timestamp()+2*3600*24)}}))

uid_list = [data['uid'] for data in user_list]

uid_report = list(db.Report.aggregate([
    {'$match': {'status': REPORT_STATUS.NORMAL, 'spend': {'$gte': 0}, 'uid': {'$in': uid_list}}},
    {'$group': {'_id': '$uid', 'spend': {'$sum': '$spend'}}},
    {'$sort': {'spend': -1}},
]))[:20]
print([data['_id'] for data in uid_report])


# %%


def insert_user():
    user_data = {'_id': ObjectId('5e83031b389df5e16c293ae6'), 'uid': 8298818, 'access_token': 'b9f38901cf8748aeabc289a7f6c916bd964b970f', 'expires_at': {'access': 1618194607, 'refresh': 1618194607, 'r1': 1618194607, 'r2': 1618194607, 'w1': 1618194607, 'w2': 1618194607}, 'last_login_t': datetime(2020, 4, 17, 10, 30, 49, 278000), 'refresh_token': 'e2bf70ccec8b4fa49342d0494d62dd17cc7de2e5', 'username': 'pdd82988180006', 'created_t': datetime(2020, 3, 31, 16, 45, 15, 956000), 'logo_url': 'http://t16img.yangkeduo.com/pdd_ims/1de56d63c054ffa39d44559a8239d7a9.jpg', 'mall_desc': '潮鞋专营,都是超好看的鞋子哦!', 'mall_name': '港岛妹妹大卖铺', 'mall_type': 1, 'huhu_level': 16, 'huhu_level_expire_t': datetime(2020, 11, 27, 16, 42, 11, 462000)}
    from app.base import account as account_base
    user_data.pop('_id')
    db.User.find_one_and_update({
        'uid': user_data['uid'],
    }, {'$set': user_data}, upsert=True)
    try:
        account_base.save_account(user_data['uid'], user_data['access_token'])
    except:
        return

insert_user()


# %%
muti_keywords = list(db.Keyword.aggregate([
    {'$group': {'_id': '$keyword_id', 'sum': {'$sum': 1}}},
    {'$match': {'sum': {'$gt': 1}}},
], allowDiskUse=True))
for data in muti_keywords:
    keyword_list = list(db.Keyword.find({'keyword_id': data['_id']}, sort=[('status', 1), ('created_t', -1)]))
    if not keyword_list:
        continue
    id_list = [keyword['_id'] for keyword in keyword_list[1:]]
    db.Keyword.delete_many({'_id': {'$in': id_list}})


# %%
from app.ext.pdd_client_v2 import ads_client

from app.tasks import report
uid = 527907889
plan_id_list = [data['plan_id'] for data in db.PlanStatistics.find({'uid':uid, 'd': {'$gte':yesterday}})]
# print(db.Unit.find_one({'unit_id': 219722286}))
keyword_id_list = [data['keyword_id'] for data in db.Keyword.find({'uid': uid})]
keyword_id_list = [data['keyword_id'] for data in db.KeywordStatistics.find({'uid':uid, 'keyword_id': {'$in': keyword_id_list}})]
keyword_id_list

list(db.Keyword.find({'keyword_id': {'$in':keyword_id_list}}))

unit_id = 204909022
user = db.User.find_one({'uid':uid})
# ads_client.keyword_query_list(user['access_token'], unit_id, yesterday, today - timedelta(seconds=1))
db.Unit.find_one({'unit_id': unit_id})
db.Plan.find_one({'plan_id': 34090599})
datetime.fromtimestamp(1596771055)


# %%
from app.ext.pdd_client_v2 import ads_client, SceneType
from app.models.constants import REPORT_STATUS

def get_has_report_uid_list():
    user_list = [data['uid'] for data in db.User.find({
        'expires_at.access': {'$gt': int(datetime.now().timestamp())},
        'is_expired': {'$ne': 1},
    }, ['uid'])]
    report_list = {data['_id']: data['keyword_id'] for data in db.KeywordStatistics.aggregate([
        {'$match': {'status': REPORT_STATUS.NORMAL, 'uid': {'$in': user_list}, 'd': {'$gte': datetime(2020,8,6)}}},
        {'$group': {'_id': '$uid', 'keyword_id':{'$addToSet': '$keyword_id'}}}
    ])}
    has_report_list = []
    for uid, keyword_ids in report_list.items():
        tmp_ids = [data['plan_id'] for data in db.Keyword.find({'keyword_id': {'$in': keyword_ids}})]
        has_ids = list(db.Plan.find({'plan_id': {'$in': tmp_ids}, 'status': {'$ne': PLAN.STATUS.DELETED}, 'uid': uid}))
        if has_ids:
            has_report_list.append(uid)
    return has_report_list

def update_user_pdd_data(uid_list):
    now_ts = int(now.timestamp())
    process = account_tasks.SyncProcess(now_ts)
    if process.init_data(now_ts, uid_list):
        account_tasks.sync_pdd_data.delay(now_ts)
    else:
        print('没有初始化成功')

uid_list = get_has_report_uid_list()
# update_user_pdd_data(uid_list)
uid_list


# %%
uid_list = [ 830080557, 527907889, 903115827, 410926132, 254813239, 5757498,]


now_ts = int(datetime.now().timestamp())
process = account_tasks.SyncProcess(now_ts)
if process.init_data(now_ts, uid_list, 1):
    account_tasks.sync_pdd_data.delay(now_ts)


# %%
pro = list(db.PromoteLog.aggregate([
    {'$sort': {'created_t': -1}},
    {'$group': {'_id': '$uid', 'created_t': {'$first': '$created_t'}}},
    {'$sort': {'created_t': -1}},
    {'$limit': 20},
]))


# %%
goods_count = list(db.Goods.aggregate([
    {'$group':{'_id': '$uid', 'sum': {'$sum': 1}}}
]))
goods_count.sort(key=lambda data: data['sum'])
goods_count = {data['_id']: data['sum'] for data in goods_count}
user_list = list(db.User.find({'uid': {'$in': list(goods_count.keys())}, 'expires_at.access': {'$gte': int(now.timestamp())}, 'is_expired':{'$ne':1}}))
user_list.sort(key=lambda data: data['created_t'])
valid_goods_count = [(data['uid'], goods_count[data['uid']]) for data in user_list]
valid_goods_count.sort(key=lambda data: data[1])


# %%
def exec():
    plan_ids = [data['plan_id'] for data in plans]
    plan_valid_uids = [data['_id'] for data in db.Keyword.aggregate([
        {'$match': {'plan_id': {'$in': plan_ids}, 'status': KEYWORD.STATUS.ACTIVED}},
        {'$group': {'_id': '$uid', 'sum': {'$sum': 1}}}
    ])]
    return plan_valid_uids


# %%
def edit_csv():
    file_path = '/Users/wangyijun/Documents/'
    file_name = 'meizhe_sms_0716.csv'

    name2package = {
        '活动 870940': ['A-1-1', '到期2天'],
        '活动 887596': ['A-1-1', '到期4天'],
        '活动 792862': ['A-1-2', '到期2天'],
        '活动 30728': ['A-1-2', '到期4天'],
        '活动 367187': ['A-1-3', '到期2天'],
        '活动 716515': ['A-1-3', '到期4天'],
        '活动 800664': ['A-2-1', '到期2天'],
        '活动 979055': ['A-2-1', '到期4天'],
        '活动 940886': ['A-2-2', '到期2天'],
        '活动 920969': ['A-2-2', '到期4天'],
        '活动 682011': ['A-2-3', '到期2天'],
        '活动 785223': ['A-2-3', '到期4天'],
    }
    rlt = ''
    with open(file_path + file_name, 'r') as file_obj:
        for line in file_obj.readlines():
            plan_name = line.split(',')[0]
            line = line.replace(plan_name, ','.join(name2package[plan_name]))
            rlt += line
    print(rlt)
edit_csv()


# %%
@celery.task
def analysis_report():
    now = datetime.now()
    start_t = datetime(now.year, now.month, now.day) - timedelta(days=8)
    yesterday = datetime(now.year, now.month, now.day) - timedelta(days=1)
    report_list = list(db.KeywordStatistics.find({
        'report_date': start_t,
    }))
    id2list = {}
    for report in report_list:
        if report['keyword_id'] not in id2list:
            id2list[report['keyword_id']] = []
        id2list[report['keyword_id']].append(report)

    for keyword_id, stat_list in id2list.items():
        stat_list.sort(lambda stat: stat['d'])
        last_stat = stat_list[-1]
        if last_stat['d'] != yesterday:
            last_stat = stat_base.insert_empty_keyword_statistics(
                last_stat['uid'], last_stat['plan_id'], last_stat['unit_id'], keyword_id, yesterday
            )
            stat_list.append(last_stat)

def insert_empty_keyword_statistics(uid, plan_id, unit_id, keyword_id, report_date):
    stat = empty_stat.copy()
    stat.update({
        'uid': uid,
        'plan_id': plan_id,
        'unit_id': unit_id,
        'keyword_id': keyword_id,
        'd': report_date,
        'status': REPORT_STATUS.EMPTY,
    })
    db.KeywordStatistics.insert_one(stat)
    return stat


# %%
def analysis_user_balance_log():
    import json
    import re
    from datetime import datetime
    # [\/a-z\.\:0-9]+
    match_str = r'.*\[([0-9\-\s\:\,]+)\].*user \[([0-9]+)\] balance changed \[([\-0-9]+)\]->\[([\-0-9]+)\] \[(.*)\]->\[(.*)\]'
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
    dir_path = '/Users/wangyijun/ads/log/remote/user_balance/account_balance/'
    for uid in uid_list:
        print(uid, uid2name[uid])
        print()
        balance_list = []
        with open(dir_path + 'account_balance_' + str(uid), 'r') as file_obj:
            for line in file_obj.readlines():
                match_rlt = complied_str.match(line)
                if not match_rlt:
                    print(line)
                    continue
                rlt = match_rlt.groups()
                record_time = datetime.strptime(rlt[0], '%Y-%m-%d %H:%M:%S,%f')
                old_balance = int(rlt[2])
                new_balance = int(rlt[3])
                old_accounts = json.loads(rlt[4].replace('\'', '\"'))
                new_accounts = json.loads(rlt[5].replace('\'', '\"'))
                balance_list.append([str(uid), uid2name[uid], record_time, str(old_balance/1000), str(new_balance/1000)])

        out_dir = '/Users/wangyijun/ads/user_balance_log/'
        with open(out_dir + uid2name[uid] + '.csv', 'w+') as out_file:
            out_file.write('用户ID,店名,检查时间,旧余额（元）,新余额（元）\r\n')
            balance_list.sort(key=lambda x: x[2])
            for balance_info in balance_list:
                balance_info[2] = balance_info[2].strftime('%Y-%m-%d %H:%M:%S')
                out_file.write(','.join(balance_info) + '\r\n')
                print(','.join(balance_info))
            out_file.flush()

        print('\n')

analysis_user_balance_log()


# %%
@cli.command()
def testttt():
    import json
    from app.actions.account import create_trustee_plan

    unit_data_list = json.loads('[{"name":"推广单元_3028","smart_creative":{"title":"手工制作生日礼物","enable":1},"goods_id":76163390719,"keyword":[{"word":"生日礼物","bid":300,"index":0},{"word":"七夕礼物","bid":500,"index":1},{"word":"情人节礼物","bid":600,"index":2},{"word":"手工制作礼物","bid":400,"index":3},{"word":"七夕情人节礼物","bid":500,"index":4},{"word":"教师节礼物","bid":400,"index":5},{"word":"diy手工礼物","bid":300,"index":6},{"word":"七夕节礼物","bid":700,"index":7},{"word":"毕业礼物","bid":300,"index":8},{"word":"水晶球生日礼物","bid":300,"index":9},{"word":"教师节礼物手工","bid":400,"index":10},{"word":"恶搞礼物","bid":300,"index":11},{"word":"结婚礼物","bid":400,"index":12},{"word":"手工礼物","bid":300,"index":13},{"word":"diy礼物","bid":400,"index":14},{"word":"糖果生日礼物","bid":1400,"index":15},{"word":"哆啦a梦生日礼物","bid":300,"index":16},{"word":"照片定制礼物","bid":300,"index":17},{"word":"搞怪礼物","bid":300,"index":18},{"word":"礼盒装礼物","bid":1800,"index":19}]}]')
    plan_type = 34
    name = '虎虎推广_132269'
    bengou_uid = 425740142
    user = db.User.find_one({'uid': bengou_uid})
    print(create_trustee_plan(user['access_token'], user['uid'], name, 33, unit_data_list + unit_data_list))


# %%
def analysis_nginx_log():
    import re
    log_re = r'([0-9\.]+).*\[(.+)\].*'
    log_comp = re.compile(log_re)
    texts = ""
    rlt = []
    for line in texts.split('\n'):
        xx = log_comp.match(line)
        if not xx:
            print(line)
            continue
        data = xx.groups()
        client_ip = data[0]
        log_t = datetime.strptime(data[1], '%d/%b/%Y:%H:%M:%S +%f') + timedelta(hours=8)
        rlt.append((client_ip, log_t))

    return rlt

client_log = analysis_nginx_log()
ip2time = {data[0]: data[1] for data in client_log}
for ip, t in ip2time.items():
    print(ip, '\t\t', t.strftime('%Y-%m-%d %H:%M:%S'))


# %%
def plan_data():
    from app.models import db
    from bson import ObjectId
    from datetime import datetime, timedelta
    from app.models.constants import PLAN, RECORD
    now = datetime.now()
    yesterday = datetime(now.year, now.month, now.day) - timedelta(days=1)
    today = datetime(now.year, now.month, now.day)
    plan_list = list(db.Plan.collection.find({
        'created_t': {'$gte': today, '$lt': today + timedelta(days=1)},
        'plan_type': PLAN.TYPE.FILE,
        'status': PLAN.STATUS.FINISHED,
    }, sort=[('created_t', 1)]))
    print([plan['name'] for plan in plan_list])
    rlt = ''
    for plan in plan_list:
        record_list = list(db.Record.collection.find({
            'plan_id': plan['_id'],
            'status': {'$in': [RECORD.STATUS.FAILED, RECORD.STATUS.SKIP]},
        }))
        for record in record_list:
            error_msg = ''
            if record['status'] == RECORD.STATUS.FAILED:
                error_msg = record.get('msg', '')
            else:
                error_msg = '被拒绝'
            data_list = [plan['name'], plan['text'], plan['created_t'].strftime("%Y-%m-%d %H:%M:%S"), record['mobile'], error_msg]
            rlt += ','.join(data_list)
            rlt += '\n'
    print(rlt)


def edit_csv():
    file_path = '/Users/wangyijun/Documents'
    file_name = 'meizhe_sms_0713.csv'
    name2package = {
        '活动 491734': ['A-1-1', '到期2天'],
        '活动 146368': ['A-1-1', '到期7天'],
        '活动 253285': ['A-1-1', '到期31天'],
        '活动 75791': ['A-1-2', '到期2天'],
        '活动 5357': ['A-1-2', '到期7天'],
        '活动 129782': ['A-1-2', '到期31天'],
        '活动 344640': ['A-1-3', '到期2天'],
        '活动 610851': ['A-1-3', '到期7天'],
        '活动 917477': ['A-1-3', '到期31天'],
        '活动 518177': ['A-2-1', '到期2天'],
        '活动 507398': ['A-2-1', '到期7天'],
        '活动 877901': ['A-2-1', '到期31天'],
        '活动 461776': ['A-2-2', '到期2天'],
        '活动 123124': ['A-2-2', '到期7天'],
        '活动 710124': ['A-2-2', '到期31天'],
        '活动 93252': ['A-2-3', '到期2天'],
        '活动 485723': ['A-2-3', '到期7天'],
        '活动 679411': ['A-2-3', '到期31天'],
        '活动 649398': ['A-3-1', '到期2天'],
        '活动 955618': ['A-3-1', '到期7天'],
        '活动 476383': ['A-3-1', '到期31天'],
        '活动 432195': ['A-3-2', '到期2天'],
        '活动 690602': ['A-3-2', '到期7天'],
        '活动 792774': ['A-3-2', '到期31天'],
        '活动 519681': ['A-3-3', '到期2天'],
        '活动 409978': ['A-3-3', '到期7天'],
        '活动 741556': ['A-3-3', '到期31天'],
        '活动 692901': ['B-1-1', '到期2天'],
        '活动 551096': ['B-1-1', '到期7天'],
        '活动 70975': ['B-1-1', '到期31天'],
        '活动 342242': ['B-1-2', '到期2天'],
        '活动 262094': ['B-1-2', '到期7天'],
        '活动 51676': ['B-1-2', '到期31天'],
        '活动 445244': ['B-1-3', '到期2天'],
        '活动 618835': ['B-1-3', '到期7天'],
        '活动 145033': ['B-1-3', '到期31天'],
        '活动 415040': ['B-2-1', '到期2天'],
        '活动 491649': ['B-2-1', '到期7天'],
        '活动 55597': ['B-2-1', '到期31天'],
        '活动 248472': ['B-2-2', '到期2天'],
        '活动 730184': ['B-2-2', '到期7天'],
        '活动 954675': ['B-2-2', '到期31天'],
        '活动 677043': ['B-2-3', '到期2天'],
        '活动 259166': ['B-2-3', '到期7天'],
        '活动 954693': ['B-2-3', '到期31天'],
        '活动 13116': ['B-3-1', '到期2天'],
        '活动 541149': ['B-3-1', '到期7天'],
        '活动 346033': ['B-3-1', '到期31天'],
        '活动 460760': ['B-3-2', '到期2天'],
        '活动 163180': ['B-3-2', '到期7天'],
        '活动 124057': ['B-3-2', '到期31天'],
        '活动 882664': ['B-3-3', '到期2天'],
        '活动 379199': ['B-3-3', '到期7天'],
        '活动 390676': ['B-3-3', '到期31天'],
        '活动 468757': ['C-1-1', '到期2天'],
        '活动 17141': ['C-1-1', '到期7天'],
        '活动 310863': ['C-1-1', '到期31天'],
        '活动 43522': ['C-1-2', '到期2天'],
        '活动 411123': ['C-1-2', '到期7天'],
        '活动 336302': ['C-1-2', '到期31天'],
        '活动 943065': ['C-2-1', '到期2天'],
        '活动 46587': ['C-2-1', '到期7天'],
        '活动 877579': ['C-2-1', '到期31天'],
        '活动 951784': ['C-2-2', '到期2天'],
        '活动 530124': ['C-2-2', '到期7天'],
        '活动 419816': ['C-2-2', '到期31天'],
        '活动 939295': ['C-3-1', '到期2天'],
        '活动 365665': ['C-3-1', '到期7天'],
        '活动 281289': ['C-3-1', '到期31天'],
        '活动 687216': ['C-3-2', '到期2天'],
        '活动 514164': ['C-3-2', '到期7天'],
        '活动 393209': ['C-3-2', '到期31天'],
    }
    with open(file_path + file_name, 'r') as file_obj:
        for line in file_obj.readlines():
            plan_name = line.split(',')[0]
            line.replace(plan_name, ','.join(name2package[plan_name]))
            print(line)


# %%

def count_log_api():
    import re
    request_str = r'\[([^\]]+)\]\[[A-Z]+\]\[([0-9a-z]+)\] call \[([a-z\.]+)\] with (.*)'
    resp_str = r'\[([^\]]+)\]\[[A-Z]+\]\[([0-9a-z]+)\] return \<[0-9]+\> (.*)'
    request_comp = re.compile(request_str)
    resp_comp = re.compile(resp_str)
    file_name = '/root/ads/log/app/pdd.log-20201010'
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
    rlt.sort(key=lambda x: x[3], reverse=True)
    for data in rlt:
        print(data)

count_log_api()


# %%
analysis_list =[{'_id': ObjectId('5fa2580ab069e5098b08d9ef'), 'analysis_date': datetime(2020, 10, 27, 0, 0), 'goods_id': 152957008477, 'click': 601, 'gmv': 575730, 'impression': 7552, 'keyword_low_score': [{'keyword_id': 5529704608, 'word': '小菜下饭菜农家', 'score': 2}, {'keyword_id': 5529704605, 'word': '蒜种', 'score': 4}, {'keyword_id': 5529704600, 'word': '蒜茄子', 'score': 2}, {'keyword_id': 5529704588, 'word': '泡', 'score': 2}, {'keyword_id': 5529704579, 'word': '山东大蒜头', 'score': 4}, {'keyword_id': 5529704572, 'word': '泡菜下饭菜香辣', 'score': 2}, {'keyword_id': 5529704571, 'word': '小菜下饭菜开胃', 'score': 2}, {'keyword_id': 5529704531, 'word': '大蒜头 干蒜', 'score': 4}, {'keyword_id': 5529704529, 'word': '紫皮大蒜', 'score': 4}, {'keyword_id': 5529704525, 'word': '干大蒜头', 'score': 4}, {'keyword_id': 5529704523, 'word': '大蒜头5斤新鲜', 'score': 4}, {'keyword_id': 5529704520, 'word': '干大蒜头批发价', 'score': 4}, {'keyword_id': 5529704514, 'word': '山东大蒜头干蒜', 'score': 4}], 'order_num': 43, 'spend': 214972, 'uid': 924178634, 'unit_id_list': [266507592, 296167272]}, {'_id': ObjectId('5fa25806b069e5098b08b410'), 'analysis_date': datetime(2020, 10, 28, 0, 0), 'goods_id': 152957008477, 'click': 783, 'gmv': 518130, 'impression': 11121, 'keyword_low_score': [{'keyword_id': 5529704608, 'word': '小菜下饭菜农家', 'score': 2}, {'keyword_id': 5529704605, 'word': '蒜种', 'score': 4}, {'keyword_id': 5529704600, 'word': '蒜茄子', 'score': 2}, {'keyword_id': 5529704588, 'word': '泡', 'score': 2}, {'keyword_id': 5529704579, 'word': '山东大蒜头', 'score': 4}, {'keyword_id': 5529704572, 'word': '泡菜下饭菜香辣', 'score': 2}, {'keyword_id': 5529704571, 'word': '小菜下饭菜开胃', 'score': 2}, {'keyword_id': 5529704531, 'word': '大蒜头 干蒜', 'score': 4}, {'keyword_id': 5529704529, 'word': '紫皮大蒜', 'score': 4}, {'keyword_id': 5529704525, 'word': '干大蒜头', 'score': 4}, {'keyword_id': 5529704523, 'word': '大蒜头5斤新鲜', 'score': 4}, {'keyword_id': 5529704520, 'word': '干大蒜头批发价', 'score': 4}, {'keyword_id': 5529704514, 'word': '山东大蒜头干蒜', 'score': 4}], 'order_num': 34, 'spend': 296887, 'uid': 924178634, 'unit_id_list': [266507592, 296167272]}, {'_id': ObjectId('5fa25802b069e5098b088bbd'), 'analysis_date': datetime(2020, 10, 29, 0, 0), 'goods_id': 152957008477, 'click': 671, 'gmv': 369360, 'impression': 8681, 'keyword_low_score': [], 'order_num': 29, 'spend': 200000, 'uid': 924178634, 'unit_id_list': [266507592]}, {'_id': ObjectId('5fa257fdb069e5098b085e1f'), 'analysis_date': datetime(2020, 10, 30, 0, 0), 'goods_id': 152957008477, 'click': 1880, 'gmv': 1229380, 'impression': 182246, 'keyword_low_score': [], 'order_num': 92, 'spend': 504092, 'uid': 924178634, 'unit_id_list': [214194101, 266507592, 298682917, 298685022]}, {'_id': ObjectId('5fa257e9b069e5098b082920'), 'analysis_date': datetime(2020, 10, 31, 0, 0), 'goods_id': 152957008477, 'click': 1916, 'gmv': 926000, 'impression': 154605, 'keyword_low_score': [], 'order_num': 65, 'spend': 456052, 'uid': 924178634, 'unit_id_list': [214194101, 266507592, 298682917, 298685022]}, {'_id': ObjectId('5fa257e7b069e5098b08101e'), 'analysis_date': datetime(2020, 11, 1, 0, 0), 'goods_id': 152957008477, 'click': 1567, 'gmv': 926700, 'impression': 130250, 'keyword_low_score': [], 'order_num': 68, 'spend': 460233, 'uid': 924178634, 'unit_id_list': [214194101, 266507592, 298682917, 298685022]}, {'_id': ObjectId('5fa257cdb069e5098b07e730'), 'analysis_date': datetime(2020, 11, 2, 0, 0), 'goods_id': 152957008477, 'click': 1256, 'gmv': 976030, 'impression': 72309, 'keyword_low_score': [], 'order_num': 69, 'spend': 338953, 'uid': 924178634, 'unit_id_list': [214194101, 266507592, 298682917, 298685022]}, {'_id': ObjectId('5fa24a37b069e5098b032737'), 'analysis_date': datetime(2020, 11, 3, 0, 0), 'goods_id': 152957008477, 'click': 757, 'gmv': 828070, 'impression': 15011, 'keyword_low_score': [], 'order_num': 68, 'spend': 233702, 'uid': 924178634, 'unit_id_list': [214194101, 266507592, 298682917, 298685022]}]

cvr_list = []
for ana in analysis_list:
    cvr_list.append(ana['order_num'] / ana['click'])
    print(ana['impression'])
    print(ana['unit_id_list'])


# %%
goods_count = list(db.Goods.aggregate([
    {'$group': {'_id': '$uid', 'sum': {'$sum': 1}}},
]))
goods_count.sort(key=lambda x: x['sum'], reverse=True)
goods_count[:10]

uid = 841738523
goods_list = list(db.Goods.find({'uid': uid}))
for goods in goods_list:
    print(','.join([
        str(goods['cat_id']),
        goods.get('cat_name', ''),
        goods['goods_name'],
    ]))




def fill_trustee_keywords(access_token, uid, unit_data_list, plan_type):
    for unit_data in unit_data_list:
        if not unit_data.pop('is_trustee_keyword', None):
            continue
        re_keyword_list = ads_client_v2.keyword_recommend_get(access_token, unit_data['goods_id'])
        re_keyword_list.sort(key=lambda x: (x['relevance'], x['score']), reverse=True)
        keyword_list = []
        for re_keyword in re_keyword_list[:20]:
            data = {
                'bid': min(99000, max(100,
                                      math.ceil(re_keyword['avg_bid'] / 100) * 100)),
                'word': re_keyword['word'],
            }
            if plan_type == PLAN.PLAN_TYPE.LONG_TAIL:
                data['custom_bid'] = min(99000, max(100, math.ceil(re_keyword['avg_bid'] / 200) * 100))
            keyword_list.append(data)
        unit_data['keyword'] = keyword_list
        logger.info('user [%s] create goods [%s] fill trustee keyword [%s]', uid, unit_data['goods_id'], keyword_list)

    return unit_data_list

