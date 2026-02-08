from random import randint

randnum = randint(0, 100)
print(randnum)
if randnum % 3 == 0:
    print(randnum//3)
else:
    print(randnum * 2 )
