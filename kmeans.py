# https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/

# Step 1: Choose the number of clusters k
# Step 2: Select k random points from the data as centroids
# Step 3: Assign all the points to the closest cluster centroid
# Step 4: Recompute the centroids of newly formed clusters
# Step 5: Repeat steps 3 and 4

# There are essentially three stopping criteria that can be adopted to stop the K-means algorithm:
# Centroids of newly formed clusters do not change
# Points remain in the same cluster
# Maximum number of iterations are reached


from scipy.io import loadmat


data = loadmat('data.mat')
# data['data1'] numpy array (5000, 2)
# data['data2'] numpy array (5000, 2)
# data['data3'] numpy array (5000, 2)
data1 = data['data1']
data2 = data['data2']
data3 = data['data3']

