import time

import pickle
import yajl
import json
import copy

try:
    import cjson
except ImportError:
    cjson = None
try:
    import simplejson
except ImportError:
    simplejson = None
try:
    import ujson
except ImportError:
    ujson = None

default_data = {
    "name": "Foo",
    "type": "Bar",
    "count": 1,
    "info": {
        "x": 203,
        "y": 102,
    },
}

datas = []


def init_data(x=10 * 10000):
    for i in range(x):
        tmp = copy.deepcopy(default_data)
        tmp['count'] = i
        datas.append(tmp)


def ttt(f, data=None, times=10):
    start = time.time()
    for _ in range(times):
        f(data)
    return time.time() - start


def profile(serial, deserial, data=None):
    if not data:
        data = datas
    squashed = serial(data)
    return (ttt(serial, data), ttt(deserial, squashed))


def test(serial, deserial, data=None):
    if not data:
        data = datas
    assert deserial(serial(data)) == data


contenders = [
    ('stdlib json', (json.dumps, json.loads)),
    ('pickle', (pickle.dumps, pickle.loads)),
]
if cjson:
    contenders.append(('cjson', (cjson.encode, cjson.decode)))
if simplejson:
    contenders.append(('simplejson', (simplejson.dumps, simplejson.loads)))
if ujson:
    contenders.append(('ujson', (ujson.dumps, ujson.loads)))
if yajl:
    contenders.append(('yajl', (yajl.Encoder().encode, yajl.Decoder().decode)))

if __name__ == "__main__":
    init_data()
    for name, args in contenders:
        test(*args)
        x, y = profile(*args)
        print("%-11s serialize: %0.3f  deserialize: %0.3f  total: %0.3f" %
              (name, x, y, x + y))
