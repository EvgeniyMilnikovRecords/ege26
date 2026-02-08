# цикл while

# cnt = 0
# while cnt <= 5:
#     print('очередной шаг цикла')
#     cnt += 1

# найти сумму цифр через while

# num = int(input('введите число')
#           )
# summmm = 0
# while num != 0:
#     summmm += num % 10
#     num //= 10
# print(summmm)


# цикл for
# итерируемый объект - объект который состоит из других элементов
# str - состоят из символов.
# list,  tuple, set, dict  - содщержат в себе любые типы данных
# range(N) - последовательность целых чисел [0, N)
# range(M, N) - последовательность целых чисел [M, N)
# range(M, N, S) - последовательность целых чисел [M, N) c шагом S
# data = 'hello'
# for i in data:
#     print('символ -' , i)

# операторы
# break - остановка цикла
for i in range(10):
    print(i)
    if i == 5:
        break

# continue - переход к следующему шагу цикла

for i in range(10):
    print(i)
    if i % 2 == 0:
        continue
    print(i)

# else - позволяет выполнить блок кода еслицикл завершился добровольно

for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print('цикл завершился сам')
