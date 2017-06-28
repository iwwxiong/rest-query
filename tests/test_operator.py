#! /usr/bin/env python
# -*-coding: utf-8 -*-
__author__ = 'dracarysX'

import unittest
from rest_query.operator import Operator


class OperatorTest(unittest.TestCase):
    """
    test case for Operator class
    """
    @classmethod
    def setUpClass(cls):
        cls.operator = Operator('age', 25)
        
    def test_eq(self):
        self.assertDictEqual(self.operator.eq(), {'field': 'age', 'op': '=', 'value': 25})

    def test_neq(self):
        self.assertDictEqual(self.operator.neq(), {'field': 'age', 'op': '!=', 'value': 25})
        
    def test_gt(self):
        self.assertDictEqual(self.operator.gt(), {'field': 'age', 'op': '>', 'value': 25})
        
    def test_gte(self):
        self.assertDictEqual(self.operator.gte(), {'field': 'age', 'op': '>=', 'value': 25})
        
    def test_lt(self):
        self.assertDictEqual(self.operator.lt(), {'field': 'age', 'op': '<', 'value': 25})
        
    def test_lte(self):
        self.assertDictEqual(self.operator.lte(), {'field': 'age', 'op': '<=', 'value': 25})
        
    def test_like(self):
        self.assertDictEqual(self.operator.like(), {'field': 'age', 'op': 'like', 'value': 25})
        
    def test_ilike(self):
        self.assertDictEqual(self.operator.ilike(), {'field': 'age', 'op': 'ilike', 'value': 25})
        
    def test_iin(self):
        operator = Operator('age', '25,30')
        self.assertDictEqual(operator.iin(), {'field': 'age', 'op': 'in', 'value': [25, 30]})

    def test_in(self):
        operator = Operator('age', '25,30')
        self.assertDictEqual(operator.iin(), {'field': 'age', 'op': 'in', 'value': [25, 30]})
    
    def test_between(self):
        operator = Operator('age', '25,30')
        self.assertDictEqual(operator.between(), {'field': 'age', 'op': 'between', 'value': [25, 30]})


if __name__ == '__main__':
    unittest.main()
