#!/usr/bin/env python

from client_lib_challenge import *
import time

# Initiate a connection object.
my_client = kuka_iiwa_ros_client()

''' TODO list:  we have not be sure that the overall limition for all directions
'''
#This function can be used in the testing part to avoid some risk commands.
'''
def verbal_command(X,Y,Z, A,B,C):
    if Z > 650:
	    Z = 650
	if Z < 150:
	    Z = 150
	if Y > 750:
		Y = 750
	if Y < -100:
		Y = -100
    verbal_string = 'setPositionXYZABC ' + str(X) + ' ' + str(Y) + ' ' +str(Z) + ' ' + str(A)\
     + ' ' + str(B) + ' ' +str(C) +' ptp'
    print verbal_string
	my_client.send_command(verbal_string)
'''


#judge if the kuka node is initiated
while (not my_client.isready): pass
print('Started!!')
time.sleep(2)

# Initializing Demo01
my_client.send_command('setTool demo01')

# Initializing
my_client.send_command('setJointAcceleration 1.0')  # If the JointAcceleration is not set, the defult value is 1.0.
my_client.send_command('setJointVelocity 1.0')      # If the JointVelocity is not set, the defult value is 1.0.
my_client.send_command('setJointJerk 1.0')          # If the JointJerk is not set, the defult value is 1.0.
my_client.send_command('setCartVelocity 10000')     # If the CartVelocity is not set, the defult value is 100

#uncomment this test a simple move of the arm
#Move close to a start position. 
my_client.send_command('setPosition 0 0 0 0 0 0 0')
time.sleep(2)
my_client.send_command('setPosition 0 49.43 0 -48.5 0 82.08 0')

while True:
	pass

#initial command is no command.
'''achieved_command='none'
while True:
    #This is the start position, we have to find a good state of the arm.
    if (my_client.Transcript)== "start position" and last_command != "start position":
		my_client.send_command('setPosition 80 -30 0 60 0 90 0')
        #my_client.send_command('setPosition 10 -45 -10 -80 7 55 0')
		last_command =  my_client.Transcript

    #All valuabes are set to zeros.
	if (my_client.Transcript)== "mechanical zero position" and last_command != "mechanical zero position":
		my_client.send_command('setPosition 0 0 0 0 0 0 0')
		last_command =  my_client.Transcript
'''

