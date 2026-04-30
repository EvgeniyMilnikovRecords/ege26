with open(r'..\files\26_589.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]


prices = sorted(prices)
for i in range(0, max(prices), 500):
    group = [j for j in prices if i < j <= i + 500]
    sale_cnt = len(group) // 2
    sale = sum(group[:sale_cnt]) / 2
    max_sale = max(sale)