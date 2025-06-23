import ipaddress
import random
from pprint import pprint

class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        ipaddress.IPv4Network.__init__(self,
                                       ((random.randint(0X0B000000, 0XDF000000), random.randint(8,24))),
                                       strict=False)
    def regular(self):
        return self.is_global

def value_ip(n):
    print(n.netmask)
    print(int(n.netmask)*2**32)
    print(int(n.network_address))
    return int(n.netmask)*2**32 + int(n.network_address)


network_list =[]
while len(network_list) != 2:
    net = IPv4RandomNetwork()
    if net.is_global:
        network_list.append(net)

for i in sorted(network_list, key=value_ip):
    print(str(i))
