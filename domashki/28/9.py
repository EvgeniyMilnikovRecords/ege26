with open(r'.\files\task9.txt') as file:
    line = [sorted(list(map(int, i.split()))) for i in file]
cnt = 0
for i in line:
    if i[3] < i[0] + i[1] + i[2]:
        if i[0] + i[3] != i[1] + i[2]:
            cnt += 1
print(cnt)
# ответ: 2354


