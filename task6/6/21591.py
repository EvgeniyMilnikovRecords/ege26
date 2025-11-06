from turtle import *

screensize(3000,3000)
tracer (0)
m=10

rt(270)
for i in range(2):
    fd(8 * m)
    rt(120)

rt(120)

for i in range(2):
    rt(120)
    fd(3 * m)
    rt (240)

rt(240)

for i in range(2):
        fd(14 * m)
        rt (120)

up()
for x in range(-35, 50):
    for y in range(-10,70):
        goto(x * m, y * m)
        dot(3, 'red')
update()
done()

#97


