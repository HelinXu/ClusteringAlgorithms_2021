import numpy as np
import matplotlib.pyplot as plt
import time
import scipy.io as io
import operator
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform


# function update(N, p, Seeds, eps, MinPts) is
#     coredist = core-distance(p, eps, MinPts)
#     for each o in N
#         if o is not processed then
#             new-reach-dist = max(coredist, dist(p,o))
#             if o.reachability-distance == UNDEFINED then // o is not in Seeds
#                 o.reachability-distance = new-reach-dist
#                 Seeds.insert(o, new-reach-dist)
#             else               // o in Seeds, check for improvement
#                 if new-reach-dist < o.reachability-distance then
#                     o.reachability-distance = new-reach-dist
#                     Seeds.move-up(o, new-reach-dist)
def update(seeds, idx, neighbours, d_cores, d_reach, distance, processed):
    d_core = d_cores[idx]
    for n in neighbours:
        if (processed[n] == 0):
            tmp = max(d_core, distance[idx][n])
            if np.isnan(d_reach[n]):
                d_reach[n] = tmp
                seeds[n] = tmp
            elif (tmp < d_reach[n]):
                d_reach[n] = tmp
                seeds[n] = tmp
    return seeds


# function OPTICS(DB, eps, MinPts) is
#     for each point p of DB do
#         p.reachability-distance = UNDEFINED
#     for each unprocessed point p of DB do
#         N = getNeighbors(p, eps)
#         mark p as processed
#         output p to the ordered list
#         if core-distance(p, eps, MinPts) != UNDEFINED then
#             Seeds = empty priority queue
#             update(N, p, Seeds, eps, MinPts)
#             for each next q in Seeds do
#                 N' = getNeighbors(q, eps)
#                 mark q as processed
#                 output q to the ordered list
#                 if core-distance(q, eps, MinPts) != UNDEFINED do
#                     update(N', q, Seeds, eps, MinPts)
def OPTICS(data, epsilon, minPts):
    distance_matrix = squareform(pdist(data, metric='euclidean'))
    print(distance_matrix) #对称矩阵
    # print(distance_matrix.shape)
    bounderies = np.argsort(distance_matrix)[:, minPts - 1]
    N = data.shape[0]  # 共N个数据点
    temp_core_dists = distance_matrix[np.arange(0, N), bounderies]
    core_dists = np.where(temp_core_dists <= epsilon, temp_core_dists, -1)
    core_idx = np.where(core_dists > 0)[0]
    d_reach = np.array([np.nan for i in range(N)])
    processed = np.array([0 for i in range(N)])

    sortedlist = []
    #     for each unprocessed point p of DB do
    for idx in core_idx:
        if not processed[idx]:
            processed[idx] = 1
            sortedlist.append(idx)
            #         N = getNeighbors(p, eps)
            nbhd = np.where((distance_matrix[:, idx] <= epsilon) & (distance_matrix[:, idx] > 0) & (processed == 0))[0]
            seeds = dict()
            seeds = update(seeds, idx, nbhd, core_dists, d_reach, distance_matrix, processed)
            # for each next q in Seeds do
            while len(seeds) > 0:
                next_idx = sorted(seeds.items(), key=operator.itemgetter(1))[0][0]
                del seeds[next_idx]
                #                 mark q as processed
                processed[next_idx] = 1
                sortedlist.append(next_idx)
                close_nbhd = np.where(distance_matrix[:, next_idx] <= epsilon)[0]
                #                 if core-distance(q, eps, MinPts) != UNDEFINED do
                if len(close_nbhd) >= minPts:
                    seeds = update(seeds, next_idx, close_nbhd, core_dists, d_reach, distance_matrix, processed)
    return sortedlist, d_reach

def label(data, sorted, reach_dists, eps):
    N = data.shape[0]
    dist_idx = np.where(reach_dists[sorted] <= eps)[0]
    pre = dist_idx[0] - 1
    cluster_idx = 0
    labels = np.full((N,), -1)
    for current in dist_idx:
        if (current - pre != 1):
            cluster_idx = cluster_idx + 1
        labels[sorted[current]] = cluster_idx
        pre = current
    return labels
