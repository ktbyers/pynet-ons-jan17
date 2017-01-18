import telnetlib
import time
from getpass import getpass
TELNET_PORT = 23
TELNET_TIMEOUT = 6

password = getpass()
remote_conn = telnetlib.Telnet('184.105.247.70', TELNET_PORT, TELNET_TIMEOUT)
output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
remote_conn.write('pyclass\n')
output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
remote_conn.write(password + '\n')

remote_conn.write('show ip int brief\n')
time.sleep(1)
print remote_conn.read_very_eager()
