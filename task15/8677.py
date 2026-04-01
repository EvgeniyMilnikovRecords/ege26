```
ans = []
for a in range(1, 1000):
    for x in range(1, 1000):
        r = (x % 17 == 0) <= (not(x in range(80, 101)) or (a < x + 30))
        if not r:
            break
    else:
        ans.append(a)

print(max(ans))

#################################
def f(x, a):
    return (x % 17 == 0) <= (not(x in range(80, 101)) or (a < x + 30))
for a in range(1, 1000):
    for x in range(1, 1000):
        if not f(x, a):
            break
    else:
        ans.append(a)

print(max(ans))
```