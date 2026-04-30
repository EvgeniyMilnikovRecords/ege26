# from math import dist
#
# def center(cluster):
#     res = []
#     for dot in cluster:
#         sum_dist = sum(dist(dot, d) for d in cluster)
#
# with open(r'.\files\27_A_28766.txt') as file:
#     dots = []
#     stars = []
#     for i in file:
#         x, y, data = i.replace(',', '.').split()
#         dots.append(list(map(float, [x, y])))
#         if data[0] == 'Y' and data[2:] == 'III':
#             stars.append(list(map(float, [x, y])))
#
#
# cluster1 = [dot for dot in dots if dot[1] < 8]
# cluster2 = [dot for dot in dots if dot[1] > 8]
#
# clusters = [cluster1, cluster2]
#
# mincluster = min((center(clusters)), key = len)
# dists = [dist(mincluster, s) for s in stars]
#
# print(min(dists) * 10_000, max(dists) * 10_000)





from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)

with open(r'.\files\27_A_28766.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Z' and data[2:] == 'I':
            stars.append(list(map(float, [x, y])))

eps = 1

cluster1 = [d for d in dots if 23 < d[1]]
cluster2 = [d for d in dots if 16 < d[1] < 23]
cluster3 = [d for d in dots if 23 > d[1] < 16]


cluster11 = [d for d in dots if 23 < d[1]]
cluster22 = [d for d in dots if 16 < d[1] < 23]
cluster33 = [d for d in dots if 23 > d[1] < 16]

# Вывод длин (размеров) кластеров
print(len(cluster11))
print(len(cluster22))
print(len(cluster33))


center1 = center(cluster1)
center2 = center(cluster2)
center3 = center(cluster3)

b2 = dist(center2, center3)

b1 = []

for s in cluster11:
    for y in cluster11:
        if s != y:
            b1.append(dist)



