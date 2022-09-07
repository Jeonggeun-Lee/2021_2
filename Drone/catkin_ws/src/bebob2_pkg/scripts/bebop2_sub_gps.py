#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from bebop_msgs.msg import Ardrone3PilotingStatePositionChanged
from bebop_msgs.msg import Ardrone3PilotingStateAltitudeChanged
 


class SubGPS():

    def __init__(self):
    
        rospy.init_node('sub_altitude')
        
        rospy.Subscriber('/bebop/states/ardrone3/PilotingState/PositionChanged',\
                         Ardrone3PilotingStatePositionChanged,
                         self.get_pos
                        )

        rospy.Subscriber('/bebop/states/ardrone3/PilotingState/AltitudeChanged',\
                         Ardrone3PilotingStateAltitudeChanged,
                         self.get_alti 
                        )
        self.lati = 0.0        
        self.long = 0.0        
        self.alti = 0.0
        
    
    def get_pos(self, msg):
        self.long = msg.longitude
        self.lati = msg.latitude
        print("latitude = %s(m)" %(self.lati))
        print("longitude = %s(m)" %(self.long))
    def get_alti(self, msg):
        self.alti = msg.altitude
        print("altitude = %s(m)" %(self.alti))
        

if __name__ == '__main__': 
    try:
        SubGPS()
        rospy.spin()
 
    except rospy.ROSInterruptException:
        pass
