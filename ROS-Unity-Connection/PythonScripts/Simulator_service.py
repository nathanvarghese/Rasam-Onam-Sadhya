#!/usr/bin/env python3
import rospy
from my_custom_unity_msgs.srv import GetSimulatorStatus
#from .My_Simulator_node import characters 


def handle_get_simulator_status(req):
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
    characters_data = []
    for character in characters:
        characters_data.append(character.data)
    return characters_data

if __name__ == '__main__':
    rospy.init_node("get_simulator_status_server")
    rospy.loginfo("Get simulator status server created")
    
    service = rospy.Service("/get_simulator_status", GetSimulatorStatus, handle_get_simulator_status)
    rospy.loginfo("Service server has been started")

    rospy.spin()