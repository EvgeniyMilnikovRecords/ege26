from ipaddress import *

ip1 = '157.127.182.76'
ip2 = '157.127.190.80'

for mask in range(16, 31):
    net = ip_network(f'{ip1}/{mask}', strict = False)
    if ip1 in net.hosts() and ip2 not in net.hosts():
        print(mask)
        break

