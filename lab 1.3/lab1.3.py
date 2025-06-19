from pysnmp.hlapi import *
from pprint import pprint

result = getCmd(SnmpEngine(),
	CommunityData('public', mpModel=0),
	UdpTransportTarget(('10.31.70.209', 161)),
	ContextData(),
	ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

result2 = nextCmd(SnmpEngine(),
	CommunityData('public', mpModel=0),
	UdpTransportTarget(('10.31.70.209', 161)),
	ContextData(),
	ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
	lexicographicMode=False)

# snmp_object = ObjectIdentity('1.3.6.1.2.1.2.2.1.2') # По значению MIB-переменной
# snmp_object = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0) # По имени MIB-переменной

for x in result:
	for y in x[3]:
		print(y)

for x in result2:
	for y in x[3]:
		print(str(y).split(' ')[2])