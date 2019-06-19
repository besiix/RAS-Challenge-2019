import subprocess
import json
import rospy
from std_msgs.msg import String


''' Get json string detection of image sent '''
def detect_objects():
	response = eval("subprocess.getoutput('curl --insecure -i -F files=@C:/Users/me1spw/Downloads/test.jpg https://amrcac922.shef.ac.uk/powerai-vision/api/dlapis/dc89d0e0-57bf-4657-9d10-510d05e2485f')")
	output = response.split("\n\n")
	output = json.loads(output[-1:][0])

	return output['classified']


''' Return position of request object '''
def locate_object(target):
	#TO-DO: take photo and pass to detect_objects()
	detected = detect_objects()

	for instance in detected:
		if instance['label'] == target:
			return instance
	return []

#============================== PUBLISHER =====================================
def vision():
	pub = rospy.Publisher('control', String, queue_size=10)
	rospy.init_node('vision', anonymous=True)
	rospy.Subscriber('/kinect2/hd/color', String, kinect_callback)
	rospy.Subscriber("nlp", String, nlp_callback)

	rate = rospy.Rate(10) # 10hz
	
	while not rospy.is_shutdown():
		rate.sleep()

#============================= LISTENER =======================================
def nlp_callback(object_to_detect):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", object_to_detect.data)
    location = locate_object(object_to_detect.data)
    pub.publish(location)

#================================ MAIN ========================================
if __name__ == '__main__':
	try:
		vision()
	except rospy.ROSInterruptException:
		pass