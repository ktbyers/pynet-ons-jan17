"""
Based on https://github.com/bigswitch/sample-scripts/
"""
import json
import requests
requests.packages.urllib3.disable_warnings()

controller_ip = "1.1.1.1"
controller_url = "https://{}:8443".format(controller_ip)

#### debug rest
#### show version

##################################
# Login 
# First you must obtain an authentication cookie from the controller, we 
# therefore define the login path
##################################
path = "/api/v1/auth/login"
url = controller_url + path

data = '{"user": "admin", "password": "bsn123"}'
headers = {"content-type": "application/json"}

# POST request made on the Big Cloud Fabric controller
response = requests.request('POST', url, data=data, headers=headers, verify=False) 
print "Authentication response\n", response.content, "\n\n"

# Extract the cookie from the response and create a session cookie string to be
# used in subsequent requests
cookie = json.loads(response.content)['session_cookie']
session_cookie = 'session_cookie=%s' % cookie


##################################
# Show Switch
##################################
path = '/api/v1/data/controller/applications/bcf/info/fabric/switch'
url = controller_url + path

data = ''
headers = {"content-type": "application/json", 'Cookie': session_cookie}
response = requests.request('GET', url, data=data, headers=headers, verify=False)
print "show switch response\n", response.content


##################################
# Logout 
##################################
path = '/api/v1/data/controller/core/aaa/session[auth-token="'+cookie+'"]'
url = controller_url + path
headers = {"content-type": "application/json", 'Cookie': session_cookie}
# DELETE request made on the Big Cloud Fabric controller
response = requests.request('DELETE', url, headers=headers, verify=False)



#cookie = ""
#controller_url = ""
#
#def bcf_login(IP, username, password):
#    global cookie
#    global controller_url
#    controller_url = "https://%s:8443" % IP
#    url = controller_url + "/api/v1/auth/login"
#    data = '{"user":"%s", "password":"%s"}' % (username, password)
#    headers = {"content-type": "application/json"}
#    r = requests.post(url, data=data, headers=headers, verify=False)
#    cookie =  json.loads(r.content)['session_cookie']
#    
#def send_rest(action, url, data):
#    global cookie
#    session_cookie = 'session_cookie=%s' % cookie
#    headers = {'Cookie': session_cookie, "content-type": "application/json"}
#    url = controller_url + "/api/v1/data/controller/applications/bcf/" + url
#    r = requests.put(url, data=data, headers=headers, verify=False)
#    return r.status_code
#        
#def configure_tenant(name) :
#    url = 'tenant[name="%s"]' % name
#    data = '{"name": "%s"}' % name
#    send_rest('PUT', url, data)
#    
#def configure_segment(name, segment, vlan, ip) :
#    url = 'tenant[name="%s"]/segment[name="%s"]' % (name, segment)
#    data = '{"name": "%s"}' % segment
#    send_rest('PUT', url, data)
#    
#    url = 'tenant[name="%s"]/segment[name="%s"]/port-group-membership-rule[vlan=%s][port-group="any"]' % (name, segment, vlan)
#    data = '{"vlan": %s, "port-group": "any"}' % (vlan)
#    send_rest('PUT', url, data)
#
#    url = 'tenant[name="%s"]/logical-router/segment-interface[segment="%s"]' % (name, segment)
#    data = '{"segment": "%s"}' % segment
#    send_rest('PUT', url, data)
#
#    url = 'tenant[name="%s"]/logical-router/segment-interface[segment="%s"]/ip-subnet' % (name, segment)
#    data = '{"ip-cidr": "%s", "private": false}' %ip
#    send_rest('PUT', url, data)   
# 
#    print "Configured segment %s successfully" % segment
#
#
#bcf_login ('10.2.18.11', 'admin', 'bsn123') 
#
#configure_tenant ('red')
#configure_segment ('red', 'web', 211, '211.0.1.1/24')
#configure_segment ('red', 'app', 212, '212.0.1.1/24')
#configure_segment ('red', 'db', 213, '213.0.1.1/24')

#def add_port_group(name):
#    method = 'PUT'
#    path = '/api/v1/data/controller/applications/bcf/port-group[name="%s"]' % name
#    data = '{"name": "%s"}' % name
#    controller_request(method, path, data=data)
#
#def add_interface_to_port_group(switch, interface, port_group):
#    method = 'PUT'
#    path = '/api/v1/data/controller/applications/bcf/port-group[name="%s"]/member-interface[switch-name="%s"][interface-name="%s"]' % (port_group, switch, interface)
#    data = '{"switch-name": "%s", "interface-name": "%s"}' % (switch, interface)
#    controller_request(method, path, data=data)
#    
#def add_tenant(name):
#    method = 'PUT'
#    path = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]' % name
#    data = '{"name": "%s"}' % name
#    controller_request(method, path, data=data)
#                                                            
#def add_port_group_to_segment(port_group, segment, tenant, vlan='-1'):
#    method = 'PUT'
#    path = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/segment[name="%s"]/port-group-membership-rule[vlan=%s][port-group="%s"]' %(tenant, segment, vlan, port_group)
#    data = '{"vlan": %s, "port-group": "%s"}' %(vlan, port_group)
#    controller_request(method, path, data=data)
#    
#def add_segment(name, port_groups, tenant, vlan='-1'):
#    method = 'PUT'
#    path = '/api/v1/data/controller/applications/bcf/tenant[name="%s"]/segment[name="%s"]' %(tenant, name)
#    data = '{"name": "%s"}' % name
#    controller_request(method, path, data=data)
#    if port_groups:
#        for port_group in port_groups:
#            add_port_group_to_segment(port_group, name, tenant, vlan=vlan)
#
#def add_port_groups(port_groups):
#    """ add each port_group in list of port_groups using the function add_port_group """
#    for port_group in port_groups:
#        add_port_group(port_group)
#
#def add_interfaces_to_port_group(interfaces, port_group):
#    """ add each (switch, interface) pair in interfaces to port-group port_group  """
#    for (switch, interface) in interfaces:
#        add_interface_to_port_group(switch, interface, port_group)
