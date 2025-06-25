# import json
# import sys
#
# dict1 = {'value1': 8192,
#          'value2': 950,
#          'value3': 7911}
# print(dict1['value2'])
#
# s = json.dumps(sys.path)
# d2 = json.loads(s)
# print(type(d2))
# print(type(s)


import paramiko
import time
from requests import session

# ssh_conn = paramiko.SSHClient()
# ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# ssh_conn.connect("10.31.70.209", username='restapi', password='j0sg1280-7@', look_for_keys=False, allow_agent=False)
# session = ssh_conn.invoke_shell()

# session.send("\n\n\n\n")
# time.sleep(2)
# session.send("\nterminal length 0\n\n\n")
# time.sleep(2)
# session.send("\n\nshow run\n\n")
# time.sleep(2)
# buf = session.recv(150000)
# print(buf.decode())

import requests
from pprint import pprint

headers = {
    "accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

# host_url = 'https://10.31.70.209'
# r = requests.get('https://10.31.70.209/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces', auth=("restapi", "j0sg1280-7@"), headers=headers)
r = requests.get('https://yandex.ru')
pprint(r.url)
pprint(r.headers)
pprint(r.content)
