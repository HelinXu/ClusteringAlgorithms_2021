# 自行编写kmeans聚类算法，绘制以上3个数据集的聚类结果

from scipy.io import loadmat
import argparse
import matplotlib.pyplot as plt
import numpy as np
from kmeans import k_means_clustering


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', default=3, type=int)
    opt = parser.parse_args()

    k = opt.k
    data = loadmat('data.mat')
    data1 = data['data1']
    data2 = data['data2']
    data3 = data['data3']

    cluster = k_means_clustering(k=k, data=data1)
    for i in range(k):
        plt.scatter(np.array(cluster[i]['point']).T[0],np.array(cluster[i]['point']).T[1])
    plt.show()

    cluster = k_means_clustering(k=k, data=data2)
    for i in range(k):
        plt.scatter(np.array(cluster[i]['point']).T[0],np.array(cluster[i]['point']).T[1])
    plt.show()

    cluster = k_means_clustering(k=k, data=data3)
    for i in range(k):
        plt.scatter(np.array(cluster[i]['point']).T[0],np.array(cluster[i]['point']).T[1])
    plt.show()