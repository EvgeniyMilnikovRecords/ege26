def func(num):
    for i in range(17, num//2+1, 10):
        if num % i == 0:
            return i
    return 0

k=0
for i in range(700000, 7000000):
    flag = func(i)
    if flag:
        print(i, func(i))
        k+=1
        if k==5:
            break