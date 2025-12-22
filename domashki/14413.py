from itertools import permutations
cnt = 0

for val in set(permutations('сортировка')):
    val = ''.join(val)
    for i in 'оиа':
        val = val.replace(i, '*')
    for i in 'стрвк':
        val = val.replace(i, '#')
    if '***' not in val and '###' not in val:
        cnt += 1
print(cnt)

#185760