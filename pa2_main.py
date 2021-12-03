# 利用数据集data2，对kmeans算法进行如下实验
# 1)聚类数目从2类开始逐渐增加，分别进行计算并分析聚类结果，决定最合适的
# 聚类数目并说明理由
# 2)选择不同的初始点多次实验，观察初始点的选择对最终结果的影响，并分析
# 原因

from scipy.io import loadmat
import os
import matplotlib.pyplot as plt
import numpy as np
from kmeans import k_means_clustering, inertia

# The inertia is defined as the sum of square distances of samples to
# their cluster center, weighted by the sample weights if provided.

if __name__ == '__main__':
    data = loadmat('data.mat')
    data2 = data['data2']

    k_list = range(2, 8)
    interia_list = []
    for k in k_list:
        cluster = k_means_clustering(k=k, data=data2)
        itr = inertia(cluster)
        print(itr)
        interia_list.append(itr)
        for i in range(k):
            plt.scatter(np.array(cluster[i]['point']).T[0],np.array(cluster[i]['point']).T[1])
        plt.savefig(os.path.join(f'./img/kmeans_data2_k{k}.png'))
        plt.close()

    plt.plot(k_list, interia_list, marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('Inertia')
    plt.show()

    # In some cases, if the initialization of clusters
    # is not appropriate, K-Means can result in arbitrarily
    # bad clusters. This is where K-Means++ helps. It
    # specifies a procedure to initialize the cluster centers
    # before moving forward with the standard k-means clustering
    # algorithm.

    # 1. The first cluster is chosen uniformly at random from 
    # the data points that we want to cluster. This is similar 
    # to what we do in K-Means, but instead of randomly picking 
    # all the centroids, we just pick one centroid here

    # 2. Next, we compute the distance (D(x)) of each data point (x)
    # from the cluster center that has already been chosen

    # 3. Then, choose the new cluster center from the data points 
    # with the probability of x being proportional to (D(x))2

    # 4. We then repeat steps 2 and 3 until *k* clusters have been 
    # chosen
