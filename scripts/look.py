#!/usr/bin/env python
#coding=utf-8
import roslib
import rospy

from sensor_msgs.msg import LaserScan
from subsumption_msgs.msg import Path
from std_msgs.msg import Bool
import math
import numpy as np

#global variables
max_range = 8.0#if the laser sensed distance is larger than the maximum distance, assign it the parameter
start_look = False
travel_max_distance = 10.0

def laserCB(msg):
	global start_look
	global max_range
	global travel_max_distance
	if start_look == True:
		#if strat_look is triggered, start calculating
		ranges = list(msg.ranges)
		turn_angle = 0.0
		forward_magnitude = 0.0
		for i in range(0, len(ranges)):
			if ranges[i] == float("inf"):
				ranges[i] = max_range
		max_distance = np.max(ranges)
		#choose a direction
		count_a = 0
		count_b = 0
		count_c = 0
		count_d = 0
		angle_index = 0.0
		for i in range(0, len(ranges)-1):
			if ranges[i] == max_distance:
				count_a = i
				break
		for i in range(0, len(ranges)-1):
			if ranges[i] == max_distance and (not (ranges[i+1] == max_distance)):
				count_b = i
				break
		for i in range(count_b+1, len(ranges)-1):
			if ranges[i] == max_distance:
				count_c = i
				break
		for i in range(count_b+1, len(ranges)-1):
			if ranges[i] == max_distance and (not (ranges[i+1] == max_distance)):
				count_d = i
		#calculate the turn angle	
		if abs(count_b - count_a) > abs(count_c - count_d):
			angle_index = (float(count_a + count_b)) / 2
			if angle_index == 0 or ((angle_index > 0) and (angle_index) < 135):
				turn_angle = (225 + angle_index) * (math.pi / 180)
			else:
				turn_angle = (angle_index - 135) * (math.pi / 180)	
		else:
			angle_index = (float(count_c + count_d)) / 2 
			if angle_index == 0 or ((angle_index > 0) and (angle_index) < 135):
				turn_angle = (225 + angle_index) * (math.pi / 180)
			else:
				turn_angle = (angle_index - 135) * (math.pi / 180)		
		#publish the path message
		pub_path = rospy.Publisher("/look/path", Path, queue_size = 10)
		path_msg = Path()
		path_msg.path_angle = turn_angle
		path_msg.path_distance = max_distance
		pub_path.publish(path_msg)
		print "Look module are working, turn is: %f, forward distance is: %f" %(turn_angle, max_distance)
	else:
		print "Look module are waiting for the trigger message!"

def start_lookCB(msg):
	global start_look
	start_look = msg.data
	if start_look == True:
		rospy.sleep(0.5)
		start_look = False	
	
'''
def start_look_update():
	rate = rospy.Rate(30)
	while not rospy.is_shutdown():
		if start_look = True:
			rospy.sleep()
		rate.sleep()
'''	

def look():
	rospy.init_node('look')
	rospy.Subscriber("/robot0/laser_12", LaserScan, laserCB)
	rospy.Subscriber("/whenlook/startlook", Bool, start_lookCB)
	rospy.spin()

if __name__ == '__main__':
	try:
		look()
	except rospy.ROSInterruptException:
		print "Program interrupted before completion"
