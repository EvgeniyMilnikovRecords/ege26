def convert(num , sus):
    res = ''
    while num != 0:
        res = res + str(num % sus)
        num = num // sus
        return res[::-1]



num = 16**820 - 2**761 +14

print(convert(num , 4))

#################

num = 16**820 - 2**761 +14
cnt_0 = 0
while num:
    if num % 4 == 0:
        cnt_0 += 1
    cnt_0 //= 5

print(cnt_0)