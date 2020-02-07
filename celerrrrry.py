# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import time
from celery import Celery
broker = 'redis://localhost:6379/8'
backend = 'redis://localhost:6379/9'
app = Celery('my_task', broker=broker, backend=backend)


class Tiaoshi:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_ab(self):
        print(self.a, self.b)


def add(x, y):
    time.sleep(5)  # 模拟耗时操作
    return x + y


add = app.task(add)

if __name__ == "__main__":
    add.apply_async((3, 4), eta=datetime.now())

a = [
    'da5cd03588b14b368487c535cc2cd16d__0E8A02',
    'da5cd03588b14b368487c535cc2cd16d__D5357B',
    'da5cd03588b14b368487c535cc2cd16d__6CB36E',
    'da5cd03588b14b368487c535cc2cd16d__858E56',
    'da5cd03588b14b368487c535cc2cd16d__698B09',
    'da5cd03588b14b368487c535cc2cd16d__1165A1',
    'da5cd03588b14b368487c535cc2cd16d__DD624B',
    'da5cd03588b14b368487c535cc2cd16d__0E5457',
    'da5cd03588b14b368487c535cc2cd16d__169196',
    'da5cd03588b14b368487c535cc2cd16d__C589EB',
    'da5cd03588b14b368487c535cc2cd16d__78D858',
    'da5cd03588b14b368487c535cc2cd16d__3E910B',
    'da5cd03588b14b368487c535cc2cd16d__0B5708',
    'da5cd03588b14b368487c535cc2cd16d__B61B52',
    'da5cd03588b14b368487c535cc2cd16d__4FED00',
    'da5cd03588b14b368487c535cc2cd16d__328012',
    'da5cd03588b14b368487c535cc2cd16d__7366FB',
    'da5cd03588b14b368487c535cc2cd16d__D9A030',
]
astr = ' or '.join(['\'%s\'' % s for s in a])
