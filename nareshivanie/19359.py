from string import printable

for x in printable[1:22]:
    num1 = int(f'a23{x}ac0', 22)
    num2 = int(f'gb{x}21670', 22)
    z = num1 + num2
    if z %21 == 0:
