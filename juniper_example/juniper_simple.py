from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

juniper_srx = { 
        "host": "184.105.247.76",
        "user": "pyclass",
        "password": getpass(),
    }   

a_device = Device(**juniper_srx)
a_device.open()
pprint(a_device.facts)

