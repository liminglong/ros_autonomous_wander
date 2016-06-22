#!/usr/bin/env python
# coding=utf-8

import rospy
import random
from subsumption_msgs.msg import Heading

time_duration = 5 #second

def wander():
	global time_duration
	rospy.init_node('wander')
	pub_heading = rospy.Publisher('/wander/heading', Heading, queue_size = 10)
	heading_msg = Heading()
	rate = rospy.Rate(10)
	count = 0
	heading_msg.angle = 0.0
	while not rospy.is_shutdown():
		if count == 10 * time_duration:
			heading_msg.angle = random.uniform(-1.0, 1.0)
			heading_msg.distance = 3.0
			count = 0
		pub_heading.publish(heading_msg)
		count += 1 
		rate.sleep()
		#print (cmd.angular.z)

if __name__ == '__main__':
	try:
		wander()
	except rospy.ROSInterruptException:
		print "Program interrupted before completion"
