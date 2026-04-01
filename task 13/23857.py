from ipaddress import *

net = ip_network('192.168.12.207/255.192.0.0', strict = False)
for ip in net:
    ip = f'{int(ip):032b}'
    if ip.count('1') == ip.count('0'):
        print(ip)
