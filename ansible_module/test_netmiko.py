

from ansible.module_utils.basic import AnsibleModule
from netmiko import ConnectHandler

def main():
    module = AnsibleModule(
        argument_spec = dict(
            device_type = dict(type='str', required=True),
            hostname=dict(type='str', required=True),
            username=dict(type='str', required=True),
            password=dict(type='str', required=True, no_log=True),
            cmd=dict(type='str', required=True)
        )
    )

    hostname = module.params['hostname']
    username = module.params['username']
    password = module.params['password']
    device_type = module.params['device_type']
    cmd = module.params['cmd']

    new_conn = ConnectHandler(ip=hostname, username=username, password=password,
                              device_type=device_type)
    output = new_conn.send_command(cmd)

    module.exit_json(changed=True, something_else=output)
#    module.fail_json(msg="Something fatal happened")

if __name__ == "__main__":
    main()
