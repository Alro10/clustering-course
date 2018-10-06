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

### Topic 2
* [Linear Algebra by Prof. Strang](https://www.youtube.com/watch?v=ZK3O402wf1c&list=PL49CF3715CB9EF31D) - Amazing classes of linear algebra

### Topic 3
* [The 5 Clustering Algorithms Data Scientists Need to Know](https://towardsdatascience.com/the-5-clustering-algorithms-data-scientists-need-to-know-a36d136ef68) - Introduction to well-known clustering algorithms for Data Scientists

### Topic 4

* [Clustering high-dimensional data: A survey on subspace clustering, pattern-based clustering, and correlation clustering
](https://dl.acm.org/citation.cfm?id=1497578) - Hans-Peter Kriegel, et. **reference 18 of class material**

* [Subspace clustering](https://onlinelibrary.wiley.com/doi/pdf/10.1002/widm.1057) - Hans-Peter Kriegel, et. **reference 19 of class material**

* [A TUTORIAL ON SUBSPACE CLUSTERING](https://pdfs.semanticscholar.org/2c2c/6609400dcabafd420e18e68a11e994a34e75.pdf) - R. Vidal

* [Subpace Clustering for High Dimensional Data: A Review](http://www.kdd.org/exploration_files/parsons.pdf) - L. Parsons, E. Haque, and H. Liu. **reference 25 of class material**

* [ClustNails: Visual Analysis of Subspace Clusters](https://www.uni-konstanz.de/mmsp/pubsys/publishedFiles/TaZhBe12.pdf) - The paper has **good figures** for understanding subspace clustering.

* [A Geometric Analysis of Subspace Clustering with Outliers](https://projecteuclid.org/download/pdfview_1/euclid.aos/1358951380) - Another paper that has **good figures** for understanding subspace clustering.

<p align="center">
<img src="https://github.com/Alro10/clustering-course/blob/master/topic3.png" alt="alt text" width="50%" height="40%">
</p>

#### Classification based on lecture:

<p align="center">
<img src="https://github.com/Alro10/clustering-course/blob/master/general.png" alt="alt text" width="100%" height="100%">
</p>

<p align="center">
<img src="https://github.com/Alro10/clustering-course/blob/master/subspace.png" alt="alt text" width="100%" height="100%">
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

* [ProClus: The ProClus Algorithm for Projected Clustering](https://rdrr.io/cran/subspace/man/ProClus.html)- R package

* [Subpace clustering](https://rdrr.io/cran/subspace/man/)- R package







