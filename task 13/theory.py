# библиотека для работы с ip-адресами
from ipaddress import *
# конвертирует текст в объект ip-address
ip_address('192.0.0.5')

# формирует все ip-адреса по заданной сети и маске
net = ip_network('192.0.0.5/255.255.255.254', strict = False)

print(*net)