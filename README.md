# ROS-with-esp32
Here you will get to know how to make a server on esp32 using websocket and send data to it by a client which is a ros node .
Put the publisher and subscriber python files in catkin_ws/src/beginner_tutorial/script  
First run the roscore command to start the ros master 
Then run the ros node publisher using command: rosrun beginner_tutorial publisher.py . This will start the publisher node which will send data to the topic.
Run the ros node subscriber using command: rosrun beginner_tutorial subscriber.py
Upload the arduino code to the esp32. Ensure that your pc and esp are conncted to the same wifi network
open the serial monitor, you will see the data the has been send from the publisher node in it.


