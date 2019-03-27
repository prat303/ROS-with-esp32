#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import websocket


s = websocket.WebSocket()    #create socket
     #bind  socket to port & made it listen to commands


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	while True:
		s.connect("ws://192.168.0.105/") 
		print("sending")
		s.send(data.data)
		s.close()
		
	
        
def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("chatter", String, callback)
	#s.connect("ws://192.168.0.105/")
	rospy.spin()
	
   
if __name__ == '__main__':
	listener()
