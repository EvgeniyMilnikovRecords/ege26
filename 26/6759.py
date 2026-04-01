with open(r'.\files\26_6759.txt') as file:
    n = int(file.readline())
    prods = [int(i) for i in file]

prods = [10, 20, 30, 40 ,50]
prods = sorted(prods)
sale_amount = n // 3

chel_real = sum(prods) - sum(prods[::-1][2::3])
chel_minn= sum(prods) - sum(prods[-sale_amount:])

print(chel_minn, chel_real)
