ans =[]
for n in range(1, 100000):
    r = bin(n)[2:]
    if r.count('0') % 2 == 0:
        r = '1' + r + '1'
    else:
        r += '10'
    r = int(r , 2)
    if r < 100:
        ans.append(r)

print(max(ans))