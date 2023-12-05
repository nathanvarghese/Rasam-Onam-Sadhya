#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class VelocityManipulator:
    def __init__(self):
        self.pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
        self.sub = rospy.Subscriber("/turtle1/pose", Pose, self.pose_callback)
        self.velocity_msg = Twist()

    def pose_callback(self, msg):
        if msg.x >= 7:
            self.velocity_msg.linear.x = 0
        else:
            self.velocity_msg.linear.x = 0.5

        self.pub.publish(self.velocity_msg)

class ROSCommunication:
    def __init__(self):
        self.pub = rospy.Publisher("/robot_news_radio", String, queue_size=10)
        self.sub = rospy.Subscriber("/robot_news_radio", String, self.callback)
        self.rate = rospy.Rate(2)
        self.timer = rospy.Timer(rospy.Duration(0.5), self.talker)  # Timer for talker function

    def talker(self, event):
        rospy.loginfo("Running talker") # debug line
        msg = String()
        msg.data = "Hi, this is Nathan from news radio"
        self.pub.publish(msg)

    def callback(self, msg): # callback and listener node is integrated into one
        rospy.loginfo("Running callback") # debug line
        rospy.loginfo("New message received")
        rospy.loginfo(msg)

if __name__ == '__main__':
    rospy.init_node("turtlesim_controller")
    velocity_manipulator = VelocityManipulator()
    rospy.loginfo("Running main") # debug line

    ros_communication = ROSCommunication()

    rospy.spin()
