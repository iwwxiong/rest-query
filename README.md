# Rest-query

A parser for rest query request. like no-sql select style.(/?select=id,name,author{*}&id=gte.20&order=id.desc).

## Installing

    > pip install rest-query

## Test

    > python setup.py test

## Usage

```python
> from rest_query import BaseParamsParser
> args = {
        'select': 'id,name,author{id,name,school{*}}',
        'id': 'gte.20',
        'author.id': 'in.10,20,30,40,50',
        'order': 'id.desc',
        'page': 1,
        'limit': 5
    }
> parser = BaseParamsParser(params_args=args)
> parser.parse_select()
['author.school.*', 'author.id', 'author.name', 'id', 'name']
> parser.parse_where()
[
    {'field': 'id', 'value': '20', 'op': '>='}, 
    {'field': 'author.id', 'value': [10, 20, 30, 40, 50], 'op': 'in'}
]
> parser.parse_order()
[{'id': 'desc'}]
> parser.parse_paginate()
{'start': 0, 'end': 5, 'limit': 5, 'page': 1}
```

## Where operator

just implement operators: `=`, `gt`, `gte`, `lt`, `lte`, `like`, `ilike`, `in`, `between`.

## Support

now we can use [Django ORM](https://github.com/dracarysX/django-rest-query), [Peewee](https://github.com/dracarysX/peewee-rest-query).

## License

MIT

## Contacts

Email: huiquanxiong@gmail.com
