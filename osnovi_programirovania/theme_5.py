# input - считывает данные с клавиатуры
# help - выдает краткую справку

#num = int(input())

# data = input() # тип строка
# #
# # print('this is ny data -', data)

# условный оператор


num = int(input())

if num > 0:
    print('+')
elif num <0:
    print('-')
else:
    print('0')

# сложные условия
# if понимает только 2 значение - True  или False

num2 = int(input())
num3 = int(input())

if num2 >0 and num3 != 0:
    print('zhopa')