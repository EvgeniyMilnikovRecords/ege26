from ipaddress import *
net = ip_network('192.168.64.176/255.255.255.240', strict= False)
cnt = 0
for ip in net:
    ip = f'{int(ip):032b}'
    if ip.count('1') % 2 != 0:
        cnt += 1

print(cnt)