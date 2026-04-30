from ipaddress import *

ip = ip_address('45.172.106.203')

net = ip_network(f'{ip}/255.255.252.0', False)

print(net.broadcast_address - 1)
