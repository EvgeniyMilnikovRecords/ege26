def convert(num, sys): # 150, 5
    while num: # 150
        res = '0'
        while num != 0:
            res += str(num % sys)#150
            num = num // sys # 30
        return res[::-1]

def convert (num , sus):
    res = ''
    while num != 0:
        res += str(num % sus)
        num //= sus
    return res[::-1]