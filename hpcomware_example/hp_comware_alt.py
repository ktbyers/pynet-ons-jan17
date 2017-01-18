from ncclient import manager
from getpass import getpass
from lxml import etree

def xml_print(xml_str):
    root = etree.fromstring(str(xml_str))
    print etree.tostring(root, pretty_print=True)

if __name__ == "__main__":
    ip_addr = raw_input("Enter IP address: ")
    my_conn = manager.connect(host=ip_addr, port=830, username='admin', 
                          password=getpass(), device_params={'name': 'hpcomware'}, 
                          hostkey_verify=False, allow_agent=False, look_for_keys=False,
                          timeout=30)
                        
    output = my_conn.cli_display("display ip interface brief")
    xml_print(output)
    raw_input("Hit enter to continue: ")

    print my_conn.client_capabilities
    for capability in my_conn.client_capabilities:
        print capability
    raw_input("Hit enter to continue: ")

    output = my_conn.get()
    xml_print(output)
    raw_input("Hit enter to continue: ")

