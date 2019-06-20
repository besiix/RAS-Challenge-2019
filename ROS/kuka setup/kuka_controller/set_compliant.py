#!/usr/bin/env python

# KUKA API for ROS

# Marhc 2016 Saeid Mokaram  saeid.mokaram@gmail.com
# Sheffield Robotics    http://www.sheffieldrobotics.ac.uk/
# The university of sheffield   http://www.sheffield.ac.uk/

# This script generats a ROS node for comunicating with KUKA iiwa
# Dependencies: conf.txt, ROS server, Rospy, KUKA iiwa java SDK, KUKA iiwa robot.

# This application is intended for floor mounted robots.
#######################################################################################################################
from client_lib import *

import time
# Making a connection object.
my_client = kuka_iiwa_ros_client()


# Wait until iiwa is connected zzz!
while (not my_client.isready):
	pass
print('Started!')

# Initializing Tool 1
my_client.send_command('setTool tool1')

# Initializing
my_client.send_command('setJointAcceleration 1.0')  # If the JointAcceleration is not set, the defult value is 1.0.
my_client.send_command('setJointVelocity 1.0')      # If the JointVelocity is not set, the defult value is 1.0.
my_client.send_command('setJointJerk 1.0')          # If the JointJerk is not set, the defult value is 1.0.
my_client.send_command('setCartVelocity 10000')     # If the CartVelocity is not set, the defult value is 100

# Move close to a start position.
time.sleep(1)
my_client.send_command('setPosition 0 0 0 -90 0 90 0')
time.sleep(10)
#m
my_client.send_command('setCompliance 10 10 100 300 200 200')
time.sleep(1)
	