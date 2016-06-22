#!/usr/bin/env python
#coding=utf-8
import roslib
import rospy

from sensor_msgs.msg import Range
from std_msgs.msg import Bool

#global variables
COLLIDE_HALT_0 = False
COLLIDE_HALT_1 = False
COLLIDE_HALT_2 = False
COLLIDE_HALT_3 = False
COLLIDE_HALT_4 = False
COLLIDE_HALT_5 = False
COLLIDE_HALT_6 = False
COLLIDE_HALT_7 = False
COLLIDE_HALT_8 = False
COLLIDE_HALT_9 = False
COLLIDE_HALT_10 = False
COLLIDE_HALT_11 = False

def sonar_0CB(msg):
	global COLLIDE_HALT_0
	#print ("sonar_0 call back start!")
	if msg.range == float("-inf"):
		COLLIDE_HALT_0 = True

def sonar_1CB(msg):
	global COLLIDE_HALT_1
	#print ("sonar_1 call back start!")
	if msg.range == float("-inf"):
		COLLIDE_HALT_1 = True

def sonar_2CB(msg):
	global COLLIDE_HALT_2
	#print ("sonar_2 call back start!")
	if msg.range == float("-inf"):
		COLLIDE_HALT_2 = True
'''
def sonar_3CB(msg):
	global COLLIDE_HALT_3
	#print ("sonar_3 call back start!")
	if msg.range == float("-inf"):
		COLLIDE_HALT_3 = True

def sonar_4CB(msg):	
	global COLLIDE_HALT_4
	#print ("sonar_4 call back start!")
	if msg.range == float("-inf"):
		COLLIDE_HALT_4 = True

def sonar_5CB(msg):
	global COLLIDE_HALT_5
	#print ("sonar_5 call back start!")
	if msg.range == float("-inf"):
		COLLIDE_HALT_5 = True

def sonar_6CB(msg):
	global COLLIDE_HALT_6
	#print ("sonar_6 call back start!")
	if msg.range == float("-inf"):
		COLLIDE_HALT_6 = True

def sonar_7CB(msg):
	global COLLIDE_HALT_7
	#print ("sonar_7 call back start!")
	if msg.range == float("-inf"):
		COLLIDE_HALT_7 = True

def sonar_8CB(msg):
	global COLLIDE_HALT_8
	#print ("sonar_8 call back start!")
	if msg.range == float("-inf"):
		COLLIDE_HALT_8 = True

def sonar_9CB(msg):
	global COLLIDE_HALT_9
	#print ("sonar_9 call back start!")
	if msg.range == float("-inf"):
		COLLIDE_HALT_9 = True
'''
def sonar_10CB(msg):
	global COLLIDE_HALT_10
	#print ("sonar_10 call back start!")
	if msg.range == float("-inf"):
		COLLIDE_HALT_10 = True

def sonar_11CB(msg):
	global COLLIDE_HALT_11
	#print ("sonar_11 call back start!")
	if msg.range == float("-inf"):
		COLLIDE_HALT_11 = True
	
def collide():
	global COLLIDE_HALT_0
	global COLLIDE_HALT_1
	global COLLIDE_HALT_2
	'''	
	global COLLIDE_HALT_3
	global COLLIDE_HALT_4
	global COLLIDE_HALT_5
	global COLLIDE_HALT_6
	global COLLIDE_HALT_7
	global COLLIDE_HALT_8
	global COLLIDE_HALT_9
	'''	
	global COLLIDE_HALT_10
	global COLLIDE_HALT_11

	rospy.init_node('collide')
	rospy.Subscriber("/robot0/sonar_0", Range, sonar_0CB)
	rospy.Subscriber("/robot0/sonar_1", Range, sonar_1CB)
	rospy.Subscriber("/robot0/sonar_2", Range, sonar_2CB)
	'''
	rospy.Subscriber("/robot0/sonar_3", Range, sonar_3CB)
	rospy.Subscriber("/robot0/sonar_4", Range, sonar_4CB)
	rospy.Subscriber("/robot0/sonar_5", Range, sonar_5CB)
	rospy.Subscriber("/robot0/sonar_6", Range, sonar_6CB)
	rospy.Subscriber("/robot0/sonar_7", Range, sonar_7CB)
	rospy.Subscriber("/robot0/sonar_8", Range, sonar_8CB)
	rospy.Subscriber("/robot0/sonar_9", Range, sonar_9CB)
	'''
	rospy.Subscriber("/robot0/sonar_10", Range, sonar_10CB)
	rospy.Subscriber("/robot0/sonar_11", Range, sonar_11CB)
	pub = rospy.Publisher('/collide/halt', Bool, queue_size = 10)
	rate = rospy.Rate(10)#10hz
	halt_msg = Bool()
	while not rospy.is_shutdown():
		'''
		if (COLLIDE_HALT_0 or COLLIDE_HALT_1 or COLLIDE_HALT_2 or COLLIDE_HALT_3 or 
			COLLIDE_HALT_4 or COLLIDE_HALT_5 or COLLIDE_HALT_6 or COLLIDE_HALT_7 or 
			COLLIDE_HALT_8 or COLLIDE_HALT_9 or COLLIDE_HALT_10 or COLLIDE_HALT_11):
		'''
		if (COLLIDE_HALT_0 or COLLIDE_HALT_1 or COLLIDE_HALT_2 or COLLIDE_HALT_10 or COLLIDE_HALT_11):
			halt_msg.data = True
			pub.publish(halt_msg)
			print "The robot will be halted!"
			COLLIDE_HALT_0 = False
			COLLIDE_HALT_1 = False
			COLLIDE_HALT_2 = False
			COLLIDE_HALT_3 = False
			COLLIDE_HALT_4 = False
			COLLIDE_HALT_5 = False
			COLLIDE_HALT_6 = False
			COLLIDE_HALT_7 = False
			COLLIDE_HALT_8 = False
			COLLIDE_HALT_9 = False
			COLLIDE_HALT_10 = False
			COLLIDE_HALT_11 = False		
		else:
			halt_msg.data = False
			pub.publish(halt_msg)
			print "The robot won't be halted!"			
		rate.sleep()
	rospy.spin()

if __name__ == '__main__':
	try:
		collide()
	except rospy.ROSInterruptException:
		print "Program interrupted before completion"
