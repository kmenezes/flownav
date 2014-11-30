from flownav.msg import ttc
import rospy

class DataLogger(object):
    def __init__(self,topic="/flownav/data"):
        self.publisher = rospy.Publisher(topic, ttc, queue_size=10)
        
    def write(self,msg):
        self.publisher.publish(msg)
