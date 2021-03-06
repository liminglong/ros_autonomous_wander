#!/usr/bin/env python
#coding=utf-8
import roslib
import rospy
import time

from subsumption_msgs.msg import Heading 
from std_msgs.msg import Bool
time_unit = 0.1#time unit is dicided by the sonar message publishing frequency(10hz)
time_unit_amount = 75
time_start = 0.0

def whenlook_startlookCB(msg):
	global time_start
	time_start = time.time()
	print "The upper layer are working"	

def wander_headingCB(msg):
	global time_unit
	global time_unit_amount
	global time_start
	time_end = time.time()
	pub_heading = rospy.Publisher('/wander/heading', Heading, queue_size=10)	
	if (time_end - time_start) > (time_unit * time_unit_amount):
		pub_heading.publish(msg)
		print "The upper layer didn't work, the lower layer instead!"

def avoid_runaway_suppressor():
	rospy.init_node('whenlook_wander_inhibitor')
	rospy.Subscriber("/whenlook/startlook", Bool, whenlook_startlookCB)	
	rospy.Subscriber("/wander/inhibitor/heading", Heading, wander_headingCB)
	rospy.spin()

if __name__ == '__main__':
	try:
		avoid_runaway_suppressor()
	except rospy.ROSInterruptException:
		print "Program interrupted before completion"
