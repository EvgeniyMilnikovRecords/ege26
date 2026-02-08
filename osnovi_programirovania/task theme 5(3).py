cell1 = input('введите стартовую клетку: ')
cell2 = input('введите конечную клетку: ')

print(cell1, cell2)

cond1 = abs(int(cell1[1]) - int(cell2[1]))== 2 and abs(ord(cell1[0]) - ord(cell2[0])) == 1
cond2 =  abs(int(cell1[1]) - int(cell2[1]))== 1 and abs(ord(cell1[0]) - ord(cell2[0])) == 2

if cond1 or cond2:
    print('yyyyeeeeeeeeeeeeesss')
else:
    print('nnnnooooooooooooooaaaaaaaaaaahhhhhhhhhh')


