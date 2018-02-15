---
title: 'Leaf classification'
date: 2018-02-15
permalink: /posts/2018/02/Classifying leaves/
mathjax: true
tags:
  - neural network
  - python
---

## Why Leaves?
From long time ago, people have already learned to identify different kinds of plants by examing their leaves. Nowadays, 
leaf Morphology, Taxonomy and Geometric Morphometrics are still actively investigated. Leaves are beautiful creations of nature,
some people today are still using them as special bookmarks or as topics in arts. It would very nice if computers can help create 
leaves automatically from sratches. I assume this is a very difficult task. In order to make a beginner's start, it may be beneficial to
investigate what makes different leaves different from each other. This is a classification problem. Features learned from classification
may help us have a peek at a glimpse of nature's genius idea when it decides to make such creations. 
In industry, automatic recognition of plants is also useful for tasks such as species identification/reservation, automatic separate management in
botany gardens or farms uses plants to produce medicines.

## Data sets
 *[UCI's machine learning repository](https://archive.ics.uci.edu/ml/datasets/leaf). A small data set. 
 *[Swedish leaf dataset](http://www.cvl.isy.liu.se/en/research/datasets/swedish-leaf/). A benchmark data set that is used in many papers, 
 this [website](https://qixianbiao.github.io/Leaf.html) lists some state-of-art methods to compare. (Maybe outdated.)
 *[UCI's 100 leaf](https://archive.ics.uci.edu/ml/datasets/One-hundred+plant+species+leaves+data+set). 
 There was a [Kaggle competition](https://www.kaggle.com/c/leaf-classification) on this.
 

## Some Previous Work
A lot of work has been documented. Generally speaking, efforts are focused on two directions:
* Features that have more discriminating power.
* Classifiers that can better discover hidden patterns from extracted features.

### Main Feature
It may be good to start with some feature that is easy and generative and then check how much accuracy can be squeezed out of it. 
`CCDC`(Centroid Contour Distance Curve) seems to be a good choice. It is one of those shape features and relatively easy to extract. It also has some
nice properties like translation, rotation (after certain alignment) and scaler invariant (after certain normalization).
By applying a `canny filter` to colored images, the contour is then easily obtained. For point $(x, y)$ on the contour, we can then
change it to polar coordinate $(r, \theta)$ by $r = \sqrt{(x-x_c)^2 + (y-y_c)^2}$ and $\theta = \arctan(\frac{y-y_c}{x-x_c})$ where $(x_c, y_c)$
is the center of image which can be computed by image moments. It is important that enough points are sampled so that CCD contains local details of the leaf. In the experiment done below, 200 points 
are sampled.

In this way, leaves are converted into time series and techniques for time serires can be applied. Some easy extension from this may include
`power spectra` and `auto correlation function (acf)` can be extrated as signatures of the CCDC and fead into the classifier. Fancier techinque
like dynamic time warping (DTW) may also be applied. This [website](http://timeseriesclassification.com/) contains many algorithms for time series.

### Main Classifier
As for the classifier, Convolutional Neural Networks now are popular and very effective in image classification tasks if trained properly. It combines feature extraction
and classification together, which allows an end-to-end training.  Due to the limited power of my laptop, I did not go too far with it.
Since 1d feature is used, architectures for 1d data such as simple forward network with only layers are considered as the main classifier.

## Exploration
The first attempt is to directly train a flat network with several dense layers with some regulations (Batchnormalization and dropout). The result
is not very good, only 60%~70% accuracy. There is a big gap between training accuracy and validation accuracy in the learning curve. 
It may because the dataset is small so that the network is trained with bias. It may also because the simple architecture of the network
is not powerful enough.

### The data part



## Conclusions

















