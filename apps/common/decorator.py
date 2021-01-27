# -*- coding: utf-8 -*-
#
from django.db import transaction


def on_transaction_commit(func):
    """
    如果不调用on_commit, 对象创建时添加多对多字段值失败
    """
    def inner(*args, **kwargs):
        transaction.on_commit(lambda: func(*args, **kwargs))
    return inner


def singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton
