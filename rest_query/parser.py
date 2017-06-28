#! /usr/bin/env python
# -*-coding: utf-8 -*-
__author__ = 'dracarysX'

import re
from collections import deque
from .operator import Operator, operator_list

ASC = 'asc'
DESC = 'desc'


def cache_property(key=None):
    def decorator(func):
        def wrapper(cls, *args, **kwargs):
            _key = key if key is not None else '_{}'.format(func.__name__)
            if hasattr(cls, _key):
                return getattr(cls, _key)
            result = getattr(cls, func.__name__)(*args, **kwargs)
            setattr(cls, _key, result)
            return result
        return wrapper
    return decorator


class ParserException(Exception):
    pass
        

class BaseParamsParser(object):
    """
    base params parser for select, where, order, paginate
    """
    select_flag = 'select'
    order_flag = 'order'
    page_flag = 'page'
    limit_flag = 'limit'
    select_format = '{}.{}'
    exclude_where = [select_flag, order_flag, page_flag, limit_flag]
    default_limit = 10
    operator_engine = Operator
    default_direction = ASC
    direction_list = [ASC, DESC]
    operator_list = operator_list

    def __init__(self, params_args=None, **kwargs):
        self.params_args = params_args
        
    def _embed_args_split(self, value):
        """
        >>> _embed_args_split('id,name,author{id,name,school{id,name}}')
        ['id', 'name', author{id,name,school{id,name}}']
        """
        regex = re.compile(r'\w+\{.*?\}+')
        embed = regex.findall(value)
        embed.extend(filter(None, ''.join(regex.split(value)).split(',')))
        return embed

    def split_select(self):
        """
        split select args
        >>> split_select('id,name,author{id,name,school{id,name}}')
        ['id', 'name', 'author.id', 'author.name', 'author.school.id', 'author.school.name']
        """
        def _select(_select_params, _select_args, k=None):
            r = re.compile(r'^(?P<key>\w+)\{(?P<value>.+)\}$')
            for index, param in enumerate(_select_args):
                if r.search(param):
                    key, value = r.search(param).groups()
                    if k is not None:
                        key = self.select_format.format(k, key)
                    if value.find(',') == -1:
                        _select_params.append(self.select_format.format(key, value))
                    else:
                        _select(_select_params, self._embed_args_split(value), k=key)
                else:
                    if k is not None:
                        param = self.select_format.format(k, param)
                    _select_params.append(param)

        select_params = []
        _select(select_params, self._embed_args_split(self.select_args))
        return select_params

    def parse_select(self):
        self.select_args = self.params_args.get(self.select_flag, '')
        return self.split_select()

    def split_where(self):
        _wheres = []
        for field, values in self.where_args.items():
            _value = values.split('.')
            operator, value = _value[0], '.'.join(_value[1:])
            if operator not in self.operator_list:
                _wheres.append(self.operator_engine(field, values).eq())
            else:
                _wheres.append(getattr(self.operator_engine(field, value), operator)())
        return _wheres

    def parse_where(self):
        self.where_args = {
            key: value for key, value in self.params_args.items() if key not in self.exclude_where
        }
        return self.split_where()

    def split_order(self):
        _order = []
        if self.order_args is None:
            return []
        for order in self.order_args.split(','):
            keys = order.split('.')
            field, direction = keys[:-1], keys[-1]
            if direction not in self.direction_list:
                field = keys
            _order.append({
                '.'.join(field): self.default_direction if direction not in self.direction_list else direction.lower()
            })
        return _order

    def parse_order(self):
        """
        >>> parse_order()
        {'author.id', 'desc'}
        """
        self.order_args = self.params_args.get(self.order_flag, None)
        return self.split_order()

    def parse_paginate(self):
        try:
            page = int(self.params_args.get(self.page_flag, 1))
            limit = int(
                self.params_args[self.limit_flag] if self.limit_flag in self.params_args else self.default_limit
            )
        except:
            raise ParserException('Param page or limit must be integer.')
        return {
            'page': page,
            'limit': limit,
            'start': (page - 1) * limit,
            'end': page * limit
        }
