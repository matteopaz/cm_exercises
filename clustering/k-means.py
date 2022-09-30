# import mpl
import matplotlib.pyplot as plt
import math
data = [
    [0.14, 0.14, 0.28, 0.44],
    [0.22, 0.1,  0.45, 0.33],
    [0.1,  0.19, 0.25, 0.4 ],
    [0.02, 0.08, 0.43, 0.45],
    [0.16, 0.08, 0.35, 0.3 ],
    [0.14, 0.17, 0.31, 0.38],
    [0.05, 0.14, 0.35, 0.5 ],
    [0.1,  0.21, 0.28, 0.44],
    [0.04, 0.08, 0.35, 0.47],
    [0.11, 0.13, 0.28, 0.45],
    [0.0,  0.07, 0.34, 0.65],
    [0.2,  0.05, 0.4,  0.37],
    [0.12, 0.15, 0.33, 0.45],
    [0.25, 0.1,  0.3,  0.35],
    [0.0,  0.1,  0.4,  0.5 ],
    [0.15, 0.2,  0.3,  0.37],
    [0.0,  0.13, 0.4,  0.49],
    [0.22, 0.07, 0.4,  0.38],
    [0.2,  0.18, 0.3,  0.4 ]
]
# data = [
#     [0, 0.8],
#     [-0.5,1],
#     [0.5,1],
#     [-1000,1],
#     [-999,0.5]
# ]

# data = [
#     [0, 1000],
#     [-0.5,1000],
#     [0.5,1000],

#     [-1000,1],
#     [-999,0.5],

#     [1000, 0.5],
#     [1001, -100]
# ]

def center(pts):
    dim = len(pts[0])
    ctr = [0]*dim
    for param_num in range(dim):
        sum = 0
        for pt in pts:
            sum += pt[param_num]
        ctr[param_num] = sum / len(pts)
    return ctr

def dist(pt1, pt2):
    diff = [0]*len(pt1)
    for i in range(len(diff)):
        diff[i] = pt1[i] - pt2[i]
    
    d_squared = 0
    for val in diff:
        d_squared += val**2

    return math.sqrt(d_squared)

def get_cluster_pts(k, pts):
    cluster_pts = []
    for i in range(k):
        cluster_pts.append([])

    for pt in pts:
        cluster_pts[pt[0]].append(pt[1:])
    return cluster_pts

def k_means(k, pts):
    labeled = []
    for i in range(len(pts)):
        labeled_pt = [(i % k)]
        labeled_pt.extend(pts[i])
        labeled.append(labeled_pt)
    # print(labeled)
    cluster_pts = get_cluster_pts(k, labeled)
    
    centers = []
    for cluster in cluster_pts:
        centers.append(center(cluster))
    
    prev_cluster_nums = []
    while(1):
        # print("CTRS:", centers)
        # print("\n")
        # for c in cluster_pts:
        #     print(c)
        # print("\n")
        

        cluster_nums = [] # Check if labels are changing
        for pt in labeled:
            cluster_nums.append(pt[0])
        if cluster_nums == prev_cluster_nums:
            break
        else:
            prev_cluster_nums = cluster_nums

        centers = [] # Update centers
        cluster_pts = get_cluster_pts(k, labeled)
        for cluster in cluster_pts:
            if cluster == []:
                continue
            centers.append(center(cluster))

        for i in range(len(labeled)): # Find nearest center for each point
            pt = labeled[i][1:]

            min_cluster = 0
            min_dist = dist(pt, centers[0])
            for j in range(len(centers)):
                ctr = centers[j]
                distance_to_ctr = dist(ctr, pt)
                if distance_to_ctr < min_dist:
                    min_cluster = j
                    min_dist = distance_to_ctr
            labeled[i][0] = min_cluster
    cpts = get_cluster_pts(k, labeled)
    for c in cpts:
        print(c)
        print("\n")
    return cpts



k_means(3, data)

ks = range(1, 16)
inertias = []
for k in ks:
    clusters = k_means(k, data)
    inertia = 0
    for i in range(len(clusters)):
        for pt in clusters[i]:
            inertia += dist(pt, center(clusters[i]))**2
    inertias.append(inertia)
# plot inertias vs ks
plt.plot(ks, inertias, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.show()