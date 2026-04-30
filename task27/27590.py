# from math import dist
#
#
# def center(cluster):
#     res = []
#     for dot in cluster:
#         sum_dist = [sum(dist(dot,d) for d in cluster)]
#         res.append([sum_dist, dot])
#     return max(res)[1]
#
#
# with open(r'.\files\27A_27590.txt') as file:
#     dots = [list(map(float, i.replace(',', '.').split())) for i in file]
#
#
# eps = 1
#
# clusters = []
#
# while dots:
#     cluster = [dots.pop()]
#     for dot in cluster:
#         for d in dots.copy():
#             if dist(dot, d) < eps:
#                 cluster.append(d)
#                 dots.remove(d)
#     clusters.append(cluster)
#
# centers = [[len(cluster), center(cluster)] for cluster in clusters]
#
#
# print(centers)
# maxcluster = max(centers)
# mincluster = min(centers)
#
# print((mincluster[1][0] + mincluster[1][1]) * 10_000)
# print((maxcluster[1][0] + maxcluster[1][1]) * 10_000)

'#############################################################3'


from math import dist


def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = [sum(dist(dot,d) for d in cluster)]
        res.append([sum_dist, dot])
    return max(res)[1]


with open(r'.\files\27B_27590.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]


eps = 1

clusters = []

while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 1:
        clusters.append(cluster)

centers = [[(center(cluster)[1] ** 2 + center(cluster)[0] ** 2)** .5, center(cluster)] for cluster in clusters]



maxcluster = max(centers)
mincluster = min(centers)

print((maxcluster[1][0]) * 10_000)
print((mincluster[1][1]) * 10_000)



