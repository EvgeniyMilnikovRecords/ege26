with open(r'..\files\24_15339.txt') as file:
    data = file.readline()

data = 'a2b2m2c6c766'

ans = 0
cnt = 1
for i in range(len(data) - 1):
    if data[i] in '6789' and data[i+1] in 'ABC' or data[i] in 'ABC' and data[i+1] in '6789':
        cnt +=1
    else:
        cnt = 1
    ans = max(ans, cnt)
print(ans)
