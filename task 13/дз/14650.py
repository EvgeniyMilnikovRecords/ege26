from ipaddress import *

ip1 = ip_address('216.54.187.235')
ip2 = ip_address('216.54.174.128')

for mask in range(16, 31):
    # Убираем слова 'address:' и 'strict:', это подсказки PyCharm, а не часть кода
    net1 = ip_network(f'{ip1}/{mask}', strict=False)
    net2 = ip_network(f'{ip2}/{mask}', strict=False)

    # Исправляем net1.hosts() и net2.hosts() — это методы, нужны скобки
    # net1[0] — это и есть адрес сети
    if net1[0] != net2[0] and ip1 in net1.hosts() and ip2 in net2.hosts():
        print(mask)
