#!/usr/bin/env python
from getpass import getpass
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pynxos.device import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

nexus_ip = "nxos1.twb-tech.com"
nxs_test = Device(host=nexus_ip, username="pyclass", password=getpass(),
                  transport='https', port=8443)

show_ver = nxs_test.show("show version")

memory = show_ver['memory']
proc_board_id = show_ver['proc_board_id']

print
print "Memory is: {}".format(memory)
print "Proc is: {}".format(proc_board_id)
print
