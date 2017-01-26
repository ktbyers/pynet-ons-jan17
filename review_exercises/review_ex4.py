#!/usr/bin/env python
from pprint import pprint

output = """Internet  10.220.88.1            59   0062.ec29.70fe  ARPA   FastEthernet4
Internet  10.220.88.20            -   c89c.1dea.0eb6  ARPA   FastEthernet4
Internet  10.220.88.21          196   1c6a.7aaf.576c  ARPA   FastEthernet4
Internet  10.220.88.28          216   5254.aba8.9aea  ARPA   FastEthernet4
Internet  10.220.88.29          194   5254.abbe.5b7b  ARPA   FastEthernet4
Internet  10.220.88.30          181   5254.ab71.e119  ARPA   FastEthernet4
Internet  10.220.88.32          190   5254.abc7.26aa  ARPA   FastEthernet4
Internet  10.220.88.37          182   0001.00ff.0001  ARPA   FastEthernet4
Internet  10.220.88.38            8   0002.00ff.0001  ARPA   FastEthernet4
Internet  10.220.88.40           96   001c.c4bf.826a  ARPA   FastEthernet4
Internet  10.220.88.41           33   001b.7873.5634  ARPA   FastEthernet4  """

ip_dict = {}
for line in output.splitlines():
    fields = line.split()
    ip_addr = fields[1]
    mac = fields[3]
    ip_dict[ip_addr] = mac

print
pprint(ip_dict)
print
