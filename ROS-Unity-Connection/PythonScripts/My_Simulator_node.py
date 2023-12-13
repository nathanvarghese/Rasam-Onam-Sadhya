#!/usr/bin/env python
import rospy
from unity_robotics_demo_msgs.msg import PosRot
from my_custom_unity_msgs.msg import SimulatorStatus


class Character:
    def __init__(self, name):
        self.name = name
        self.data = SimulatorStatus()  # Create an instance of your custom message type
        rospy.Subscriber(f"/{self.name}Location", PosRot, self.callback)

    def callback(self, data):
        self.data.name = self.name
        self.data.pos_x = data.pos_x
        self.data.pos_y = data.pos_y
        self.data.pos_z = data.pos_z
        self.data.debug_message = "Running well"

def main():
    rospy.init_node("simulator_status_publisher")
    pub = rospy.Publisher("/my_simulator_status", SimulatorStatus, queue_size=10)
    rate = rospy.Rate(5)

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
        #Character('Robot'),
        # Add other characters here
    ]

    def publish_data():
        characters_data = []  # Clear the array before filling it again
        for character in characters:
            characters_data.append(character.data)
            
        rospy.loginfo("Characters Data: %s", characters_data)
        
        # Publish the characters_data
        for character_data in characters_data:
            pub.publish(character_data)

    while not rospy.is_shutdown():
        publish_data()
        rate.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
