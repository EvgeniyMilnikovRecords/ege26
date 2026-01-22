from string import printable as alph


a = []
for x in alph[:25]:
    num_1 = int(f'11353{x}12', 25)
    num_2 = int(f'135{x}21', 25)
    num = num_1 + num_2
    if num %24 == 0:
        a.append(num)

print(max(a))

#6389996328