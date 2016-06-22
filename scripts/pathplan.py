#!/usr/bin/env python
#coding=utf-8
import roslib
import rospy

from std_msgs.msg import Bool
from subsumption_msgs.msg import Heading
from subsumption_msgs.msg import Path

#global variables
start_pathplan = False

def look_pathCB(msg):
	global start_pathplan
	if start_pathplan == True:
		pub_heading = rospy.Publisher('/pathplan/suppressor', Heading, queue_size=10)
		heading_msg = Heading()
		heading_msg.angle = msg.path_angle
		heading_msg.distance = msg.path_distance
		pub_heading.publish(heading_msg)
		print "pathplan module is working, path_angle: %f; path_distance %f" % (heading_msg.angle, heading_msg.distance)	
	else:
		print "pathplan module is sleeping"
	

def start_lookCB(msg):
	global start_pathplan
	start_pathplan = msg.data
	if start_pathplan == True:
		rospy.sleep(0.5)
		start_pathplan = False	

def pathplan():
	rospy.init_node('pathplan')
	rospy.Subscriber("/look/path", Path, look_pathCB)
	rospy.Subscriber("/whenlook/startlook", Bool, start_lookCB)	
	rospy.spin()	

if __name__ == '__main__':
	try:
		pathplan()
	except rospy.ROSInterruptException:
		print "Program interrupted before completion"
