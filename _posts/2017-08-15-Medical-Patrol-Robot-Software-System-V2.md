---
layout: post
title:  Medical & Patrol Robot (XiaoBai) Software System-V2.4
---

Recently, I reconstructed the software system of XiaoBai robot. Now the entire software system are transfered to ROS system. Digrapg of entire software system is shown as follow:

![]({{ site.url }}/images/XiaoBai-Robot/structure)

![]({{ site.url }}/images/XiaoBai-Robot/map.png)

Besides, the user interface is no longer based on QT. Instead, the interface has been rewrote by html5 and javascript. And the backend of the interface has been reconstructed with django and websocket too. In this way, the user interface can be truly cross-platform. We can control the robot through any device with a browser (Even iPad and smart phone).

Controller:

![]({{ site.url }}/images/XiaoBai-Robot/controller.png)