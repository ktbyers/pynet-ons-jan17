import jinja2

f = open("pynet_rtr1.txt")
my_template = f.read()

my_vars = {
    'ip_addr': '10.10.12.2',
    'netmask': '255.255.255.0',
}

t = jinja2.Template(my_template)
print t.render(my_vars)
