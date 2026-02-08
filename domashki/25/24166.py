def get_prime_factors(n):
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    return factors


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


count = 0
num = 7305678 + 1

while count < 5:
    factors = get_prime_factors(num)

    # Условие: ровно 4 простых множителя
    if len(factors) == 4:
        sum_f = sum(factors)
        # Условие: сумма множителей — палиндром
        if is_palindrome(sum_f):
            print(num, sum_f)
            count += 1

    num += 1
