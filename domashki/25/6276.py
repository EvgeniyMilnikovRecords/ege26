from fnmatch import fnmatch

# Определяем старт (ровно 10101011 или чуть больше, но кратное 2023)
start = 10101011
if start % 2023 != 0:
    start += (2023 - start % 2023)

for i in range(start, 10 ** 10, 2023):
    s = str(i)

    if fnmatch(s, '1?1?1?1*1'):
        suma = sum(int(d) for d in s)

        if suma == 22:
            print(i)
