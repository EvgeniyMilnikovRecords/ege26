with open(r'.\files\26_4660.txt') as file:
    N = int(file.readline())
    prods = [int(i) for i in file]

prods = sorted(prods)
sale_amount = N
print(N)
one_check = sum(prods) - sum(prods[:sale_amount]) // 2
many_checks = sum(prods) - sum(prods[::-1][3::4]) // 2

print(one_check, many_checks)