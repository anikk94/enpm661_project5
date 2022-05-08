#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 10:55:25 2022

@author: pulkit
"""

import rospy 
from geometry_msgs.msg import Twist
from competition import *
import time
import os


with open('output.txt') as f:
    lines = f.readlines()
        
w = []
v = []

for line in lines:
    w_, v_ = line.strip().split(" ")
    w.append(float(w_))
    v.append(float(v_))

        
def main():
    rospy.init_node('comp_node')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    cmd = Twist()
    rate = rospy.Rate(10)

    for i in range(len(v)):  
        # rospy.loginfo(v[i]) 
        start = time.time()
        while(time.time() - start <= 1.0):
            # rospy.loginfo(counter)
            cmd.linear.x = v[i]
            cmd.angular.z = w[i]
            pub.publish(cmd)
            rate.sleep()

    cmd.linear.x = 0
    cmd.angular.z = 0
    pub.publish(cmd)        
    rospy.signal_shutdown('done')

            
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
