---
layout: post
title: Indoor Patrol Robot Software System ( Graduation Design )
---

## Robot System

## Hardware

We use a PeopleBot-sh robot (from Aria Mobile Robot) as a platform. A Hokuyo UST-10LX laser scanner was added on the robot. 

## Software

I didn't use ROS in this project. Instead, I wrote all components in python, include robot controller, path planning, and SLAM system. It takes me about half a year to get done and then I learned not making any wheels :)


![]({{ site.url }}/images/Indoor_Patrol_Robot_Software_System/realexp01.JPG)

# Unknown Area Detection

A robot with curiosity is a good idea, so I let robot explore its working environment by itself. The robot will check any place where range signal changes severely. If the place hasn't been explored, the robot will try to approach this area. This method works well, but the robot shall be kept away from the stairway.

![]({{ site.url }}/images/Indoor_Patrol_Robot_Software_System/scanner03.jpg)

# Robot SLAM System

This robot uses a classical (and easy to implement! ) way localize itself and build map. The first step is to extract feature point and geometry feature from LIDAR observation. Then match them into a global map. As the odometry is robust in
 linear movement and laser scanner can estimate rotation easily. I designed a switch system to determine the estimation from different source and it works! I also tried particle filter method. This algorithm solved the initiation problem.

![]({{ site.url }}/images/Indoor_Patrol_Robot_Software_System/map.png)

Digraph about a part of the SLAM system.

![]({{ site.url }}/images/Indoor_Patrol_Robot_Software_System/slamSystem.png)



#  Ref

[1] 赵立军, 孙立宁, 李瑞峰, and 葛连正. 室内环境下同步定位与地图创建改进算法. 机
器人, 31(5):438–444, 2009.

[2] 李阳铭, 孟庆虎, 梁华为, 李帅, 陈万明, et al. 基于粒子滤波的无线传感器网络辅助
同步定位与地图创建方法研究. 机器人, 30(5):421–427, 2008.

[3] 王卫华, 陈卫东, and 席裕庚. 基于不确定信息的移动机器人地图创建研究进展.
机器人, 06:563–568, 2001.

[4] 王珂, 赵立军, and 李瑞峰. 基于贯序mb-icp 融合的机器人复杂室内地图构建. 中国
自动化学会控制理论专业委员会B 卷, 6, 2011.

[5] C. Nieto-Granda, J. G. Rogers, A. J. B. Trevor, and H. I. Christensen. Semantic map
partitioning in indoor environments using regional analysis. In Intelligent Robots and
Systems (IROS), 2010 IEEE/RSJ International Conference on, pages 1451–1456, Oct
2010.

[6] 李瑞峰and 李伟招. 基于多传感器信息融合的移动机器人路径规划. 机电一体化,
8(4):20–23, 2002.

[7] Von der Hardt, Didier Wolf, René Husson, et al. The dead reckoning localization
system of the wheeled mobile robot romane. In Multisensor Fusion and Integration
for Intelligent Systems, 1996. IEEE/SICE/RSJ International Conference on, pages
603–610. IEEE, 1996.

[8] 王卫华, 陈卫东, and 席裕庚. 移动机器人地图创建中的不确定传感信息处理. 自动
化学报, 29(2):267–274, 2003.

[9] Jose A Castellanos, JM Martinez, Jose Neira, and Juan D Tardós. Simultaneous
map building and localization for mobile robots: A multisensor fusion approach. In
Robotics and Automation, 1998. Proceedings. 1998 IEEE International Conference
on, volume 2, pages 1244–1249. IEEE, 1998.

[10] Dieter Fox, Wolfram Burgard, Hannes Kruppa, and Sebastian Thrun. A probabilistic
approach to collaborative multi-robot localization. Autonomous robots, 8(3):325–344,
2000.

[11] 厉茂海, 洪炳熔, and 罗荣华. 用改进的rao-blackwellized 粒子滤波器实现移动机器
人同时定位和地图创建. 吉林大学学报: 工学版, 37(2):401–406, 2007.

[12] Liang Zhao, Shoudong Huang, and Gamini Dissanayake. Linear slam: A linear
solution to the feature-based and pose graph slam based on submap joining. In
Intelligent Robots and Systems (IROS), 2013 IEEE/RSJ International Conference
on, pages 24–30. IEEE, 2013.

[13] 黄庆成, 洪炳熔, 厉茂海, and 罗荣华. 基于主动环形闭合约束的移动机器人分层同
时定位和地图创建. 计算机研究与发展, 44(4):636–642, 2007.

[14] Felix Endres, Jurgen Hess, Jurgen Sturm, Daniel Cremers, and Wolfram Burgard.
3-d mapping with an rgb-d camera. Robotics, IEEE Transactions on, 30(1):177–187,
2014.
71

[15] David Filliat. A visual bag of words method for interactive qualitative localization
and mapping. In Robotics and Automation, 2007 IEEE International Conference on,
pages 3921–3926. IEEE, 2007.

[16] Ethan Eade and Tom Drummond. Unified loop closing and recovery for real time
monocular slam. In BMVC, volume 13, page 136. Citeseer, 2008.

[17] Kok Seng Chong and L. Kleeman. Accurate odometry and error modelling for a mobile
robot. In Robotics and Automation, 1997. Proceedings., 1997 IEEE International
Conference on, volume 4, pages 2783–2788 vol.4, Apr 1997.

[18] Ulrike Von Luxburg. A tutorial on spectral clustering. max planck institute for
biological cybernetics. Technical report, Tech. Rep, 2006.


# Resources:

1. [Thesis]({{ site.url }}/Resources/Indoor_Patrol_Robot_Software_System/main.pdf)
2. [Powerpoint for oral representation]({{ site.url }}/Resources/Indoor_Patrol_Robot_Software_System/ppt.pdf)



[Return to homepage]({ {site.url} })
