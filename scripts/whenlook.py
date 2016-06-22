#!/usr/bin/env python
#coding=utf-8
import roslib
import rospy

from std_msgs.msg import Bool

def status_busyCB(msg):
	pub_startlook = rospy.Publisher('/whenlook/startlook', Bool, queue_size=10)		
	if msg.data == False:
		startlook_msg = Bool()
		startlook_msg.data = True	
		pub_startlook.publish(startlook_msg)

def whenlook():
	rospy.init_node('whenlook')
	rospy.Subscriber("/status/busy", Bool, status_busyCB)	
	rospy.spin()	

if __name__ == '__main__':
	try:
		whenlook()
	except rospy.ROSInterruptException:
		print "Program interrupted before completion"
