import subprocess
import json
import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String
from sensor_msgs.msg import Image


class object_locator:

	def __init__(self):
		self.location_pub = rospy.Publisher('control', String, queue_size=10)
		self.kinect_sub = rospy.Subscriber('/kinect2/hd/image_color', Image, kinect_callback)
		self.nlp_sub = rospy.Subscriber("nlp", String, nlp_callback)
		self.bridge = CvBridge()
		

	''' Get json string detection of image sent '''
	def detect_objects(image_path):
		image_path = "kinect_color.jpg"
		response = eval("subprocess.getoutput('curl --insecure -i -F files=@%s https://amrcac922.shef.ac.uk/powerai-vision/api/dlapis/dc89d0e0-57bf-4657-9d10-510d05e2485f')", image_path)
		output = response.split("\n\n")
		output = json.loads(output[-1:][0])

		return output['classified']


	''' Return position of request object '''
	def locate_object(target_name):
		detected = detect_objects()

		for instance in detected:
			if instance['label'] == target_name:
				return instance
		return []


	''' Callback for kinect - writes image to file '''
	def kinect_callback(self, data):
		try:
			cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
		except CvBridgeError as e:
			print(e)
		else:
			cv2.imwrite('kinect_color.jpg', cv2_img)
		cv2.waitKey(1000)


	''' Callback for NLP - find location of object name in string '''
	def nlp_callback(self, object_name):
		print("I heard %s", object_name.data)
		self.location_pub.publish(locate_object(object_name.data))


def main(args):
	obj_find = object_locator()
	rospy.init_node('vision', anonymous=True)

	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main(sys.argv)
