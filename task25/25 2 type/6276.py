from fnmatch import fnmatch

for n in range(2023, 10**10, 2023):
    if fnmatch(str(n), '1?1?1?1*1'):
        if sum(map(int, str(n))) == 22:
            print(n)

