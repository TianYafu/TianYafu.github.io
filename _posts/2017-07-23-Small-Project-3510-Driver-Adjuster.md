---
layout: post
title: 3510 Motor Driver's Adjuster with GUI
---

The aim of this project is to help new student (in my lab) adjusting motor with 3510 motor driver. This motor driver is a high-performance, mid-power driver developed by State Key Laboratory of Robotics and System. 3510 Motor driver receive both 485 serial communication and CAN communication. By providing a graphic interface, I free some student from suffering the pain of calculating and generating CAN message manually. This program can also track and plot robot's speed automatically.

This program provides 3 levels of interface:

1. Users without any programming can use GUI interface adjusting motor. This GUI integrates some regular functions and it is easy to use!
2. Programmer whom don't want to rely on ROS can import functions from CANBusController.py. This script provides low-level functions which implements common operation of 3510 Motor Driver. 
3. This project also provides ROS nodes and topics which are conveninent for ROS users.

3510 Motor Driver:


ROS node grpah 

![](images/dfsa)

Source Code and Manual: [Source Code]()  [pdf manual]() [3510 motor's manual]()