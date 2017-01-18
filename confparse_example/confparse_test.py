#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse

if __name__ == "__main__":
    cisco_file = 'cisco_config.txt'

    cisco_cfg = CiscoConfParse(cisco_file)
    intf_obj = cisco_cfg.find_objects(r"^interf")
    for intf in intf_obj:
        print
        print intf.text
        for child in intf.children:
            print child.text
        break
    print
