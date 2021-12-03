# Step 1: Choose the number of clusters k
# Step 2: Select k random points from the data as centroids
# Step 3: Assign all the points to the closest cluster centroid
# Step 4: Recompute the centroids of newly formed clusters
# Step 5: Repeat steps 3 and 4

# There are essentially three stopping criteria that can be adopted to stop the K-means algorithm:
# Centroids of newly formed clusters do not change
# Points remain in the same cluster
# Maximum number of iterations are reached
# Reference: https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/

import numpy as np
import random
from math import *
from copy import deepcopy


def k_means_clustering(k, data):

    def dis(u, v):
        ''' return the distance between u and v '''
        return sqrt((u[0] - v[0])**2 + (u[1] - v[1])**2)
    
    def stable(last_centroids, centroids):
        ''' judge if the centroids are stable '''
        if last_centroids == None: return False
        for i in range(len(centroids)):
            if abs(last_centroids[i][0]-centroids[i][0]) > 1e-6 or abs(last_centroids[i][1]-centroids[i][1]) > 1e-6:
                return False
        return True
    
    cluster = {}
    # Step 2: Select k random points from the data as centroids
    centroids = random.sample(list(data), k) # [array([1.94994131, 0.31367821]), array([0.02987393, 1.03225495]), array([ 0.9149981 , -0.55322564])]
    for i in range(k):
        cluster[i] = {'center': centroids[i], 'point': []}
    last_centroids = None

    while True:
        for i in range(k):
            cluster[i] = {'center': centroids[i], 'point': []}
        last_centroids = deepcopy(centroids)
        
        # Step 3: Assign all the points to the closest cluster centroid
        for point in list(data):
            d = dis(point, cluster[0]['center'])
            c = 0
            for i in range(k):
                if dis(point, cluster[i]['center']) < d:
                    d = dis(point, cluster[i]['center'])
                    c = i
            cluster[c]['point'].append(point)
        
        # Step 4: Recompute the centroids of newly formed clusters
        for i in range(k):
            centroids[i] = np.mean(cluster[i]['point'], axis=0)
        
        # Step 5: Repeat steps 3 and 4 until
        # centroids of newly formed clusters do not change    
        if stable(last_centroids, centroids):
            return cluster
