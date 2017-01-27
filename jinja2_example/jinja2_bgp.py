import jinja2

bgp_template = """
router bgp 10
  neighbor {{ peer_ip }} remote-as {{ remote_as }}
    address-family ipv4 unicast 

"""

my_vars = {
    'remote_as': '100',
    'peer_ip': '10.10.10.2',
}

t = jinja2.Template(bgp_template)
print t.render(my_vars)
