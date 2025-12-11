from itertools import product

alph = sorted('сублимаця')
alph_1 = set('уиая')
for pos,val in enumerate(product(alph, repeat = 5), start=1):
    val = ''.join(val)
    if val[-1] != 'я' and pos % 2 == 1:
        cnt_1 = sum(1 for i in val if i in alph_1)
    if cnt_1 == 2:
            print(max(cnt_1, pos))


#58955



#Функция set() в Python создает множество (set) — неупорядоченную коллекцию,
# которая хранит только уникальные элементы, автоматически удаляя дубликаты