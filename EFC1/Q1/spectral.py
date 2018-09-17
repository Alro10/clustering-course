
# import packages

import pandas as pd
import numpy as np


# Imports for SpectralClustering
from sklearn.cluster import SpectralClustering

from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import matplotlib as mpl

# Load cluster data

X = np.loadtxt('data1.txt')


# Compute SpectralClustering

spc = SpectralClustering(n_clusters=6,
                        # eigen_solver='arpack', # {None, ‘arpack’, ‘lobpcg’, or ‘amg’}
                        kernel_params='', # chi2_kernel
                        assign_labels= 'kmeans', # {‘kmeans’, ‘discretize’}
                        affinity="nearest_neighbors").fit(X) #‘nearest_neighbors’, ‘precomputed’, ‘rbf’ or
# cosine_similarity, Linear kernel,  Polynomial kernel, Sigmoid kernel,  RBF kernel,  Laplacian kernel, 
# Chi-squared kernel


# Hiperparameters
# Affinity matrix construction: distance and kernel;
# kernel parameter (scaling factor);
# number of clusters k;
# clustering method

core_samples_mask = np.zeros_like(spc.labels_, dtype=bool)
#core_samples_mask[spc.core_sample_indices_] = True

labels = spc.labels_

n_clusters_ =  len(set(labels)) - (1 if -1 in labels else 0)


# Black removed and is used for noise instead.
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = (labels == k)

    xy = X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=10)

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=4)

plt.title('Estimated number of clusters: %d' % n_clusters_)
mpl.rcParams['figure.dpi']= 300
mpl.rcParams['figure.figsize']= (8, 6)
#plt.show()  # uncomment this for showing the figure
plt.savefig('spectral.png')