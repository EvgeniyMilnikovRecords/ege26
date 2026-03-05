def DIG(x, y):
    return str(x)[0] == str(y)[0]

def f(x, a):
    left_side = (not DIG(x, 28)) and DIG(x, 47)
    right_side = x > a - 20
    return left_side <= right_side

for a in range(1, 1000)[::-1]:
    if all(f(x, a) for x in range(1, 1000)):
        print(a)
        break