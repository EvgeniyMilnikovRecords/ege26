from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_A_28946.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 1
clusters = []

while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots:
            if dist(dot, d) < 1:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 6:
        clusters.append(cluster)

centers = []
for i in clusters:
    c = center(i)
    centers.append(c)
print(centers)


if len(clusters[0]) > len(clusters[1]):
    big_cluster = clusters[0]
    small_cluster = clusters[1]
else:
    big_cluster = clusters[1]
    small_cluster = clusters[0]


a2 = abs(centers[0][0] - centers[1][0])

big_center = center(big_cluster)

a1 = 0
for dot in big_cluster:
    if dot[1] < big_center[1]:
        a1 += 1

print(a1, a2 * 10_000)
