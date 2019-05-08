# coding: utf-8

from bson import ObjectId
from datetime import datetime
from app.actions.plan import create_plan

user = {
    'balance': 1000,
    '_id': ObjectId('1234567890ab1234567890ab'),
}

data = {
    'user_id': ObjectId('1234567890ab1234567890ab'),
    'name': 'test plan for airu',
    'text': 'show me the map',
    'mobiles': [15972096311],
    'schedule_t': datetime(2099, 12, 12),
    'plan_type': 1,
}

create_plan(user, data)

from app.actions.plan import get_plans

get_plans()

from bson import ObjectId
from app.actions.plan import get_details

get_details(plan_id=ObjectId('5cd00d32f22cd93a1d319e95'))
