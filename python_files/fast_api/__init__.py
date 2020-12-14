import pydantic

from enum import Enum
from typing import List


class TransText:
    _default_text = '未知'

    def __new__(cls):
        kv = {}
        text = {}
        cls_dict = dict(vars(TransText))
        cls_dict.pop('__new__')
        for key, val in vars(cls).items():
            if key.isupper() and isinstance(val, tuple):
                kv[key] = val[0]
                text[val[0]] = val[1]
            else:
                cls_dict[key] = val

        cls_dict['_kv'] = kv
        cls_dict['_text'] = text
        return type(cls.__name__, (), cls_dict)()

    def __getattr__(self, item):
        return self._kv.get(item, -1)

    def items(self):
        return self._kv

    def keys(self):
        return list(self._kv.keys())

    def values(self):
        return list(self._kv.values())

    def trans(self, key):
        return self._text.get(key, self._default_text)

    def trans_items(self, items, key, trans_key=None):
        if not trans_key:
            trans_key = 'view_' + key

        if isinstance(items, list):
            for item in items:
                item[trans_key] = self.trans(item.get(key, ''))
        else:
            items[trans_key] = self.trans(items.get(key, ''))
        return items


class Plan:
    class SceneType(TransText):
        _default_text = '未知类型'
        SEARCH_ADV = 0x00, '搜索广告'
        STAR = 0x01, '明星店铺'
        TARGET_ADV = 0x02, '定向广告'
        BANNER_ADV = 0x03, '首页 Banner 广告'
    SCENE_TYPE = SceneType()


PLAN = Plan()


class TestModlld(pydantic.BaseModel):
    scene_type: Literal[PLAN.SCENE_TYPE.values()]
