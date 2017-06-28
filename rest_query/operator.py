#! /usr/bin/env python
# -*-coding: utf-8 -*-

__author__ = 'dracarysX'


operator_list = ['eq', 'neq', 'gt', 'gte', 'lt', 'lte', 'like', 'ilike', 'in', 'between']


class OperatorException(Exception):
    pass


class Operator(object):
    """
    """
    def __init__(self, field_name, value, **kwargs):
        self.field_name = field_name
        self.value = value

    def __getattribute__(self, value, *args, **kwargs):
        if value == 'in':
            return super(Operator, self).__getattribute__('iin', *args, **kwargs)
        return super(Operator, self).__getattribute__(value, *args, **kwargs)

    def format(self, op, value=None):
        return {
            'field': self.field_name,
            'op': op,
            'value': value or self.value
        }

    def eq(self):
        """
        x equals y
        """
        return self.format('=')

    def neq(self):
        """
        x is not equal to y
        """
        return self.format('!=')

    def gt(self):
        """
        x is greater than y
        """
        return self.format('>')

    def gte(self):
        """
        x is greater than or equal to y
        """
        return self.format('>=')

    def lt(self):
        """
        x is less than y
        """
        return self.format('<')

    def lte(self):
        """
        x is less than or equal to y
        """
        return self.format('<=')

    def like(self):
        """
        x LIKE y where y may contain wildcards
        """
        return self.format('like')

    def ilike(self):
        """
        x ILIKE y where y may contain wildcards
        """
        return self.format('ilike')

    def _split_value(self):
        value = []
        for i in self.value.split(','):
            try:
                value.append(int(i))
            except ValueError:
                value.append(i.strip())
        return value

    def iin(self):
        """
        x IN y, where y is a list or query
        """
        return self.format('in', value=self._split_value())

    def between(self):
        """
        x between y where y is a array
        """
        return self.format('between', value=self._split_value())
