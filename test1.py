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
                        print i
                    print '---' * 30
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
