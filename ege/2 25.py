from fnmatch import fnmatch

for i in range(464907 - 464907 % 9117, 10**9, 9117):
    if fnmatch(str(i), '4*64*9?7'):
        print(i)