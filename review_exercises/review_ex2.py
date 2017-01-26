#!/usr/bin/env python
my_dict = {
    'key1': 'whatever',
    'ip_addr': '1.1.1.1',
    'key2': 'something',
    'key3': 'else'
}

my_dict['ip_addr'] = '10.20.30.222'

for k, v in my_dict.items():
    print k, v
