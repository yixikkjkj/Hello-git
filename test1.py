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
