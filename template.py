
import hashlib
import json
import time

import requests

API_KEY = '5daedb8d061173241101e734'  # 子账号的 api_key
SECRET_KEY = '0yzR8dWThN'  # 子账号的 secret_key
POST_URL = 'https://www.meixinduanxin.com'

def gen_sign(data):
    v = '|'.join(["{}={}".format(k, v) for k, v in sorted(data.items())])
    str_to_sign = "{}_{}".format(v, SECRET_KEY)
    print(str_to_sign)
    sign = hashlib.md5(str_to_sign.encode()).hexdigest()
    return sign


def handle_send_result(result):
    print(result)
    print(result.json())


def batch_send_by_template(mobiles, template_id, params):
    """
        mobiles: 手机号码列表，如 ['15972096311', '15972096312']
        template_id: 模版id，如 '5dbfbc9c940bb98484125783'
        params: 模版参数，如 {'code': 123456}
    """
    data = {
        'api_key': API_KEY,
        'template_id': template_id,
        'mobiles': ','.join(mobiles),
        'params': json.dumps(params).replace(' ', ''),
    }
    data['ts'] = int(time.time())
    data['sign'] = gen_sign(data)
    rlt = requests.post(POST_URL + '/api/sender/template_batch_send', json=data)
    handle_send_result(rlt)


if __name__ == "__main__":
    POST_URL = 'http://127.0.0.1:8010'
    m = ['15972096311']
    t = '5dc27e67ad2809fd53f83a25'
    p = {'code': 123456}
    batch_send_by_template(m, t, p)
