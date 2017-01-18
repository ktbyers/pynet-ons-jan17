#!/usr/bin/env python
import json

my_dict = {'ntp_server1': '1.1.1.1'}
print "'{}'".format(json.dumps(my_dict))
#print json.dumps(my_dict)

