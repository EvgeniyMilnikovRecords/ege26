from itertools import product

alph = sorted('дионсй')
cnt = 0
for pos , val in enumerate(product(alph, repeat = 6), start = 1):
    if 'д' in val and 'н' not in val or 'н' in val and 'д' not in val :
        cnt += 1
        print(cnt)
