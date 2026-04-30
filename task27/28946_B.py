from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_B_28946.txt') as file:
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
# print(centers)


cl = [len(cluster) for cluster in clusters]
# print(cl)


small_cluster = clusters[1]
small_center = center(small_cluster)

xc = small_center[0]
yc = small_center[1]

b1 = 0
for dot in small_cluster:
    if abs(dot[0] - xc) < 0.9 and abs(dot[1] - yc) < 0.9:
        b1 += 1

big_cl = clusters[0]
med_cl = clusters[2]

big_cen = center(big_cl)
med_cen = center(med_cl)

print(b1)
print(abs(big_cen[1] - med_cen[1]) * 10_000)

# print(small_cluster[0])