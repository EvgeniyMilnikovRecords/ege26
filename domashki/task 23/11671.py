points = set()

def f(start, cnt):
    if cnt == 15:
        points.add(start)
        return True
    return f(start + 10, cnt + 1) + f(start - 5, cnt + 1)

f(1, 0)

print(len(points))

