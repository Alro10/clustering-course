# coding: utf-8

from gng import GrowingNeuralGas
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import numpy as np
import os
import shutil

__authors__ = 'Alexander Robles'
__email__ = 'alexander.robles20@gmail.com'


if __name__ == '__main__':
    if os.path.exists('visualization/sequence'):
        shutil.rmtree('visualization/sequence')
    os.makedirs('visualization/sequence')
    n_samples = 2500
    print('Load data1')
    data = np.loadtxt("data1.txt")
    print(data.shape)
    print('Done.')
    print('Fitting neural network...')
    gng = GrowingNeuralGas(data)
    gng.fit_network(e_b=0.1, e_n=0.006, a_max=10, l=200, a=0.5, d=0.995, passes=25, plot_evolution=True)
    print('Found %d clusters.' % gng.number_of_clusters())
    gng.plot_clusters(gng.cluster_data())
