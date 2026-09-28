from sklearn.cluster import KMeans

X=[[5, 2], [6, 3], [5, 1],
     [40, 2], [45, 3], [42, 1],
     [20, 15], [22, 14], [19, 16]]
model= KMeans(n_clusters=3, random_state=0, n_init=10)
model.fit(X)

print("Cluster of each customer: ", model.labels_)

print("Cluster centres:\n", model.cluster_centers_) # averaged center points average of each clusters

print("New customer [41, 2] goes to cluster: ", model.predict([[41,2]]))