from turtle import *
tracer(0)
screensize(3000, 3000)
m = 2

for n in range(2):
    for i in range(2):
        fd(180 * m)
        rt(120)
    rt(120)

rt(150)
fd(15 * m)
rt(90)
fd(360 * m)
rt(90)
fd(15 * m)
rt(30)
fd(74 * m)

up()

for x in range(-100, 100):
    for y in range(-100,  100):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()
