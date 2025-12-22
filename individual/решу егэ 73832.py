from turtle import *
screensize(3000, 3000)
tracer (0)
m = 8
lt(90)

for i in range(2):
    fd(15 *m )
    rt(90)
    fd(8 * m)
    rt(90)
up()
from turtle import *
screensize(3000, 3000)
tracer (0)
m = 8
down()
for n in range(2):
    fd(15 *m )
    rt(90)
    fd(8 * m)
    rt(90)

for x in range(-30, 50):
    for y in range(-50, 30):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()
