import paramiko
import time
import re
from pprint import pprint
from requests import session

def ip_parse(ip_str):
    if re.search('^GigabitEthernet[0-9]|^Loopback[0-9]', ip_str):
        return ip_str.split()[0]
    elif re.search('\w+ packets input, \w+ bytes', ip_str):
        return ' '.join(ip_str.split(',')[0:2])
    elif re.search('\w+ packets output, \w+ bytes', ip_str):
        return ' '.join(ip_str.split(',')[0:2])


# Создаем объект — соединение по ssh
ssh_conn = paramiko.SSHClient()
ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy)

# Инициируем соединение по ssh
ssh_conn.connect("10.31.70.209", username='restapi', password='j0sg1280-7@', look_for_keys=False, allow_agent=False)
session = ssh_conn.invoke_shell()


session.send("\n")
time.sleep(2)
session.send("\nterminal length 0\n\n\n")
session.send("\n\nshow interface\n\n")
time.sleep(2)
buf = session.recv(150000)
# print(buf.decode())

list_config = list(buf.decode().split('\n'))
list_parse = []
for line in list_config:
    intf = ip_parse(line.strip())
    if intf:
        list_parse.append(intf)
pprint(list_parse)
# pprint(list_config)
session.close()