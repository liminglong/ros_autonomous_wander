#!/usr/bin/env python
# coding=utf-8

import rospy
import random
import math
import numpy as np

from subsumption_msgs.msg import Heading
from subsumption_msgs.msg import Force

#global variables
#wander_heading_msg = Heading()
feelforce_force_msg = Force()
random_factor = 0.5 #proportion of the heading message 

def avoid_headingCB(wander_heading_msg):
	#global wander_heading_msg
	global feelforce_force_msg
	#wander_heading_msg = msg
	avoid_heading_msg = Heading()
	'''
	Summing Method 1: 
	calculate the average of the two scalar quantities(heading_msg.angle and force_msg.direction))
	''' 
	#avoid_heading_msg.angle = (random_factor) * wander_heading_msg.angle + (1 - random_factor) * feelforce_force_msg.direction
	'''
	Summing Method 2: 
	calculate the average of the two vectors(heading and force))
	'''
	x_0 = 0.0
	y_0 = 0.0
	x_1 = 0.0
	y_1 = 0.0
	x_average = 0.0
	y_average = 0.0	

	x_0 = wander_heading_msg.distance * math.cos(wander_heading_msg.angle)
	y_0 = wander_heading_msg.distance * math.sin(wander_heading_msg.angle)

	x_1 = feelforce_force_msg.magnitude * math.cos(feelforce_force_msg.direction)
	y_1 = feelforce_force_msg.magnitude * math.sin(feelforce_force_msg.direction)

	x_average = random_factor * x_0 + (1 - random_factor) * x_1
	y_average = random_factor * y_0 + (1 - random_factor) * y_1

	avoid_heading_msg.distance = math.sqrt(x_average ** 2 + y_average ** 2) 
	avoid_heading_msg.angle = (np.arctan2(y_average, x_average) + 2 * math.pi) % (2 * math.pi)

	#TODO: avoid local obstacles, calculate the threshold of the resulting force,
	#TODO: but in this implementation it may seem needless('collide' module already has this function)
	pub_heading = rospy.Publisher('/avoid/suppressor/heading', Heading, queue_size = 10)
	pub_heading.publish(avoid_heading_msg)
	print "The avoid heading message was published successfully!"

def avoid_forceCB(msg):
	#global wander_heading_msg
	global feelforce_force_msg
	feelforce_force_msg = msg
	

def avoid():
	rospy.init_node('avoid')
	rospy.Subscriber("/wander/heading", Heading, avoid_headingCB)
	rospy.Subscriber("/feelforce/force", Force, avoid_forceCB)
	rospy.spin()

if __name__ == '__main__':
	try:
		avoid()
	except rospy.ROSInterruptException:
		print "Program interrupted before completion"

