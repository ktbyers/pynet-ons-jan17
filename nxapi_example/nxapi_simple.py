#!/usr/bin/env python
from pprint import pprint
from getpass import getpass
from pynxos.device import Device

nexus_ip = "nxos1.twb-tech.com"
nxs_test = Device(host=nexus_ip, username="pyclass", password=getpass(),
                  transport='https', port=8443)

my_facts = nxs_test.facts
pprint(nxs_test.facts)
