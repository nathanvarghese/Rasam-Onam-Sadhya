#!usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class velocity_manipulator:

    def __init__(self):
        #pub_topic_name = "/turtle1/cmd_vel"
        #sub_topic_name = "/turtle1/pose"
        
        self.pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size = 10)
        self.sub = rospy.Subscriber("/turtle1/pose", Pose, self.pose_callback)
        self.velocity_msg = Twist() # Assigned velocity_msg to Twist function
        
    def pose_callback(self,msg):
        if (msg.x >= 7):
            ## Stopping condition
            self.velocity_msg.linear.x = 0
        else :
            self.velocity_msg.linear.x = 0.5

        self.pub.publish(self.velocity_msg)



if __name__ == '__main__':

    rospy.init_node("turtlesim_controller")
    velocity_manipulator()
    rospy.spin()



