from ipaddress import *

ip_1 = ip_address('157.127.172.56')
ip_2 = ip_address('157.127.191.78')

for mask in range(16, 33):
    net1 = ip_network(f'{ip_1}/{mask}', False)
    net2 = ip_network(f'{ip_2}/{mask}', False)
    if net1.network_address != net2.network_address:
        print(mask)
        break
