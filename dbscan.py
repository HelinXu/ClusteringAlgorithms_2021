# 1. Arbitrary select a point p
# 2. Retrieve all points density-reachable from p based on Eps and MinPts
# 3. If p is a core point, a cluster is formed
# 4. If p is a border point, no points are density-reachable from p and DBSCAN visits the next point of the database
# 5. Continue the process until all of the points have been processed

import numpy as np
import matplotlib.pyplot as plt
import queue

# Define label for differnt point group
NOISE = 0
UNASSIGNED = 0
core = -1
edge = -2


# function to find all neigbor points in radius
def neighbor_points(data, pointId, radius):
    points = []
    for i in range(len(data)):
        # Euclidian distance using L2 Norm
        if np.linalg.norm(data[i] - data[pointId]) <= radius:
            points.append(i)
    return points

# DB Scan algorithom


def dbscan(data, Eps, MinPt):
    # initilize all pointlable to unassign
    pointlabel = [UNASSIGNED] * len(data)
    pointcount = []
    # initilize list for core/noncore point
    corepoint = []
    noncore = []

    print('Find all neigbor for all point')
    # Find all neigbor for all point
    cnt = 0
    for i in range(len(data)):
        if cnt % 100 == 98:
            print(cnt)
        cnt += 1
        pointcount.append(neighbor_points(data, i, Eps))

    print('Find all core point, edgepoint and noise')
    # Find all core point, edgepoint and noise
    for i in range(len(pointcount)):
        if (len(pointcount[i]) >= MinPt):
            pointlabel[i] = core
            corepoint.append(i)
        else:
            noncore.append(i)

    for i in noncore:
        for j in pointcount[i]:
            if j in corepoint:
                pointlabel[i] = edge

                break
    print('start assigning point to luster')
    # start assigning point to luster
    cl = 1
    cnt = 0
    # Using a Queue to put all neigbor core point in queue and find neigboir's neigbor
    for i in range(len(pointlabel)):
        if cnt % 100 == 99:
            print(cnt)
        cnt += 1
        q = queue.Queue()
        if (pointlabel[i] == core):
            pointlabel[i] = cl
            for x in pointcount[i]:
                if(pointlabel[x] == core):
                    q.put(x)
                    pointlabel[x] = cl
                elif(pointlabel[x] == edge):
                    pointlabel[x] = cl
            # Stop when all point in Queue has been checked
            while not q.empty():
                neighbors = pointcount[q.get()]
                for y in neighbors:
                    if (pointlabel[y] == core):
                        pointlabel[y] = cl
                        q.put(y)
                    if (pointlabel[y] == edge):
                        pointlabel[y] = cl
            cl = cl+1  # move to next cluster

    return pointlabel, cl

# Function to plot final result


def plotRes(data, clusterRes, clusterNum):
    nPoints = len(data)
    scatterColors = ['black', 'green', 'brown',
                     'red', 'purple', 'orange', 'yellow']
    for i in range(clusterNum):
        if (i == 0):
            # Plot all noise point as blue
            color = 'blue'
        else:
            color = scatterColors[i % len(scatterColors)]
        x1 = []
        y1 = []
        for j in range(nPoints):
            if clusterRes[j] == i:
                x1.append(data[j, 0])
                y1.append(data[j, 1])
        plt.scatter(x1, y1, c=color, alpha=1, marker='.')
