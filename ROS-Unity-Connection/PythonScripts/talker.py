#!/usr/bin/env python
# license removed for brevity
import rospy
import random
from std_msgs.msg import String
from unity.msg import vector3
from unity_robotics_demo_msgs.msg import PosRot

#from unity_robotics_demo_msgs.msg import UnityColor

characters = ["Aj", "Amy", "boss", "Ch17", "clair", "david", "jose", "jose2", "megan", "peasant"]
locations = [[-15,0,15], [-15,0,-15], [15,0,15],[15,0,-15]]
import time

def talker():
    rospy.init_node('talker', anonymous=True)
    
    Aj    = rospy.Publisher('Aj', vector3, queue_size=10)
    Amy   = rospy.Publisher('Amy', vector3, queue_size=10)
    boss  = rospy.Publisher('Boss', vector3, queue_size=10)
    Ch17  = rospy.Publisher('Ch17', vector3, queue_size=10)
    clair = rospy.Publisher('Clair', vector3, queue_size=10)
    david = rospy.Publisher('David', vector3, queue_size=10)
    jose  = rospy.Publisher('Jose', vector3, queue_size=10)
    josh = rospy.Publisher('Josh', vector3, queue_size=10)
    josh2 = rospy.Publisher('Josh2', vector3, queue_size=10)
    megan = rospy.Publisher('Megan', vector3, queue_size=10)
    peasant  = rospy.Publisher('Peasant', vector3, queue_size=10)
    
    
    characters = [Aj, Amy, boss, Ch17, clair, david, jose, josh, josh2, megan, peasant]

    rate = rospy.Rate(10) # 10 hz
    while not rospy.is_shutdown():
        
        # Time topic
        rospy.loginfo("Current time %f", rospy.get_time())
        
        x = locations[0][0]
        z = locations[0][0]
        y = 0
       
        for i in range(len(characters)):
            if i <= 3:
                x = locations[0][0]
                z = locations[0][2]         
            elif 3 < i <= 4:
                x = locations[1][0]
                z = locations[1][2]
            elif 4 < i <= 5:
                x = locations[2][0]
                z = locations[2][2]
            elif i ==6:
                x = locations[3][0]
                z = locations[3][2]
                
            pos = vector3(x, y, z)
            characters[i].publish(pos)
        
            
        
        rate.sleep()
        time.sleep(10)

    
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
