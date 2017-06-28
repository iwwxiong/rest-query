#! /usr/bin/env python
# -*-coding: utf-8 -*-

__author__ = 'dracarysX'

from .parser import BaseParamsParser


class QueryBuilder(object):
    """
    base query builder
    """
    parser_engine = BaseParamsParser

    def __init__(self, model, params, **kwargs):
        self.model = model
        self.params = params
        self.parser = self.parser_engine(self.params, model=self.model)
        self.select = self.parser.parse_select()
        self.where = self.parser.parse_where()
        self.order = self.parser.parse_order()
        self.paginate = self.parser.parse_paginate()

    def build(self):
        raise NotImplementedError()
