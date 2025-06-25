import requests
from pprint import pprint
import urllib3



urllib3.disable_warnings()

headers = {
    "accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

host_url = 'https://10.31.70.209'
r = requests.get(host_url + '/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces', auth=("restapi", "j0sg1280-7@"), headers=headers, verify=False)

intf_list = r.json()['Cisco-IOS-XE-interfaces-oper:interfaces']['interface']
list_ = []
for intf in intf_list:
    list_.append('interface {}\n packets input: {}\n packets output: {}\n bytes input: {}\n bytes output: {}\n'.format
                 (intf['name'],
                  intf['statistics']['in-octets'],
                  intf['statistics']['out-octets'],
                  intf['statistics']['in-unicast-pkts'],
                  intf['statistics']['out-unicast-pkts']))

pprint(list_)