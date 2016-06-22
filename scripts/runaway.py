#!/usr/bin/env python
#coding=utf-8
import roslib
import rospy

from subsumption_msgs.msg import Force #messages representing the sum of resultant forces
from subsumption_msgs.msg import Heading #messages representing the velocity command for the turn and forward module

#global variables
significant_force = 0.5

def runawayCB(msg):
	global significant_force
	heading_msg = Heading()
	pub = rospy.Publisher('/runaway/heading', Heading, queue_size = 10)
	heading_msg.distance = msg.magnitude
	heading_msg.angle = msg.direction 
	print "heading_msg.distance %f" % heading_msg.distance
	print "heading_msg.angle %f" % heading_msg.angle
	if heading_msg.distance > significant_force:
		pub.publish(heading_msg)
	print "heading_msg was published successfully!"

def runaway():
	rospy.init_node('runaway')
	rospy.Subscriber("/feelforce/force", Force, runawayCB)
	rospy.spin()
	
if __name__ == '__main__':
	try:
		runaway()
	except rospy.ROSInterruptException:
		print "Program interrupted before completion"
