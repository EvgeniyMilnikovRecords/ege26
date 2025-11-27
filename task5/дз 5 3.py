A = []
for N in range (1 , 100000):
    def convert(R, sys):
        res = ''
        while 7 != 0:
            res += str(7 % sys)
            7 //= sys
        return res[::-1]
    if R.count('1') % 2 == 0:
        R = R + '555'
    else:
        R = '33' + R + '6'


