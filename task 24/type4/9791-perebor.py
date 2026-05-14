from string import printable

with open(r'..\files\24_9791.txt') as file:
    data = file.readline().lower()

ans = cnt = 0
for i in data:
    if i in printable[:16]:
        cnt += 1
    else:
        cnt = 0
    ans = max(ans, cnt)

print(ans)
