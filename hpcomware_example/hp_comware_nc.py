from pyhpecw7.comware import HPCOM7
from pyhpecw7.features.vlan import Vlan
from pyhpecw7.features.interface import Interface
from getpass import getpass


ip = raw_input("Enter IP address")
device = HPCOM7(host=ip, username='admin', password=getpass())
print device.open()

vlan = Vlan(device, '1')
print vlan.get_config()
print vlan.get_vlan_list()

interface = Interface(device, 'FortyGigE1/0/50')
print interface.get_config()

#vlan = Vlan(device, '20')   # Add a new vlan
#vlan.build()                # Stage the Vlan
#device.execute()              # Execute the chagne
#vlan.build(name='NEWV20', descr='DESCR_20')
#device.execute()              # Execute the chagne
#vlan.remove()
#device.execute()

#interface.default()
#response = device.execute()
#interface.build(admin='down', description='TEST_DESCR')
#rsp = device.execute()

# cleanerase - Factory default
# config - manage comware configs
# file_copy
# install_os
# ipinterface
# irf
