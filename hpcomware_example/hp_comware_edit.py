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
                        
    xml_data = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <top xmlns="http://www.hp.com/netconf/config:1.0">
        <Device>
          <Base>
            <HostName>5900</HostName>
          </Base>
        </Device>
    </top>
</config>"""

    my_conn.edit_config(target="running", config=xml_data, default_operation="merge")
