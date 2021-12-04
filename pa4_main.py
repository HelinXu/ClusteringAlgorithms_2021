# 4. 利用数据集data3，对DBSCAN算法进行如下实验：
# (1)选择不同的ϵ,观察实验结果并分析原因；(1分)
# (2)选择不同的minPots，观察实验结果并分析原因；(1分)

from dbscan import dbscan, plotRes
import collections
import scipy.io as spio
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Load Data
    data = spio.loadmat('data.mat')
    data3 = data['data3']
    
    eps = 0.001
    minpts = 100
    print('Set eps = ' + str(eps) + ', Minpoints = '+str(minpts))
    pointlabel, cl = dbscan(data3, eps, minpts)
    plotRes(data3, pointlabel, cl)
    plt.show()
    print('number of cluster found: ' + str(cl-1))
    counter = collections.CouDBACANnter(pointlabel)
    print(counter)
    outliers = pointlabel.count(0)
    print('numbrer of outliers found: '+str(outliers) + '\n')
    
    eps = 0.01
    minpts = 100
    print('Set eps = ' + str(eps) + ', Minpoints = '+str(minpts))
    pointlabel, cl = dbscan(data3, eps, minpts)
    plotRes(data3, pointlabel, cl)
    plt.show()
    print('number of cluster found: ' + str(cl-1))
    counter = collections.Counter(pointlabel)
    print(counter)
    outliers = pointlabel.count(0)
    print('numbrer of outliers found: '+str(outliers) + '\n')

    eps = 0.05
    minpts = 10
    print('Set eps = ' + str(eps) + ', Minpoints = '+str(minpts))
    pointlabel, cl = dbscan(data3, eps, minpts)
    plotRes(data3, pointlabel, cl)
    plt.show()
    print('number of cluster found: ' + str(cl-1))
    counter = collections.Counter(pointlabel)
    print(counter)
    outliers = pointlabel.count(0)
    print('numbrer of outliers found: '+str(outliers) + '\n')

    eps = 0.1
    minpts = 10
    print('Set eps = ' + str(eps) + ', Minpoints = '+str(minpts))
    pointlabel, cl = dbscan(data3, eps, minpts)
    plotRes(data3, pointlabel, cl)
    plt.show()
    print('number of cluster found: ' + str(cl-1))
    counter = collections.Counter(pointlabel)
    print(counter)
    outliers = pointlabel.count(0)
    print('numbrer of outliers found: '+str(outliers) + '\n')


    eps = 0.2
    minpts = 100
    print('Set eps = ' + str(eps) + ', Minpoints = '+str(minpts))
    pointlabel, cl = dbscan(data3, eps, minpts)
    plotRes(data3, pointlabel, cl)
    plt.show()
    print('number of cluster found: ' + str(cl-1))
    counter = collections.Counter(pointlabel)
    print(counter)
    outliers = pointlabel.count(0)
    print('numbrer of outliers found: '+str(outliers) + '\n')

    eps = 0.2
    minpts = 10
    print('Set eps = ' + str(eps) + ', Minpoints = '+str(minpts))
    pointlabel, cl = dbscan(data3, eps, minpts)
    plotRes(data3, pointlabel, cl)
    plt.show()
    print('number of cluster found: ' + str(cl-1))
    counter = collections.Counter(pointlabel)
    print(counter)
    outliers = pointlabel.count(0)
    print('numbrer of outliers found: '+str(outliers) + '\n')
    
    eps = 0.2
    minpts = 3
    print('Set eps = ' + str(eps) + ', Minpoints = '+str(minpts))
    pointlabel, cl = dbscan(data3, eps, minpts)
    plotRes(data3, pointlabel, cl)
    plt.show()
    print('number of cluster found: ' + str(cl-1))
    counter = collections.Counter(pointlabel)
    print(counter)
    outliers = pointlabel.count(0)
    print('numbrer of outliers found: '+str(outliers) + '\n')

    eps = 0.1
    minpts = 3
    print('Set eps = ' + str(eps) + ', Minpoints = '+str(minpts))
    pointlabel, cl = dbscan(data3, eps, minpts)
    plotRes(data3, pointlabel, cl)
    plt.show()
    print('number of cluster found: ' + str(cl-1))
    counter = collections.Counter(pointlabel)
    print(counter)
    outliers = pointlabel.count(0)
    print('numbrer of outliers found: '+str(outliers) + '\n')
    
    eps = 0.5
    minpts = 3
    print('Set eps = ' + str(eps) + ', Minpoints = '+str(minpts))
    pointlabel, cl = dbscan(data3, eps, minpts)
    plotRes(data3, pointlabel, cl)
    plt.show()
    print('number of cluster found: ' + str(cl-1))
    counter = collections.Counter(pointlabel)
    print(counter)
    outliers = pointlabel.count(0)
    print('numbrer of outliers found: '+str(outliers) + '\n')
