#! /usr/bin/env python
# -*-coding: utf-8 -*-
__author__ = 'dracarysX'

"""
Orm extra function
"""


class ModelExtra(object):
    """
    model extra mixin
    """
    field_map = {}
    join_model = {}

    def push_join_model(self, field, model):
        """
        push join model into set
        """
        self.join_model[field] = model

    def is_foreign(self, field):
        """
        check field is ForeignKey
        """
        if self.foreign_key is not None and isinstance(field, self.foreign_key):
            self.push_join_model(field, self.foreign_model(field))
            return True
        return False

    def foreign_model(self, field):
        """
        get foreign key field related model class
        """
        raise NotImplementedError()

    def is_field_exist(self, model, field_name):
        """
        is field exist in model
        """
        raise NotImplementedError()

    def field_by_model(self, model, field_name):
        """
        """
        raise NotImplementedError()

    def check_field_exist(self, field_name):
        """
        check field name exist in model
        """
        if field_name in self.field_map:
            return True
        field_names = field_name.split('.')
        if len(field_names) == 1:
            if self.is_field_exist(self.model, field_name):
                # cache field
                self.field_map[field_name] = self.field_by_model(self.model, field_name)
                return True
            return False
        model = self.model
        for _field_name in field_names[:-1]:
            if not self.is_field_exist(model, _field_name):
                return False
            field = self.field_by_model(model, _field_name)
            if not self.is_foreign(field):
                return False
            model = self.foreign_model(field)
        if self.is_field_exist(model, field_names[-1]):
            # cache field
            self.field_map[field_name] = self.field_by_model(model, field_names[-1])
            return True
        return False

    def get_field(self, field_name):
        """
        get field instance with field_name from cache
        """
        return self.field_map[field_name]
