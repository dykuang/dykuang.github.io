---
title: 'geodesics on 2d surfaces'
date: 2017-10-10
permalink: /posts/2017/10/geodesics on 2d surfaces/
tags:
  - geodesics
  - python
---

Geometries can be fun, though it will require a deep and strict mathematical formulation. Physics and geometry has nature and deep connections with each other. It is well known that einstein's theory of general relaltivity will need the support from non-Euclidean Geometry. One of the interesting topics in geometry is about finding geodesics. You can image the geodesic as a curve that minimizes certain *metrics* bewteen two fixed points in the considered space. One natural way of formulating the problem formally is by calculus of variations where you write your target metric as a functional and the Euler - Langrange Equation of this functional will govern the behavior of the geodesic. Usually, if the configuration space will have dimension 2N where N is the dimension of the manifold with geodesics on. There is a beatiful theorm: Noether's theorem that can help deduct the dimension to N by solving a corresponding equation on the Lie Algebra. I think [Prof. Terrence Tao's post](https://terrytao.wordpress.com/tag/euler-arnold-equation/) gives a very good explanation about this techique.

If the manifold is a smooth 3d graph or a smooth 2d surface where things are not too complicated there. We can directly work on the configuration space, write down the patch map, the corresponding EL-equation and uses certain numerical schemes to integration out the solution. It should be aware that systems like this usually will have intrinsic invariance or symmetries, so it is better to use a symplectic integrator for *long* geodesics.

The following .mp4 files illustrates some geodesics on selected surfaces. You can download .py files [here](https://dykuang.github.io/Files/Geo_ellipzoid.py) for  the revolutional ellipzoid animation and [here](https://dykuang.github.io/Files/Geo_2dGauss.py) for the Gaussian-density-liked surface 

**Q**:For general ellipzoid, i.e. \(x^2/a^2 + y^2/b^2 + z^2/c^2 = 1\), where \(a, b ,c\) are all different. The program can give very wired curves. I did not find many useful contents about geodesics on general ellipzoid from google, is it still an open question? or at least part of it? 

### One geodesic on a revolutional ellipzoid ###
<video src="/images/geo_Ellipzoid1.mp4" width="720" height="360" controls preload></video>

### Another geodesic on the same revolutional ellipzoid ###
<video src="/images/geo_ellipzoid.mp4" width="720" height="360" controls preload></video>

### Different geodesics on the surface \$$ f(x, y) = exp(-x^2/2-y^2)$$ ###
<video src="/images/geo_2dGauss.mp4" width="720" height="360" controls preload></video>


