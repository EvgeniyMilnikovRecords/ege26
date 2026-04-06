from ipaddress import *

net = ip_network('172.45.12.200/255.255.240.0', strict=False)

# Находит широковещательный адрес (самый большой в этой сети)
print(net.broadcast_address - 1, sep='')