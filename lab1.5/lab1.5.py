import glob
from pprint import pprint

file_list = glob.glob("*.log")
ip_list = set()
for file in file_list:
    with open(file) as f:
        for line in f:
            if line.strip().startswith('ip address'):
                line = ' '.join(line.split()[2:4])
                ip_list.add(line)

pprint(sorted(ip_list))
