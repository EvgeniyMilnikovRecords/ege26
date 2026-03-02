from fnmatch import fnmatch

def sost(num):
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return True
    return False

sost_nums = []
for N in range(4, 10_000):
    if sost(N):
        sost_nums += [N]

for i in range(22768, 10 ** 8 + 1, 22768):
    for N in sost_nums:
        if fnmatch(str(i), f'1{N}03*6*'):
            print(i, N)
