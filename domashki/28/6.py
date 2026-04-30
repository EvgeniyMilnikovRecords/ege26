from turtle import *
tracer(0)
screensize(3000, 3000)
lt(90)
m = 15


rt(45)
for i in range(3):
    rt(45)
    fd(10 * m)
    rt(45)
rt(315)
fd(10 * m)
rt(90)
fd(20 * m)
rt(90)

for i in range(2):
    fd(10 * m)
    rt(90)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x *m, y * m)
        dot(3, 'red')

update()
done()

# ответ: 261