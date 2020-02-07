# coding:utf-8

import re

sp = re.compile('^\#{2}')
not_sp = re.compile('^\#{3}')


def ex_report_line(in_file='/Users/wangyijun/Documents/日志.md',
                   out_file='/Users/wangyijun/Documents/日志1.md'):
    report_cache = []
    tmp_cache = []
    with open(in_file, 'r') as report:
        for line in report.readlines():
            if sp.match(line) and not not_sp.match(line):
                if tmp_cache:
                    report_cache.append(tmp_cache)
                    for i in tmp_cache:
                        print(i)
                    print('---' * 30)
                    tmp_cache = []
            tmp_cache.append(line)
        if tmp_cache:
            report_cache.append(tmp_cache)

    report_cache.reverse()
    with open(out_file, 'a+') as new_report:
        for tmp_cache in report_cache:
            new_report.writelines(tmp_cache)
        new_report.flush()


def ignore_duplicated_lock_decorator(
        raise_msg,  # pylint: disable=too-many-arguments
        prefix,
        key=None,
        sub_key=None,
        seconds=None,
        retry_count=0,
        retry_delay=None):
    def wrapper(func, *args, **kwargs):
        built_key = ''
        if key is not None:
            args_name = inspect.getargspec(func)[0]
            try:
                key_index = args_name.index(key)
                built_key = args[key_index]
            except ValueError:
                built_key = kwargs.get(key, '')

            if isinstance(built_key, dict) and sub_key is not None:
                md_args = []
                if isinstance(sub_key, list):
                    for k in sub_key:
                        if k in built_key:
                            md_args.append(built_key[k])
                elif sub_key in built_key:
                    md_args.append(built_key[sub_key])
                built_key = md_args

        md5 = hashlib.md5()
        md5.update(json.dumps(built_key))
        lock_key = '{}:{}'.format(prefix, md5.hexdigest())
        try:
            with LockContext(
                    lock_key,
                    locker=global_locker,
                    lock_seconds=seconds,
                    retry_count=retry_count,
                    retry_delay=retry_delay):
                return func(*args, **kwargs)
        except LockFailedError:
            raise SMSError("{}。请稍后再试".format(raise_msg))

    return decorator(wrapper)


def build_one_file():
    pass


@cli.command()
@click.argument('mobile', type=click.STRING)
def yunpian_send_batch(mobile):
    from datetime import datetime
    from app.ext.helper import calc_count
    from bson import ObjectId
    from app.utils.record import record as record_utils
    from app.sender.yunpian import YunpianSender
    from app.sender.utils import choose_channel
    text = '【美折促销】没有大优惠，怎敢惊动您，全店满2件打8折，进店领取满300减20优惠券，活动仅限今天。回T退订'
    plan = {
        '_id': ObjectId(),
        'user_id': ObjectId('5ceb967f4f9fc9321a88ab59'),
        'schedule_t': datetime.now(),
    }
    record = record_utils.create_record_by_web_plan(plan, mobile, text,
                                                    calc_count(text))
    channel = next(choose_channel(2, 0))
    sender = YunpianSender(channel)
    sender.batch_send_by_records([record])


def tiaoshi():
    from app.models import db
    from bson import ObjectId
    from app.sender.yunpian import YunpianSender
    from app.sender.utils import choose_channel
    from app.sender.sender_manager import update_records_by_sending_result
    yunpian_data = {
        'total_count':
        1,
        'data': [{
            'count': 1,
            'msg': '发送成功',
            'fee': 0.05,
            'code': 0,
            'mobile': '15972096311',
            'sid': 1566278880596443,
            'unit': 'RMB'
        }],
        'total_fee':
        0.05,
        'unit':
        'RMB'
    }
    record = db.Record.collection.find_one({
        '_id':
        ObjectId('5d5b83e36fe836febdbd502d')
    })
    records = [record]
    channel = next(choose_channel(2, 0))
    sender = YunpianSender(channel)
    result = sender._format_response_by_records(records,
                                                yunpian_data.get('data'))
    update_records_by_sending_result(result, record['task_id'])


report = {
    'sid': 0,
    'status': 0,
    'mobile': 0,
    'code': 0,
    'desc': desc,
    'report_t': now,
}

yunpian_report = {
    'sid': 0,
    'uid': 0,
    'user_receive_time': now,
    'error_msg': '',
    'mobile': str,
    'report_status': str,
}


@cli.command()
def text_to_md():
    import re
    s = """
User 13946662101 recharges 1760.0, sent 6, cost 0.21, remain 1759.79
User mikui recharges 131.0, sent 1212, cost 42.42, remain 88.58
User jockeywind recharges 3.5, sent 2, cost 0.21, remain 3.29
User yijunjun recharges 2186.75, sent 59876, cost 2095.695, remain 91.055
User liujunwei13142 recharges 0.0, sent 0, cost 0.0, remain 0.0
User nbcower recharges 0.35, sent 1, cost 0.07, remain 0.28
User mztest1 recharges 5.0, sent 3, cost 0.105, remain 4.895
User mztest2 recharges 0.0, sent 0, cost 0.0, remain 0.0
User mztest276 recharges 0.0, sent 0, cost 0.0, remain 0.0
User mztest114 recharges 1.0, sent 12, cost 0.455, remain 0.545
User huiyonggong recharges 2000.28, sent 12094, cost 338.632, remain 1661.648
User tuanhaoke recharges 0.353, sent 6, cost 0.21, remain 0.143
User 343071396 recharges 0.0, sent 0, cost 0.0, remain 0.0
User test216 recharges 0.0, sent 0, cost 0.0, remain 0.0
User qingcheng recharges 2000.28, sent 30097, cost 842.716, remain 1157.564
User hvyosv recharges 0.56, sent 4, cost 0.112, remain 0.448
"""
    s2 = """
User meizhe recharges 21201.0, sent 576517, cost 20198.78, remain 1002.22
User hudong recharges 2100.0, sent 16243, cost 568.505, remain 1531.495
"""

    def make_md(sx):
        rlt = """
| 用户   | 充值     | 发送条数 | 花费金额 | 剩余金额 |
| ------ | -------- | -------- | -------- | -------- |
"""
        headers = ['用户', '充值', '发送条数', '花费金额', '剩余金额']
        lines = sx.split('\n')
        expr = r'User ([^\s]+).*recharges ([0-9]+).*sent ([0-9]+).*cost ([0-9.]+).*remain ([0-9.]+)'
        compiler = re.compile(expr)
        total = [0, 0, 0, 0]
        csv_lines = []
        for line in lines:
            if not line:
                continue
            print(line)
            data_match = compiler.match(line)
            if not data_match:
                print('errorrr with:')
                print(line)
                continue
            data = data_match.groups()
            csv_lines.append(data)
            to_num = lambda x: float(x) if '.' in x else int(x)
            total = [num + to_num(data[idx + 1]) for idx, num in enumerate(total)]
            rlt += '| ' + ' | '.join(data) + ' |\n'
        total = ['%.3f' % num for num in total]
        rlt += '| 总计 | ' + ' | '.join(total) + ' |\n'
        csv_lines.append(['总计'] + total)
        assert len(rlt.split('\n')) - 3 == len(lines)
        print(rlt)
        print(id(sx))
        save_csv_file(str(id(sx)) + '.csv', headers, csv_lines)

    def save_csv_file(file_name, headers, csv_lines, mode='w+'):
        import csv

        with open(file_name, mode) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(csv_lines)

    make_md(s)
    make_md(s2)


@cli.command()
def api_test():
    import json
    from app.ext.pdd_client import pdd_client
    from app.models.constants import PLAN
    access_token = '970ea1225053481cbf5694af3c9f06d8c3bc0d1e'
    res = pdd_client.ad_plan_delete({
        'access_token': access_token,
        'scene_type': PLAN.SCENE_TYPE.SEARCH_ADV,
        'plan_ids': json.dumps([21069414]),
    })
    print(res)


@cli.command()
def api_test():
    import json
    from app.ext.pdd_client import pdd_client
    from app.models.constants import PLAN
    access_token = '970ea1225053481cbf5694af3c9f06d8c3bc0d1e'
    res = pdd_client.call('pdd.ad.plan.max.cost.update', {
        'access_token': access_token,
        'scene_type': PLAN.SCENE_TYPE.SEARCH_ADV,
        'plan_id': 21397689,
        'max_cost': 5000000,
    })
    print(res)


class Update:
    from abc import abstractmethod
    def __init__(self, api, access_token):
        self.api = api
        self.access_token = access_token

    @abstractmethod
    def _build_params(self, *args, **kwargs):
        pass

    @abstractmethod
    def _check_success(self, res):
        pass

    @abstractmethod
    def _update_db(self, res, *args, **kwargs):
        pass

    @abstractmethod
    def _save_history(self, new_data):
        pass

    def run(self, *args, **kwargs):
        data = self._build_params(*args, **kwargs)
        res = getattr(pdd_client, self.api)(**data)
        if not self._check_success(res):
            raise PDDError(f'更新失败 {self.api} {args} {kwargs}')
        new_data = self._update_db(res, *args, **kwargs)
        self._save_history(new_data)


def test_api():
    import json
    from app.models.constants import PLAN
    client = PDDClient(
        config.PDD_CLIENT_ID,
        config.PDD_CLIENT_SECRET,
        config.PDD_API_GW
    )
    access_token = 'b8265260caf247c2929d30f005c1bb673ada458f'
    res = client.call('pdd.ad.keyword.create', {
        'access_token': access_token,
        'scene_type': PLAN.SCENE_TYPE.SEARCH_ADV,
        'unit_id': 80906689,
        'keywords': json.dumps([{
            'word': '生日礼物',
            'bid': 200,
        }]),
        # 'begin_date': '2020-01-15',
        # 'end_date': '2020-01-15',
    })
    print(res)


def test_orm():
    from datetime import datetime
    from bson import ObjectId
    from app.orm.account import plan_orm, unit_orm, keyword_orm, creative_orm
    from app.models.constants import PLAN, UNIT

    access_token = 'b8265260caf247c2929d30f005c1bb673ada458f'
    goods_id = 76163390719
    # plan = plan_orm.create_plan(access_token, '测试任务01')
    plan = {
        'last_update_t': datetime(2020, 1, 15, 15, 45, 59, 652832),
        'created_t': datetime(2020, 1, 15, 15, 45, 59, 652836),
        'unit_num': 0,
        'plan_id': 21528480,
        'plan_name': '测试任务01',
        'max_cost': 1000000000,
        'type': 0,
        '_id': ObjectId('5e1ec337fc615e42cca2e33e')
    }
    # print(plan)
    # plan = plan_orm.update_plan_max_cost(access_token, plan['plan_id'], 500000000)
    # print(plan)
    # plan = plan_orm.update_plan_operate_status(access_token, plan['plan_id'], PLAN.OPERATE_STATUS.PAUSED)
    # print(plan)
    # plan = plan_orm.update_plan_discounts(access_token, plan['plan_id'], [{'index':12, 'rate':1000}])
    # print(plan)

    # unit = unit_orm.create_unit(access_token, plan['plan_id'], goods_id, [{'bid': 200, 'word': '生日礼物蛋糕'}])
    # unit = {
    #     'unit_id': 81112171,
    #     'plan_id': 21528480,
    #     'keyword_count': 1,
    #     'goods_id': 76163390719,
    #     'status': 1,
    #     '_id': ObjectId('5e1ec83a587aa6884456ec56')
    # }
    # print(unit)
    # unit = unit_orm.update_unit_status(access_token, unit['unit_id'], UNIT.STATUS.PAUSED)
    # print(unit)

    # keyword = keyword_orm.create_keyword(access_token, unit['unit_id'], 200, '礼物蛋糕')
    keyword = {
        '_id': ObjectId('5e1ecad9f5489ebdb3f9872b'),
        'keyword_id': 1677297135,
        'bid': 200,
        'quality_score': 7,
        'status': 1,
        'unit_id': 81112171,
        'word': '礼物蛋糕'
    }
    # print(keyword)
    # keyword = keyword_orm.update_bid(access_token, keyword['keyword_id'], 400)
    # print(keyword)

    # creative = creative_orm.create_creative(access_token, unit['unit_id'], '手工匠心制作礼物蛋糕', 'https://t00img.yangkeduo.com/goods/images/2019-12-13/d35871d8-9787-4c10-bc80-761afeed9bc1.jpg')
    creative = {
        '_id': ObjectId('5e1ece23f5489ebdb3f98b86'),
        'creative_id': 124253125,
        'image_url':
        'https://t00img.yangkeduo.com/goods/images/2019-12-13/d35871d8-9787-4c10-bc80-761afeed9bc1.jpg',
        'operate_status': 1,
        'status': 4,
        'title': '手工匠心制作礼物蛋糕',
        'unit_id': 81112171
    }
    # print(creative)
    # creative = creative_orm.update_creative(access_token, creative['creative_id'], '全自动匠心制作礼物蛋糕', creative['image_url'])
    # print(creative)

    # creative = creative_orm.delete_creative(access_token, creative['creative_id'])
    # print(creative)

    # todo delete keyword
    # keyword = keyword_orm.delete_keyword(access_token, keyword['keyword_id'])
    # print(keyword)

    # todo delete unit
    # unit = unit_orm.delete_unit(access_token, unit['unit_id'])
    # print(unit)

    # todo delete plan
    plan = plan_orm.delete_plan(access_token, plan['plan_id'])
    print(plan)
