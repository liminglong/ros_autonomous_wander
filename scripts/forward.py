#!/usr/bin/env python
#coding=utf-8
import roslib
import rospy
import math

from std_msgs.msg import Bool
from geometry_msgs.msg import Twist
from subsumption_msgs.msg import Heading #messages representing the velocity command for the turn and forward module

HALT = False
linear_velocity = 0.5
angular_velocity = 1.0
idle_time = 0.5

def forwardCB(msg):
	global linear_velocity 
	global HALT
	global idle_time
	print "forwardCB start!"
	pub_twist = rospy.Publisher('/robot0/cmd_vel', Twist, queue_size = 10)
	pub_turn_reset = rospy.Publisher('/turn/reset', Bool, queue_size = 10)
	pub_busy = rospy.Publisher('/robot/busy', Bool, queue_size = 10)
	twist = Twist()
	rate = rospy.Rate(10)#10hz
	bool_msg = Bool()
	busy_msg = Bool()#message for the robot status
	print "HALT:"
	print HALT			
	#once halt, send reset to the turn
	'''
	if HALT == True:
		print "program break point 1"
		count = 0 
		#rospy.sleep(2.0 * math.pi / angular_velocity)
		twist.linear.x = linear_velocity
		pub_twist.publish(twist)
		bool_msg.data = True
		pub_turn_reset.publish(bool_msg)
		HALT = False
	'''	
	#if HALT	== False:
	print "program break point 2"
	forward_count = 0 
	while not rospy.is_shutdown():
		twist.linear.x = linear_velocity
		pub_twist.publish(twist)
		forward_count += 1
		if HALT == True:
		
			'''
			#once halt, send reset to the turn
			bool_msg.data = True
			pub_turn_reset.publish(bool_msg)
			print "turn reset message was published successfully!"
			'''
			#once halt, send stop forward to the robot
			twist.linear.x = 0.0
			pub_twist.publish(twist)
			bool_msg.data = True
			pub_turn_reset.publish(bool_msg)
			print "turn reset was published successfully in forwardCB!"
			print "robot stop, the robot hit obstacles!"
			break
		#make the robot move forward a specified distance
		elif linear_velocity * 0.1 * forward_count > msg.distance:
			forward_count = 0
			twist.linear.x = 0.0
			pub_twist.publish(twist)
			print "robot stop, the robot is idle"
			#the status is idle here
			busy_msg.data = False
			pub_busy.publish(busy_msg)
			rospy.sleep(idle_time)
			#pub return message to the Turn module
			bool_msg.data = True
			pub_turn_reset.publish(bool_msg)
			print "turn reset was published successfully in forwardCB!"
			break
		rate.sleep()

def haltCB(msg):
	global HALT
	#print "haltCB start"
	HALT = msg.data
	#pub_twist = rospy.Publisher('/robot0/cmd_vel', Twist, queue_size = 10)
	pub_turn_reset = rospy.Publisher('/turn/reset', Bool, queue_size = 10)
	if HALT == True:
		#once halt, send reset to the turn
		bool_msg = Bool()
		twist = Twist()
		bool_msg.data = True
		pub_turn_reset.publish(bool_msg)
		print "turn reset message was published successfully in haltCB!"
		
def turn():
	rospy.init_node('forward')
	rospy.Subscriber("/turn/heading", Heading, forwardCB)
	rospy.Subscriber("/collide/halt", Bool, haltCB)	
	rospy.spin()	

if __name__ == '__main__':
	try:
		turn()
	except rospy.ROSInterruptException:
		print "Program interrupted before completion"
