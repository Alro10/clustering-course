# clustering-course
Subspace clustering and coclustering course at the School of Electrical and Computer Engineering (FEEC-UNICAMP). I just want to collect repositories and useful materials for clustering course. Official site by Prof. Fernando Von Zuben and Rosana Veroneze [here](http://www.dca.fee.unicamp.br/~vonzuben/courses/ia376.html).

## Definition of Clustering:

Clustering or cluster analysis takes a mass of observations and separates them, using some measure of dissimilarity, into distinct groups called clusters (disjoint subsets of the whole dataset). Each group is expected to exhibit some internal homogeneity. 


## Table of Contents 

<!-- MarkdownTOC depth=4 -->
- [Tutorials](#github-tutorials)
- [Coding/Projects](#github-projects)

<!-- /MarkdownTOC -->


<a name="github-tutorials" />

## Tutorials

### Topic 1
* [Linear Algebra by Prof. Strang](https://www.youtube.com/watch?v=ZK3O402wf1c&list=PL49CF3715CB9EF31D) - Amazing classes of linear algebra

### Topic 2
* [The 5 Clustering Algorithms Data Scientists Need to Know](https://towardsdatascience.com/the-5-clustering-algorithms-data-scientists-need-to-know-a36d136ef68) - Introduction to well-known clustering algorithms for Data Scientists

### Topic 3

* [Subpace Clustering for High Dimensional Data: A Review](http://www.kdd.org/exploration_files/parsons.pdf) - L. Parsons, E. Haque, and H. Liu.

* [ClustNails: Visual Analysis of Subspace Clusters](https://www.uni-konstanz.de/mmsp/pubsys/publishedFiles/TaZhBe12.pdf) - The paper has **good figures** for understanding subspace clustering.

* [A Geometric Analysis of Subspace Clustering with Outliers](https://projecteuclid.org/download/pdfview_1/euclid.aos/1358951380) - Another paper that has **good figures** for understanding subspace clustering.

<p align="center">
<img src="https://github.com/Alro10/clustering-course/blob/master/topic3.png" alt="alt text" width="60%" height="60%">
</p>

<a name="github-projects" />

## Coding/Projects

### Clustering

**scikit learn** package has many clustering algorithms implementation, you can see [here](http://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering). How to install on Ubuntu 16.04 (needs numpy and scipy):

* Python 2.7

$ pip install -U scikit-learn

* Python 3.5

$ pip3 install -U scikit-learn

* [Agglomerative Clustering](http://scikit-learn.org/stable/auto_examples/cluster/plot_digits_linkage.html#sphx-glr-auto-examples-cluster-plot-digits-linkage-py)

* [k-means](http://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html#sphx-glr-auto-examples-cluster-plot-kmeans-digits-py)

* [DBSCAN](http://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#sphx-glr-auto-examples-cluster-plot-dbscan-py)

* [Spectral Clustering](http://scikit-learn.org/stable/auto_examples/cluster/plot_segmentation_toy.html#sphx-glr-auto-examples-cluster-plot-segmentation-toy-py)

* [The EM algorithm](http://scikit-learn.org/stable/modules/mixture.html)

* [Fuzzy c-means](https://github.com/bm424/scikit-cmeans). Other good example [here](https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_cmeans.html)

* [Self-organizing maps](https://github.com/JustGlowing/minisom)- MiniSom is a minimalistic and Numpy based implementation of the Self Organizing Maps (SOM)

### Subspace Clustering








