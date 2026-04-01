with open(r'./files/26_4684.txt') as file:
    n = int(file.readline())
    prods = [int(i) for i in file]

sale_amount = n // 6
prods = sorted(prods)

one_check = sum(prods) - sum(prods[:sale_amount]) // 2
many_checks = sum(prods) - sum(prods[::-1][5::6]) // 2



