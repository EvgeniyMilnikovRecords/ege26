# переменные и типы данных

# = - оператор присваивания
# переменнная

age = 57
print( 'мне',age)

# Нотации
# snake_case
client_name = 'антон'
client_age = 777

#camelCase

clientName = 'DZHO'
clientAge = 75

#PascalCase

ClientName = 'brooo'
ClientAge = 666

# Правила наименования переменных

# Только латинские символы
# Цифры но не на первом месте
# Знак нижнего подчеркивания _
client1 = 1
client2 = 2
#################
client_1 = 1
client_2 = 2

# Типы данных
# integer / int / целое число
my_int = 10
print(my_int, type(my_int))

# float /float / плавающее число

my_float = 10.5
print(my_float, type(my_float))

# string/ str/ строка

my_str1 = 'hello1'
my_str2 = "world2"
my_str3 = '"hello3"'
print(my_str1, type(my_str1))
print(my_str2, type(my_str2))
print(my_str3, type(my_str3))

# list / list / список

my_list = ['sasha', 20, 170.5]
print(my_list, type(my_list))
# У каждого элемента списка есть свой порядковый номер
# Нумерация элементов списка всегда начинается с нуля
print(my_list[0], type(my_list[0]))
print(my_list[1], type(my_list[1]))

# tuple / tuple / кортеж
my_tuple = (19, 'hello', 8.9)
print(my_tuple, type(my_tuple))
print(my_tuple[0], type(my_tuple[0]))

my_list[0] = 'neSasha'
print(my_list[0], type(my_list[0]))

# значения в тапле менять нельзя, а в листе можно

# set / set / множество
test = [1, 1, 1, 1]
print(test)
my_set = {1, 1, 1, 1}
print(my_set, type(my_set))

# dictionary / dict / словарь

my_dict = {'name':'egor', 'age':18, 'height':180}
print(my_dict['name'], type(my_dict))

#boolean / bool / логический тип данных

my_bool1  = True
my_bool2 = False
print(my_bool1, type(my_bool1))