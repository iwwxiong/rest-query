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
> parse.parse_select()
['author.school.*', 'author.id', 'author.name', 'id', 'name']
> parse.parse_where()
[
    {'field': 'id', 'value': '20', 'op': '>='}, 
    {'field': 'author.id', 'value': [10, 20, 30, 40, 50], 'op': 'in'}
]
> parse.parse_order()
[{'id': 'desc'}]
> parse.parse_paginate()
{'start': 0, 'end': 5, 'limit': 5, 'page': 1}
```

## License

MIT

## Contacts

Email: huiquanxiong@gmail.com
