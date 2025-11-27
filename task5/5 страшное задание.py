# 012345 python
# 123456 task
R = '101110'
cnt_chet = 0
for i in range(1, len(R), 2):
    if R[i] == '1':
        cnt_chet += 1
print(cnt_chet)
