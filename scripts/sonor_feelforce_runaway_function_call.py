#!/usr/bin/env python
#coding=utf-8
import roslib
import rospy

from sensor_msgs.msg import Range
from subsumption_msgs.msg import Force#messages representing the sum of forces
from subsumption_msgs.msg import Heading
import math
import numpy as np
#global variables
#the direction and magnitude of the forces
force_0 = [1.0, 1.0] 
force_1 = [1.0, 1.0]
force_2 = [1.0, 1.0]
force_3 = [1.0, 1.0]
force_4 = [1.0, 1.0]
force_5 = [1.0, 1.0]
force_6 = [1.0, 1.0]
force_7 = [1.0, 1.0]
force_8 = [1.0, 1.0]
force_9 = [1.0, 1.0]
force_10 = [1.0, 1.0]
force_11 = [1.0, 1.0]
max_range = 3.0#if the sensed distance is shorter than the minimum distance, assign it the parameter
min_range = 0.3#if the sensed distance is longer than the max distance, assign it the parameter
significant_force = 0.5


def sonar_0CB(msg):
	global force_0
	global max_range
	global min_range
	#print ("sonar_0 call back start!")
	if msg.range == float("inf"):
		force_0[0] = max_range
	elif msg.range == float("-inf"):
		force_0[0] = min_range
	else:
		force_0[0] = msg.range
	force_0[1] = 0.0
	#print "force_0[0]: %f; force_0[1]: %f" % (force_0[0], force_0[1])
	#print "force_0[1]: %f" % force_0[1]
def sonar_1CB(msg):
	global force_1
	global max_range
	global min_range
	#print ("sonar_1 call back start!")
	if msg.range == float("inf"):
		force_1[0] = max_range
	elif msg.range == float("-inf"):
		force_1[0] = min_range
	else:
		force_1[0] = msg.range
	force_1[1] = 30.0

def sonar_2CB(msg):
	global force_2
	global max_range
	global min_range
	#print ("sonar_2 call back start!")
	if msg.range == float("inf"):
		force_2[0] = max_range
	elif msg.range == float("-inf"):
		force_2[0] = min_range
	else:
		force_2[0] = msg.range
	force_2[1] = 60.0

def sonar_3CB(msg):
	global force_3
	global max_range
	global min_range
	#print ("sonar_3 call back start!")
	if msg.range == float("inf"):
		force_3[0] = max_range
	elif msg.range == float("-inf"):
		force_3[0] = min_range
	else:
		force_3[0] = msg.range
	force_3[1] = 90.0

def sonar_4CB(msg):
	global force_4
	global max_range
	global min_range
	#print ("sonar_4 call back start!")
	if msg.range == float("inf"):
		force_4[0] = max_range
	elif msg.range == float("-inf"):
		force_4[0] = min_range
	else:
		force_4[0] = msg.range
	force_4[1] = 120.0

def sonar_5CB(msg):
	global force_5
	global max_range
	global min_range	
	#print ("sonar_5 call back start!")
	if msg.range == float("inf"):
		force_5[0] = max_range
	elif msg.range == float("-inf"):
		force_5[0] = min_range
	else:
		force_5[0] = msg.range
	force_5[1] = 150.0

def sonar_6CB(msg):
	global force_6
	global max_range
	global min_range
	#print ("sonar_6 call back start!")
	if msg.range == float("inf"):
		force_6[0] = max_range
	elif msg.range == float("-inf"):
		force_6[0] = min_range
	else:
		force_6[0] = msg.range
	force_6[1] = 180.0

def sonar_7CB(msg):
	global force_7
	global max_range
	global min_range
	#print ("sonar_7 call back start!")
	if msg.range == float("inf"):
		force_7[0] = max_range
	elif msg.range == float("-inf"):
		force_7[0] = min_range
	else:
		force_7[0] = msg.range
	force_7[1] = 210.0

def sonar_8CB(msg):
	global force_8
	global max_range
	global min_range
	#print ("sonar_8 call back start!")
	if msg.range == float("inf"):
		force_8[0] = max_range
	elif msg.range == float("-inf"):
		force_8[0] = min_range
	else:
		force_8[0] = msg.range
	force_8[1] = 240.0

def sonar_9CB(msg):
	global force_9
	global max_range
	global min_range
	#print ("sonar_9 call back start!")
	if msg.range == float("inf"):
		force_9[0] = max_range
	elif msg.range == float("-inf"):
		force_9[0] = min_range
	else:
		force_9[0] = msg.range
	force_9[1] = 270.0

def sonar_10CB(msg):
	global force_10
	global max_range
	global min_range
	#print ("sonar_10 call back start!")
	if msg.range == float("inf"):
		force_10[0] = max_range
	elif msg.range == float("-inf"):
		force_10[0] = min_range
	else:
		force_10[0] = msg.range
	force_10[1] = 300.0

def sonar_11CB(msg):
	global force_11
	global max_range
	global min_range
	#print ("sonar_11 call back start!")
	if msg.range == float("inf"):
		force_11[0] = max_range
	elif msg.range == float("-inf"):
		force_11[0] = min_range
	else:
		force_11[0] = msg.range
	force_11[1] = 330.0

 
def polar_coordinates_sum(coordinates0 = [1.0, 1.0], coordinates1 = [1.0, 1.0], coordinates2 = [1.0, 1.0], coordinates3 = [1.0, 1.0], 
						  coordinates4 = [1.0, 1.0], coordinates5 = [1.0, 1.0], coordinates6 = [1.0, 1.0], coordinates7 = [1.0, 1.0], 
						  coordinates8 = [1.0, 1.0], coordinates9 = [1.0, 1.0], coordinates10 = [1.0, 1.0], coordinates11 = [1.0, 1.0]):
	
	coordinates_sum = [1.0, 1.0]

	rho = [1.0 for i in range(12)]
	theta = [1.0 for j in range(12)]  	

	rectangular_coordinates_sum_x = 0.0
	rectangular_coordinates_sum_y = 0.0

	rho[0] = 1 / (coordinates0[0] ** 2)
	rho[1] = 1 / (coordinates1[0] ** 2)
	rho[2] = 1 / (coordinates2[0] ** 2)
	rho[3] = 1 / (coordinates3[0] ** 2)
	rho[4] = 1 / (coordinates4[0] ** 2)
	rho[5] = 1 / (coordinates5[0] ** 2)
	rho[6] = 1 / (coordinates6[0] ** 2)
	rho[7] = 1 / (coordinates7[0] ** 2)
	rho[8] = 1 / (coordinates8[0] ** 2)
	rho[9] = 1 / (coordinates9[0] ** 2)
	rho[10] = 1 / (coordinates10[0] ** 2)
	rho[11] = 1 / (coordinates11[0] ** 2)
	
	theta[0] = math.pi * coordinates0[1] / 180.0
	theta[1] = math.pi * coordinates1[1] / 180.0
	theta[2] = math.pi * coordinates2[1] / 180.0
	theta[3] = math.pi * coordinates3[1] / 180.0
	theta[4] = math.pi * coordinates4[1] / 180.0
	theta[5] = math.pi * coordinates5[1] / 180.0
	theta[6] = math.pi * coordinates6[1] / 180.0
	theta[7] = math.pi * coordinates7[1] / 180.0
	theta[8] = math.pi * coordinates8[1] / 180.0
	theta[9] = math.pi * coordinates9[1] / 180.0
	theta[10] = math.pi * coordinates10[1] / 180.0
	theta[11] = math.pi * coordinates11[1] / 180.0

	for i in range(0, 11):
		rectangular_coordinates_sum_x += rho[i] * math.cos(theta[i])
		rectangular_coordinates_sum_y += rho[i] * math.sin(theta[i])

	rectangular_coordinates_sum_x = (-1) * rectangular_coordinates_sum_x
	rectangular_coordinates_sum_y = (-1) * rectangular_coordinates_sum_y
	
	coordinates_sum[0] = math.sqrt(rectangular_coordinates_sum_x ** 2 + rectangular_coordinates_sum_y ** 2)	/ 12.0 #devided by 12 to avoid the result distance to be too large 
	coordinates_sum[1] = (np.arctan2(rectangular_coordinates_sum_y, rectangular_coordinates_sum_x) + 2 * math.pi) % (2 * math.pi)

	print "coordinates_sum[0]: %f" % coordinates_sum[0]	
	print "coordinates_sum[1]: %f" % coordinates_sum[1]
	return coordinates_sum

def sum_feelforce():
	rospy.init_node('feelforce')
	rospy.Subscriber("/robot0/sonar_0", Range, sonar_0CB)
	rospy.Subscriber("/robot0/sonar_1", Range, sonar_1CB)
	rospy.Subscriber("/robot0/sonar_2", Range, sonar_2CB)
	rospy.Subscriber("/robot0/sonar_3", Range, sonar_3CB)
	rospy.Subscriber("/robot0/sonar_4", Range, sonar_4CB)
	rospy.Subscriber("/robot0/sonar_5", Range, sonar_5CB)
	rospy.Subscriber("/robot0/sonar_6", Range, sonar_6CB)
	rospy.Subscriber("/robot0/sonar_7", Range, sonar_7CB)
	rospy.Subscriber("/robot0/sonar_8", Range, sonar_8CB)
	rospy.Subscriber("/robot0/sonar_9", Range, sonar_9CB)
	rospy.Subscriber("/robot0/sonar_10", Range, sonar_10CB)
	rospy.Subscriber("/robot0/sonar_11", Range, sonar_11CB)
    #TODO:问题是能不能保证上面的每一个消息触发的回调函数都执行一次？
	#print ("Feelforce force publish start!")
	#pub = rospy.Publisher('/feelforce/force', Force, queue_size = 10)
	#rate = rospy.Rate(10)
    temp_sum = [1.0, 1.0]
	temp_sum = polar_coordinates_sum(force_0, force_1, force_2, force_3,
									force_4, force_5, force_6, force_7, 
									force_8, force_9, force_10, force_11)
	force_msg = Force()
	force_msg.magnitude = temp_sum[0]
	force_msg.direction = temp_sum[1]
    return force_msg
	#pub.publish(force_msg)在这里把消息发布变成函数调用
 	print ("Feelforce force message was published successfully!")
    '''
	while not rospy.is_shutdown():
		temp_sum = [1.0, 1.0]
		temp_sum = polar_coordinates_sum(force_0, force_1, force_2, force_3,
							  			 force_4, force_5, force_6, force_7, 
							  			 force_8, force_9, force_10, force_11)
		force_msg = Force()
		force_msg.magnitude = temp_sum[0]
		force_msg.direction = temp_sum[1]
		pub.publish(force_msg)
 		print ("Feelforce force message was published successfully!")
		rate.sleep()
    '''
	#TODO：rospy.spin()#rospy.spin()还要不要加在这里面啊？
    
def runawayCB():
	global significant_force
	heading_msg = Heading()
	pub = rospy.Publisher('/runaway/heading', Heading, queue_size = 10)
    msg = sum_feelforce() #函数调用在这里实现
	heading_msg.distance = msg.magnitude
	heading_msg.angle = msg.direction 
	if heading_msg.distance > significant_force:
		pub.publish(heading_msg)
	print "heading_msg was published successfully!"    

if __name__ == '__main__':
	try:
		#sum_feelforce()这里的主函数要变化？
	except rospy.ROSInterruptException:
		print "Program interrupted before completion"
