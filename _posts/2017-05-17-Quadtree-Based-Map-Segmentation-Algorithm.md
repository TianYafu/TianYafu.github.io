---
layout: post
title: [Waiting for publish] Quadtree-Based Map Segmentation-Algorithm
---

I made a great improvement on my previous map segmentation algorithm [thesis pdf]({{ site.url }}/Resources/Autonomous-Map-Segmentation/PID4286163.pdf). In this algorithm, I focused on the stability, resource occupation of algorithm. This page will be updated until this paper finally published (About March 2018).

**Abstract**

Currently, state-of-art SLAM methods are capable of generating large scale and dense environmental map. One primary
reason may be the applications of map partition strategies. An efficient map partition method will decrease the time
complexity of SLAM algorithm, and more importantly, make robot understand a place anthropomorphically. In this
paper, we propose a novel map segmentation algorithm based on QuadTree and spectral clustering. The map is firstly
organized hierarchically by using QuadTree, and then an user-friendly criterion is utilized to construct corresponding
Laplacian matrix for QuadTree, so that spectral clustering can be solved efficiently based on sparse property of matrix.
In this paper, we go further to provide a real-time incremental, parallel algorithm that can implemented on multi-
core CPU/GPU to enhance the performance of proposed basic algorithm. Our Algorithms are verified on multiple
environments including both simulation and real world data, and results reveal that the algorithm can provide a correct
and user-friendly segmentation result in a short runtime.

**Keywords
Autonomous map segmentation, QuadTree, Spectral cluster**