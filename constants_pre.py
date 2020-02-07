class TransTextMeta(type):

    def __new__(meta, name, bases, cls_dict):
        print('showme this meta')
        print(cls_dict)
        kv = {}
        text = {}
        keys = []
        for key, val in cls_dict.items():
            if key.isupper() and isinstance(val, tuple):
                kv[key] = val[0]
                text[val[0]] = val[1]
                keys.append(key)

        cls_dict['_kv'] = kv
        cls_dict['_text'] = text
        for key in keys:
            print('meta pop', key)
            cls_dict.pop(key)

        print(cls_dict)
        # cls_dict['__getattr__'] = meta.__getattr__
        # cls_dict['keys'] = meta.keys
        # cls_dict['values'] = meta.values
        # cls_dict['trans'] = meta.trans
        # cls_dict['trans_items'] = meta.trans_items
        return type(name, bases, cls_dict)

    # def __getattr__(self, item):
    #     return self._kv.get(item, -1)

    # def keys(self):
    #     return list(self._kv.keys())

    # def values(self):
    #     return list(self._kv.values())

    # def trans(self, key):
    #     return self._text.get(key, self._default_text)

    # def trans_items(self, items, key, trans_key=None):
    #     if not trans_key:
    #         trans_key = 'view_' + key

    #     if isinstance(items, list):
    #         for item in items:
    #             item[trans_key] = self.trans(item.get(key, ''))
    #     else:
    #         items[trans_key] = self.trans(items.get(key, ''))
    #     return items


class TransText:
    _default_text = '未知'

    def __new__(cls, *args, **kwargs):
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
        return type(cls.__name__, (), cls_dict)(*args, **kwargs)

    def __getattr__(self, item):
        return self._kv.get(item, -1)

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


class PlanType(TransText):
    _default_text = '不知道'
    ADV = 0, '搜索'


if __name__ == "__main__":
    a = PlanType(1, 2, 3, 4)
    print(a)
    print(a.keys())
    print(a.ADV)
    print(a.trans(a.XXXX))
    print(a.XXXX)
