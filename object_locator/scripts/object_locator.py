#!/usr/bin/env python
import sys
import subprocess
import json
import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String
from sensor_msgs.msg import Image


class object_locator:

	#============================= CONSTRUCTOR ================================
	def __init__(self):
		self.location_pub = rospy.Publisher('control', String, queue_size=10)
		self.kinect_sub = rospy.Subscriber('/kinect2/sd/image_color_rect', Image, self.kinect_callback)
		self.nlp_sub = rospy.Subscriber("nlp", String, self.nlp_callback)
		print("Publisher and subscribers set.")

		self.bridge = CvBridge()
		self.image_path = "~/Pictures/kinect_color.jpeg"
		print("Image path set: " + self.image_path)

	#============================ LOCATE OBJECT ===============================
	''' Return position of request object '''
	def locate_object(self, object_name):
		
		print("Image sending, looking for " + object_name)
		response = eval("subprocess.getoutput('curl --insecure -i -F files=@%s https://amrcac922.shef.ac.uk/powerai-vision/api/dlapis/dc89d0e0-57bf-4657-9d10-510d05e2485f')", self.image_path)
		
		print("Received response, processing...")		
		output = response.split("\n\n")
		output = json.loads(output[-1:][0])		
		detected = output['classified']

		for instance in detected:
			if instance['label'] == object_name:
				print(object_name + " found!")
				return instance
		print(object_name + " not found.")
		return []

	#============================ DETECT OBJECTS ==============================
	''' Callback for kinect - writes image to file '''
	def kinect_callback(self, data):
		print("CALLBACK: kinect_callback")
		try:
			cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
			print("Writing image to: " + self.image_path)
			cv2.imwrite(self.image_path, cv_image)
			cv2.imshow("Viewer", cv_image)
			cv2.waitKey(1000)
		except CvBridgeError as e:
			print(e)
			

	#============================ DETECT OBJECTS ==============================
	''' Callback for NLP - find location of object name in string '''
	def nlp_callback(self, object_name):
		print("CALLBACK: nlp_callback")
		print("I heard %s", object_name.data)
		location = locate_object(object_name.data)
		print(location)
		self.location_pub.publish(location)



def main(args):
	print("Starting object locator...")
	rospy.init_node('vision', anonymous=True)
	obj_find = object_locator()
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main(sys.argv)
