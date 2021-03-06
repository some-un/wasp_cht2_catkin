#!/usr/bin/env python

# A basic front controller to be used with the PID controller. Based on the drone controller class for the tutorial "Up and flying with the AR.Drone and ROS | Getting Started"
# https://github.com/mikehamer/ardrone_tutorials_getting_started

# This class implements the pid2plant part in the control loop

# Import the ROS libraries, and load the manifest file which through <depend package=... /> will give us access to the project dependencies
import roslib
import rospy
import sys
roslib.load_manifest('drone')

# Import the messages we're interested in sending and receiving
from geometry_msgs.msg import Twist  	 # for sending commands to the drone
from std_msgs.msg import Float64	 # for the control_effort
from nav_msgs.msg import Odometry
import tf
import math

# Global variable for the cmd/vel publisher command

global command
command = Twist()

global ce_pitch
global ce_roll
ce_pitch = 0
ce_roll = 0
global curr_angle
curr_angle = 0

# Method that applies the yaw signal (theta)
def ApplyControlEffort_Yaw(controlEffort):
	global command
	yaw_velocity=controlEffort.data
	command.angular.z = yaw_velocity
	#pubCmdTo_drone.publish(command)
	#PrintCommands()

# Method that applies the pitch signal (x)
def ApplyControlEffort_Pitch(controlEffort):
	#global command
	global ce_pitch	
	#pitch =  controlEffort.data
	#command.linear.x  = pitch
	
	#pubCmdTo_drone.publish(command)
	#PrintCommands()
	ce_pitch = controlEffort.data


# Method that applies the roll signal (y)
def ApplyControlEffort_Roll(controlEffort):
	#global command
	global ce_roll
	# The negative roll is applied because of the coordinate system
	#roll =  controlEffort.data	
	#command.linear.y  = -roll
	#pubCmdTo_drone.publish(command)
	#PrintCommands()

	ce_roll = controlEffort.data

# Method that applies the altitude signal (z)
def ApplyControlEffort_Altitude(controlEffort):
	global command

	alt = controlEffort.data
	command.linear.z = alt
	#pubCmdTo_drone.publish(command)
	#PrintCommands()

# Print the applied signals
def PrintCommands():
	global command
	global curr_angle
	print("Applying Control Effort \n\tX \t\tY \t\tZ \t\tYaw")
	print(str("{:10.4f}".format(command.linear.x)) + " \t" + str("{:10.4f}".format(command.linear.y)) +"\t" + str("{:10.4f}".format(command.linear.z)) +"\t" + str("{:10.4f}".format(command.angular.z)) + "\n")
	print "Curr angle: "+ str(curr_angle)
		  
	

def UpdateAngle(pos):
	global curr_angle
	pose = pos.pose.pose

	quaternion = (
		pose.orientation.x,
    		pose.orientation.y,
    		pose.orientation.z,
    		pose.orientation.w)

	euler = tf.transformations.euler_from_quaternion(quaternion)

	curr_angle = euler[2]


# Setup the application
if __name__=='__main__':
	global command
	# Drone id in order to set up topics
	if (len(sys.argv)<=1):
		id = '0'
	else:
		id = str(sys.argv[1])

	# Firstly we setup a ros node, so that we can communicate with the other packages
	rospy.init_node('drone'+id+'pid2plant')

	# Topic that listens to the desired applied yaw signal
	rospy.Subscriber('/drone'+id+'/control_effort_slam_yaw/',Float64,ApplyControlEffort_Yaw)
	
	# Topic that listens to the desired applied y signal (yaw)
	rospy.Subscriber('/drone'+id+'/control_effort_slam_y/',Float64,ApplyControlEffort_Pitch)
	
	# Topic that listens to the desired applied x signal (pitch)
	rospy.Subscriber('/drone'+id+'/control_effort_slam_x/',Float64,ApplyControlEffort_Roll)
	
	# Topic that listens to the desired applied z signal (altitude)
	rospy.Subscriber('/drone'+id+'/control_effort_slam_z/',Float64,ApplyControlEffort_Altitude)
	

	rospy.Subscriber('/drone'+id+'/global/pos', Odometry, UpdateAngle)

	# Topic that we publish to the drone for control
	global pubCmdTo_drone
	pubCmdTo_drone = rospy.Publisher('drone'+id+'/cmd_vel', Twist, queue_size=1)

	print "Launched pid2plant for drone"+id
	#This keeps the function active till node are shurdown.
	
	r = rospy.Rate(100)
	while not rospy.is_shutdown():
		command.linear.x = (ce_pitch*math.cos(curr_angle)-ce_roll*math.sin(curr_angle))
		command.linear.y = -(ce_roll*math.cos(curr_angle)+ce_pitch*math.sin(curr_angle))

		#command.linear.x = ce_pitch
		#command.linear.y = -ce_roll
		pubCmdTo_drone.publish(command)
		PrintCommands()
		r.sleep()

	
	#rospy.spin()
