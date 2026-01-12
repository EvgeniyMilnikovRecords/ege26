for x in range(10, 70001):


    num = 5**2025 + 5**400 - x

cnt_4 = 0

while num != 0:
    num.count('4')
    cnt_4 += 1
print(cnt_4)