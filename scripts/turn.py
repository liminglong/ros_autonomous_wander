#!/usr/bin/env python
#coding=utf-8
import roslib
import rospy
import math

from std_msgs.msg import Bool
from geometry_msgs.msg import Twist
from subsumption_msgs.msg import Heading #messages representing the velocity command for the turn and forward module

RESET = True
angular_velocity = 1.0
turn_frequency = 50 #hz

def turnCB(msg):
	global RESET
	global angular_velocity
	global turn_frequency
	#print "turnCB start!"
	pub_twist = rospy.Publisher('/robot0/cmd_vel', Twist, queue_size = 10)
	pub_heading = rospy.Publisher('/turn/heading', Heading, queue_size = 10)
	turn_angle = 0.0
	turn_angle = msg.angle
	if RESET == True:
		print "turn reset start"
		rate = rospy.Rate(turn_frequency) #50hz
		twist = Twist()
		#turn left or turn right
		if turn_angle == 0.0 or (turn_angle > 0.0 and turn_angle < math.pi) or turn_angle == math.pi:
			twist.angular.z = angular_velocity
			count = 0 
			print "turn angle is %f" %turn_angle
			while not rospy.is_shutdown():
				#any commands sent to the Turn module during transit are lost
				pub_twist.publish(twist)
				count += 1
				rate.sleep()
				if (1.0 / turn_frequency) * count * angular_velocity > turn_angle:
					twist.angular.z = 0 
					pub_twist.publish(twist)
					print "robot turn stop message was published successfully!"
					break
			count = 0
		else:
			twist.angular.z = (-1.0) *angular_velocity
			count = 0 
			print "turn angle is %f" %turn_angle
			while not rospy.is_shutdown():
				#any commands sent to the Turn module during transit are lost
				pub_twist.publish(twist)
				count += 1
				rate.sleep()
				if (1.0 / turn_frequency) * count * angular_velocity > (2 * math.pi - turn_angle):
					twist.angular.z = 0 
					pub_twist.publish(twist)
					print "robot turn stop message was published successfully!"
					break
			count = 0
		print "turn reset stop"
		pub_heading.publish(msg)
		print "heading message was published successfully to forward module!"
	RESET = False

def resetCB(msg):
	global RESET
	RESET = msg.data
	print 'RESET:'
	print RESET

def turn():
	rospy.init_node('turn')
	rospy.Subscriber("/runaway/heading", Heading, turnCB)
	rospy.Subscriber("/turn/reset", Bool, resetCB)	
	rospy.spin()
	
if __name__ == '__main__':
	try:
		turn()
	except rospy.ROSInterruptException:
		print "Program interrupted before completion"
