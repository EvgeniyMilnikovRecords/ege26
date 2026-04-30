from math import dist


def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot , d) for d in cluster)
    res.append([sum_dist, dot])
    return min(res[1])

with open(r'.\files\27_A_21599.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]





cluster1 = [d for d in dots if d[1] < -7]
cluster2 = [d for d in dots if -7 < d[1] < 11/14 * d[0] - 11]
cluster3 = [d for d in dots if d[1] > 11/14 * d[0] - 11]

center1 = center(cluster1)
center2 = center(cluster2)
center3 = center(cluster3)

