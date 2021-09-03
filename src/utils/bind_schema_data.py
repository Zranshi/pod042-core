# -*- coding: UTF-8 -*-
# @Time     : 2021/09/03 18:34
# @Author   : Ranshi
# @File     : bind_schema_data.py
# @Doc      : 将验证后的参数绑定到orm对象上


from typing import Set


def bind(empty_obj, target_obj, ignore: Set[str]) -> object:
    for attr in target_obj:
        if hasattr(empty_obj, attr[0]) and attr[0] not in ignore:
            setattr(empty_obj, attr[0], attr[1])
    return empty_obj
