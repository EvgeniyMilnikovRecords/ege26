```
with open(r'.\files\1962.txt') as file:
    data = [list(map(int, i.split())) for i in file]


cnt = 0

for pos, tri in enumerate(data, start = 1):
    tri = sorted(tri)
    if tri[0] + tri[1] > tri[2]:
        cnt += 1



print(cnt)
```