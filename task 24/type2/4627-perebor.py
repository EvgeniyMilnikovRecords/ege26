with open(r'..\files\24_4627.txt') as file:
    data = file.readline()

with open(r'..\files\24_4627.txt') as file:
    data = file.readline().strip()

ans = 0

for sdvig in range(3):
    cnt = 0

    for i in range(sdvig, len(data) - 2, 3):
        triplet = data[i:i + 3]

        if triplet == 'PNO' or triplet == 'NPO':
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0

print(ans)
