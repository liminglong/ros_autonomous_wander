#!/usr/bin/env python
#coding=utf-8
import roslib
import rospy


from std_msgs.msg import Bool

def halt_test():
	rospy.init_node('halt_test')
	bool_msg = Bool()
	bool_msg.data = True
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		pub_halt = rospy.Publisher('/collide/halt', Bool, queue_size = 10)
		print 'published successfully!'
		rate.sleep()
		pub_halt.publish(bool_msg)

if __name__ == '__main__':
	try:
		halt_test()
	except rospy.ROSInterruptException:
		print "Program interrupted before completion"
