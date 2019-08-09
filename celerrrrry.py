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
