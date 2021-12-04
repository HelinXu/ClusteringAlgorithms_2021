from dbscan import dbscan, plotRes
import collections
import scipy.io as spio
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Load Data
    data = spio.loadmat('data.mat')
    data1 = data['data1']
    data2 = data['data2']
    data3 = data['data3']

    eps = 0.01
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
    minpts = 100
    print('Set eps = ' + str(eps) + ', Minpoints = '+str(minpts))
    pointlabel, cl = dbscan(data1, eps, minpts)
    plotRes(data1, pointlabel, cl)
    plt.show()
    print('number of cluster found: ' + str(cl-1))
    counter = collections.Counter(pointlabel)
    print(counter)
    outliers = pointlabel.count(0)
    print('numbrer of outliers found: '+str(outliers) + '\n')

    eps = 1
    minpts = 80
    print('Set eps = ' + str(eps) + ', Minpoints = '+str(minpts))
    pointlabel, cl = dbscan(data2, eps, minpts)
    plotRes(data2, pointlabel, cl)
    plt.show()
    print('number of cluster found: ' + str(cl-1))
    counter = collections.Counter(pointlabel)
    print(counter)
    outliers = pointlabel.count(0)
    print('numbrer of outliers found: '+str(outliers) + '\n')

    eps = 0.5
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