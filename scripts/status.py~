#!/usr/bin/env python
#coding=utf-8
import roslib
import rospy

from std_msgs.msg import Bool

def forward_busyCB(msg):
	pub_status = rospy.Publisher('/status/busy', Bool, queue_size=10)		
	count = 0
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		pub_status.publish(msg)
		count += 1		
		rate.sleep()
		if count == 5:#'5' is decided by the frequency of status publisher 
			count = 0
			break


def status():
	rospy.init_node('status')
	rospy.Subscriber("/robot/busy", Bool, forward_busyCB)	
	rospy.spin()	

if __name__ == '__main__':
	try:
		status()
	except rospy.ROSInterruptException:
		print "Program interrupted before completion"
