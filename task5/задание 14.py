for p in range(16, 37):
    num_1 =  int('17496', p)
    num_2 = int('91f83', p)
    num_3 = int('d9543', p)
    num = num_1 +num_2 +num_3

    if num%12 ==0:
        print(num//12)