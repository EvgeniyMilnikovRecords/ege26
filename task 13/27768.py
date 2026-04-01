from ipaddress import *
cnt = 0
net = ip_network('172.16.160.0/255.255.240.0')
for ip in net:
    ip = f'{int(ip):032b}'
    if ip.count('1') % 2 == 0:
        cnt += 1

print(cnt)