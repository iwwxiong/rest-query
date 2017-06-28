#! /usr/bin/env python
# -*-coding: utf-8 -*-
__author__ = 'dracarysX'

import unittest
from rest_query.parser import BaseParamsParser


class BaseParamsParserTest(unittest.TestCase):
    """
    test case for BaseParamsParser class
    """
    @classmethod
    def setUpClass(cls):
        args = {
            'select': 'id,name,author{id,name,school{id,name}}',
            'id': 'gt.10', 
            'age': 'lte.25',
            'name': 'in.python, javascript',
            'order': 'id.desc',
            'page': 2,
            'limit': 5
        }
        cls.parser = BaseParamsParser(params_args=args)

    def test_parse_select(self):
        self.assertIn('id', self.parser.parse_select())
        self.assertIn('name', self.parser.parse_select())
        self.assertIn('author.id', self.parser.parse_select())
        self.assertIn('author.name', self.parser.parse_select())
        self.assertIn('author.school.id', self.parser.parse_select())
        self.assertIn('author.school.name', self.parser.parse_select())

    def test_parse_select_failure(self):
        parser = BaseParamsParser({})
        self.assertNotIn('id', parser.parse_select())
        parser = BaseParamsParser({'select': 'id{'})
        self.assertIn('id{', parser.parse_select())

    def test_parse_where(self):
        self.assertIn({'field': 'id', 'op': '>', 'value': '10'}, self.parser.parse_where())
        self.assertIn({'field': 'age', 'op': '<=', 'value': '25'}, self.parser.parse_where())
        self.assertIn({'field': 'name', 'op': 'in', 'value': ['python', 'javascript']}, self.parser.parse_where())

    def test_parse_where_failure(self):
        parser = BaseParamsParser({'age': 'gte.25'})
        self.assertNotIn('age >= 25', parser.parse_where())

    def test_parse_order(self):
        self.assertIn({'id': 'desc'}, self.parser.parse_order())

    def test_parse_order_failure(self):
        parser = BaseParamsParser({'order': 'xxx.abc'})
        self.assertNotEqual(parser.parse_order()[0]['xxx.abc'], 'ASC')

    def test_parse_paginate(self):
        self.assertDictEqual({'start': 5, 'end': 10, 'limit': 5, 'page': 2}, self.parser.parse_paginate())

    # def test_parse_paginate_failure(self):
    #     pass


if __name__ == '__main__':
    unittest.main()
