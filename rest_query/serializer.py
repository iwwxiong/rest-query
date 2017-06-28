#! /usr/bin/env python
# -*-coding: utf-8 -*-
__author__ = 'dracarysX'


class BaseSerializer(object):
    """
    base serializer
    """
    def __init__(self, obj=None, object_list=None, select_args=None):
        self.obj = obj
        self.object_list = object_list
        self.select_args = select_args

    def obj_serializer(self, obj):
        """
        serializer for obj without select args
        """
        raise NotImplementedError()

    def serializer(self, obj):
        """
        single obj serializer.
        """
        raise NotImplementedError()

    def data(self):
        """
        serializer
        :return: {json object}
        """
        if self.obj is not None:
            return self.serializer(obj=self.obj)
        return [self.serializer(obj=obj) for obj in self.object_list]
