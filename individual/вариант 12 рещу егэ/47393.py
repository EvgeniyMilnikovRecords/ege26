from turtle import *
m = 70

screensize(3000, 3000)
tracer(0)

for i in range(6):
    rt(36)
    fd(10 * m)
    rt(36)

up()

for x in range(-70, 69):
    for y in range(-70, 70):
        goto(x*m, y * m)
        dot(3, 'red')

update()
done()