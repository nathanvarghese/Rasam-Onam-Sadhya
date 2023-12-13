#!/usr/bin/env python
import rospy
from unity_robotics_demo_msgs.msg import PosRot  

class Character:
    def __init__(self, name):
        self.name = name
        self.pos_x = 0
        self.pos_y = 0
        self.pos_z = 0
        rospy.Subscriber(f"/{self.name}Location", PosRot, self.callback)

    def callback(self, data):
        self.pos_x = data.pos_x
        self.pos_y = data.pos_y
        self.pos_z = data.pos_z


def main():
    rospy.init_node('Listener_node', anonymous=True)

    characters = [
        Character('Aj'),
        Character('Amy'),
        Character('Boss'),
        Character('Ch17'),
        Character('Clair'),
        Character('David'),
        Character('Jose'),
        Character('Josh2'),
        Character('Megan'),
        Character('Peasant'),
        Character('Robot'),
        
        # Add other characters here
    ]
 
    rate = rospy.Rate(2)  # Rate of 2 Hz (0.5 seconds interval)

    while not rospy.is_shutdown():
        for character in characters:
            rospy.loginfo("This is the location of %s - pos_x: %.2f, pos_y: %.2f, pos_z: %.2f",
                          character.name, character.pos_x, character.pos_y, character.pos_z)
        rate.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
