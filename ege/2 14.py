from string import printable as alph
for x in range(1, 13):
    num1 = int(f'2AB{x}', 12)
    num2 = int(f'{x}8E', 17)
    num = num1 + num2
    if num % 27 == 0:
        print(num // 27)
