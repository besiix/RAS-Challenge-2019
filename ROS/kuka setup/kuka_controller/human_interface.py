#!/usr/bin/env python

from client_lib_challenge import *
from numpy import *
import time

#The function to prase the json data to strings.
def prase_json_data(object):
	pass

#All oral words can be changed. These are not settled
def pick_up_command(string):
	if string == "pick up the hammer":
		return True
	elif string == "pick up the spanner":
		return True
	elif string == "pick up the screwdriver":
		return True


def reset_compliance_command(string):
	if string == "reset push mode":
		return True
	else: 
		return False 

def set_compliance_command(string):
	if string == "set push mode":
		return True
	else: 
		return False 

def start_pos_command(string):
	if string == "start position":
		return True
	else: 
		return False 

'''
We have several instructions: 
1. ask the robot to pass a item or items to a user
2. ask the robot to manipulate a item(including ) to different locations
'''
def drop_obj_command(string):
	if string == "place the object on default location":
		return True
	elif string == "place object on default location":
		return True
	elif string == "place the object on x location":
		return True
	elif string == "place object on x location":
		return True
	else: 
		return False


# Wait until iiwa is connected
while (not my_client.isready): pass
print('Started!!')
time.sleep(2)

# Initializing Tool
my_client.send_command('setTool demoTool')

# Initializing
my_client.send_command('setJointAcceleration 1.0')  # If the JointAcceleration is not set, the defult value is 1.0.
my_client.send_command('setJointVelocity 1.0')      # If the JointVelocity is not set, the defult value is 1.0.
my_client.send_command('setJointJerk 1.0')          # If the JointJerk is not set, the defult value is 1.0.
my_client.send_command('setCartVelocity 1000')     # If the CartVelocity is not set, the defult value is 100
my_client.send_command('resetCompliance') # If the setCompliance is not set the robot will not be in C. mode by default

# Move close to a start position.
my_client.send_command('setPosition 0 0 0 0 0 0 0') 

time.sleep(2)

objectPicked = False
my_client.Moved_to_object(False)
last_command = "none"

while True:
	#here is the logic part to judge which task or goal we want to do and 
    #complete them propertly
    length_message = len(my_client.Transcript)
    print my_client.Transcript

    if reset_compliance_command(my_client.Transcript) and last_command != "reset push mode":
        my_client.send_command('resetCompliance')
        last_command = "reset push mode"

    if set_compliance_command(my_client.Transcript) and last_command != "set push mode on":
        my_client.send_command('setCompliance 1000 1000 5000 200 200 200')
        last_command = "set push mode on"
    
    if pick_up_command(my_client.Transcript) and last_command != "pick up the object":
        if not objectPicked:
            #Getting the position from the cameara
        	if my_client.Transcript == "spanner":
        		my_client.send_command('MoveXYZABC 570 41 234 -180 2.5 -178')
        	if my_client.Transcript == "hammer":
        		my_client.send_command('MoveXYZABC 463 -62 235 -180 4.8 -178')
        	if my_client.Transcript == "screwdriver":
        		my_client.send_command('MoveXYZABC 642.37 130.48 231.78 -180 1.04 -176.37')


    #in this part, we use two kinds of commands to initiate a start position
    elif start_pos_command(my_client.Transcript) and last_command != "start position":
		my_client.send_command('setPosition 0 49.43 0 -48.5 0 82.08 0')
		my_client.send_command('setPositionXYZABC 700 0 500 -180 0 -180 ptp')
		objectPicked = False
		my_client.Moved_to_object(False)
		last_command = "start position"
    elif start_pos_command(my_client.Transcript) and last_command != "drop the object":
		my_client.send_command('setPositionXYZABC 420 396 500 -180 0 -180 ptp')
		time.sleep(1)
		my_client.send_command('setPositionXYZABC 420 396 350 -180 0 -180 ptp')
		last_command = "drop the object"
		