import cv2
import numpy  as np
from matplotlib import pyplot as plt

#start - 0 end-100 (excluded), 16 values , two colums 
data = np.random.randint(0,100,(16,2)).astype(np.float32)
print(data)
#creating the labels (0:red, 1:blue for each of the 16 points) 
labels = np.random.randint(0,2,(16,1)).astype(np.float32)

sample = np.random.randint(0,100,(1,2)).astype(np.float32)
#k-NN creation
knn = cv2.ml.KNearest_create()
#K-NN training
#train() to provide both the data and the labels
knn.train(data, cv2.ml.ROW_SAMPLE, labels)

k=3
ret, results, neighbours, dist = knn.findNearest(sample, k)
# results stores the predictions for each input sample, 
#neighborResponses stores the corresponding neighbors,
#dist-the distances from the input samples to the corresponding neighbors

print("result:{}".format(results))
print("neighbours:{}".format(neighbours))
print("distance:{}".format(dist))

# Plot all the data and print the results:
fig = plt.figure(figsize=(8, 6))
fig.patch.set_facecolor('silver')

red_triangles = data[labels.ravel() == 0]
plt.scatter(red_triangles[:, 0], red_triangles[:, 1], 200, 'r', '^')

# Take points with label 1 (will be the blue squares) and plot them:
blue_squares = data[labels.ravel() == 1]
plt.scatter(blue_squares[:, 0], blue_squares[:, 1], 200, 'b', 's')

# Plot the sample point:
plt.scatter(sample[:, 0], sample[:, 1], 200, 'g', 'o')

plt.show()