from string import printable as alph
ans = []
for x in alph[:22]:
    num_1 = int(f'27{x}98876' , 26)
    num_2 = int(f'26{x}51', 26)
    num_3 = int(f'15{x}47', 26)
    num_4 = int(f'62{x}5', 26)
    num = num_1 + num_2 +num_3 +num_4
    if num % 25 == 0:
        print(x , num //25)

