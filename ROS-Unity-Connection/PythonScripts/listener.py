#!/usr/bin/env python
import rospy
from unity_robotics_demo_msgs.msg import PosRot
import matplotlib.pyplot as plt
import numpy as np


import time
  
Starttime = time.time()
# Generate some random data
x = []
y = []

def callback(data):
    x.append(int(data.pos_x) +15)
    y.append(int(data.pos_z)+15)
    #print(x,y)
    #laptime = round((time.time() - Starttime), 2)
    #if laptime > 300:
        #print("printing the heat map")
        # Create a hexbin plot
        #plt.hexbin(x, y, gridsize=20, cmap='inferno', bins='log', mincnt=1)

            # Add a colorbar
        #plt.colorbar()

        # Set the axis labels and title
        #plt.xlabel('X coordinate')
        #plt.ylabel('Y coordinate')
        #plt.title('Heatmap based on X-Y coordinates')
        #plt.show()
        #exit(0)
        #return 0

    
def listener():
    rospy.init_node('listener', anonymous=True)
    
    
    Aj_location = rospy.Subscriber("AjLocation", PosRot, callback)
    print("This is the location of Aj %s"  %Aj_location)


    rospy.Subscriber("AmyLocation", PosRot, callback)
    rospy.Subscriber("BossLocation", PosRot, callback)
    rospy.Subscriber("Ch17Location", PosRot, callback)
    rospy.Subscriber("ClairLocation", PosRot, callback)
    rospy.Subscriber("DavidLocation", PosRot, callback)
    rospy.Subscriber("JoseLocation", PosRot, callback)
    rospy.Subscriber("Josh2Location", PosRot, callback)
    rospy.Subscriber("MeganLocation", PosRot, callback)
    rospy.Subscriber("PeasantLocation", PosRot, callback)
    rospy.Subscriber("RobotLocation", PosRot, callback)


    rospy.spin()

if __name__ == '__main__':
    listener()
    

