with open(r'.\files\26_17687.txt') as file:
    prices = [int(i) for i in file]
    n = int(file.readline())

prices = sorted(prices, reverse = True)

real_price_customer = sum(prices) - sum(prices[:n // 9])
luck_price_customer = sum(prices) - sum(prices[9 - 1::9])