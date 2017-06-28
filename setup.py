#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys


class MyTest(TestCommand):
    def run_tests(self):
        tests = unittest.TestLoader().discover('tests', pattern='test_*.py')
        unittest.TextTestRunner(verbosity=1).run(tests)


setup(
    name='rest-query',
    version='0.1.0',
    license='MIT',
    description='A parser for rest query request. like no-sql select style',
    author='dracarysX',
    author_email='huiquanxiong@gmail.com',
    url='https://github.com/dracarysX/rest-query',
    packages=find_packages(include=['rest_query']),
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Framework :: rest-query',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: MIT',
    ],
    keywords='rest, query, no-sql, parser',
    long_description='A parser for rest query request. like no-sql select style.'
                     '(/?select=id,name,author{*}&id=gte.20&order=id.desc).'
)
