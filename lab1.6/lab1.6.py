import ipaddress
import re
import glob
from pprint import pprint


def ip_parse(ip_str):
    if re.search('ip address ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})$', ip_str):
        a = '/'.join(ip_str.split()[2:4])
        ip_obj = ipaddress.IPv4Interface(a)
        return ip_obj

file_list = glob.glob("C:\\av.krasavin\p4ne\lab1.6\config_files\*.log")
ip_list = set()
for file in file_list:
    with open(file) as f:
        for line in f:
            ip_ = ip_parse(line.strip())
            if ip_:
                ip_list.add(ip_)

pprint(ip_list)