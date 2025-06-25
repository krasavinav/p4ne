from flask import Flask
import re
import glob
from pprint import pprint
import ipaddress


info = ["Здравствуйте! Hello",
        'При обращении по “/” — выдаёт краткую справку об использовании',
        'При обращении по “/configs” — выдаёт сведения об именах всех хостов, для которых есть кофигурационные файлы (см. работу 1.6)',
        'При обращении по “/config/hostname” выдает сведения о всех IP-адресах этого хоста']

app = Flask(__name__)


def parse(file):
    a = {}
    hostname = None
    ip_addr = []
    with open(file) as f:
        for line in f:
            if re.search('^hostname |^sysname', line.strip()):
                hostname = line.split()[1]
            elif re.search('^ip address ',line.strip()) and hostname:
                ip_addr.append(ipaddress.IPv4Interface('/'.join(line.split()[2:4])))
        a[hostname] = ip_addr
    return a


@app.route('/')
def index():
    return info


@app.route('/configs')
def configs():
    s =''
    a = main_dict.keys()
    for i in a:
        s += str(i) +'\n'
    return s

@app.route('/configs/<hostname>')
def configs1(hostname):
    return

if __name__ =='__main__':
    file_list = glob.glob("C:\\av.krasavin\p4ne\lab1.6\config_files\*.log")
    main_dict = dict()
    for file in file_list:
        file_dict = parse(file)
        if file_dict:
            main_dict.update(file_dict)
    pprint(main_dict)


    app.run(debug=True)