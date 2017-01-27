#!/usr/bin/env python
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
from getpass import getpass
from pynxos.device import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#nexus_ip = "34.195.147.241"
nexus_ip = "nxos1.twb-tech.com" 
nxs_test = Device(host=nexus_ip, username="pyclass", 
                  password=getpass(),
                  transport='https', port=8443)

#### FACTS
print "\nFacts"
print '-' * 50
pprint(nxs_test.facts)
raw_input("\n\nHit a key to continue: ")

###### SHOW
print "\nShow hostname"
print '-' * 50
print nxs_test.show("show hostname")
print '-' * 50
raw_input("\n\nHit a key to continue: ")

###### SHOW RAW TEXT
print "\nShow raw text: "
print '-' * 20 + " Raw Text " + '-' * 20
print nxs_test.show("show ip arp vrf management", raw_text=True)
print '-' * 50
raw_input("\n\nHit a key to continue: ")

###### SHOW STRUCTURED DATA
print "\nShow structured data: "
print '-' * 20 + " Structured " + '-' * 20
pprint(nxs_test.show("show ip arp vrf management", raw_text=False))
print '-' * 50
raw_input("\n\nHit a key to continue: ")

##### CONFIG
print "\nConfig"
print '-' * 50
nxs_test.config("hostname test123")
print nxs_test.show("show hostname")
print '-' * 50
raw_input("\n\nHit a key to continue: ")

print "\nRestore Config"
print '-' * 50
nxs_test.config("hostname nxos1")
print nxs_test.show("show hostname")
print '-' * 50
raw_input("\n\nHit a key to continue: ")

##### RUN-CONFIG
print "\nRun"
print '-' * 50
run_config = nxs_test.running_config
print run_config
print '-' * 50
raw_input("\n\nHit a key to continue: ")

# pynxos methods
#'backup_running_config', 
#'checkpoint', 
#'config', 
#'config_list', 
#'facts', 
#'feature', 
#'file_copy', 
#'file_copy_remote_exists', 
#'get_boot_options', 
#'reboot', 
#'rollback', 
#'running_config', 
#'save', 
#'set_boot_options', 
#'show', 
#'show_list'
