#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from sensor_msgs.msg import Joy

def publish_joy(joy_msg):
    rospy.loginfo(joy_msg.axes[0])

if __name__== '__main__':
    rospy.init_node('testcode')
    rospy.Subscriber('joy', Joy, publish_joy, queue_size=1)
    rospy.spin()
