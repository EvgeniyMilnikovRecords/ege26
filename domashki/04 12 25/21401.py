#print('w x y z')
#for w in range(2):
    #for x in 0, 1:
        #for y in 0, 1:
            #for z in 0, 1:
                #f = x and (z <= w) and not y
                #if f:
#                   print(w, x, y, z)

from itertools import product, permutations
def f(w, x, y, z):
    return x and (z <= w) and not y

for i in product((0, 1), repeat =4):
    table = [
        (1, i[0], 1, i[1]),
        (0, 1, i[2], 0),
        (i[3], 1, 1, 0)
    ]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,t))) for t in table] == [1, 1, 1]:
                print(*p, sep = '')





# Порядок выполнения операций в алгебре логики
# 1. Отрицание / Инверсия (¬A, (not A))
# 2. Логическое умножение / Конъюнкция (A∧B, A∙B, A and B)
# 3. Логическое сложение / Дизъюнкция (A∨B, A+B, A or B)
# 4. Следование / Импликация (A→B, A <= B)
# 5. Тождество / Эквивалентность (A≡B, A == B)

