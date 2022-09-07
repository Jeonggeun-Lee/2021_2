#!/usr/bin/env python

import sys
import rospy
from turtlesim.msg import Pose
from math import degrees, radians, sin, cos, pi
from ar_track_alvar_msgs.msg import AlvarMarker, AlvarMarkers
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Twist
from bebop_msgs.msg import Ardrone3PilotingStateAltitudeChanged
from bebop_move import Bebop2Move

TARGET_ID = int(sys.argv[1]) # argv[1] = id of target marker

LIN_SPD   = 0.125
ANG_SPD   = 0.125

TARGET_H  = 1.4

ROTATION_COEF = 0.3
ROTATION_TOLERENCE = 0.0125
LIN_Y_COEF = 1.28

class MarkerPose:

    def __init__(self):    
        rospy.init_node('recog_ar_marker')        
        rospy.Subscriber('/ar_pose_marker', AlvarMarkers, self.get_ar_pose) 
        rospy.Subscriber('/bebop/states/ardrone3/PilotingState/AltitudeChanged',\
                         Ardrone3PilotingStateAltitudeChanged,
                         self.get_alti 
                        )
        self.pub = rospy.Publisher('/bebop/cmd_vel', Twist, queue_size=10)
        self.tw  = Twist()
        
        self.theta = 0.0
        self.pos_z = 0.0
        self.pos_x = 0.0
        
        self.ref_th = 0.0
        self.ref_d  = 0.0
        
        self.alti   = 0.0
        
        self.ar_tag = AlvarMarker()
        
        self.target_found  = False
        
        
        """   
                                                 ////////////| ar_marker |////////////
                y                      z         --------+---------+---------+--------
                ^  x                   ^                 |     R-0/|\R-0    R|
                | /                    |                 |       /0|0\       |
         marker |/                     | robot           |      /  |  \      |
                +------> z    x <------+                 |     /   |   \     |
                                      /                  |  dist   |  dist   |
                                     /                   |   /     |     \   |
                                    y                    |  /      |      \  |
                                                         | /       |       \0|
                                                         |/R-0    R|R    R-0\|
        pose.x = position.z                      (0 < O) x---------+---------x (0 > 0)
        pose.y = position.x              [0]roll         ^                   ^   
        theta  = euler_from_quaternion(q)[1]pitch*       |                   |
                                         [2]yaw        robot               robot
        """        
    def get_ar_pose(self, msg):
        
        if len(msg.markers) != 0: # found marker at least 1EA
            
            for msg in msg.markers:
                
                if msg.id == TARGET_ID: # found target marker
                
                    self.ar_tag = msg
                    
                    #print("%s" %(self.ar_tag.pose.pose.position.x))
                    
                    self.target_found = True
                    
                    self.pos_x = msg.pose.pose.position.x
                    self.pos_z = msg.pose.pose.position.z
                    
                    theta = self.get_ar_theta(msg)                    
					# make theta from -90 to 90                    
                    if   theta >  radians(270): 
                        self.theta = theta - 2 * pi            
                    elif theta < -radians(270):
                        self.theta = theta + 2 * pi
                    else:
                        self.theta = theta
                    
                
    def get_ar_theta(self, msg): 
              
        """
        orientation x,y,z,w ----+
                                +--4---> +-------------------------+
        input orientaion of marker-----> |                         |
                                         | euler_from_quaternion() |
        returnned rpy of marker <------- |                         |
                                +--3---- +-------------------------+
        r,p,y angle <-----------+
                                         +------------+------------+
                                         |   marker   |   robot    |
                                         +------------+------------+
          r: euler_from_quaternion(q)[0] | roll   (x) | (y) pitch  |
        * p: euler_from_quaternion(q)[1] | pitch  (y) | (z) yaw ** | <-- 
          y: euler_from_quaternion(q)[2] | yaw    (z) | (x) roll   | 
                                         +------------+------------+
        """   
        q = (msg.pose.pose.orientation.x, msg.pose.pose.orientation.y,
             msg.pose.pose.orientation.z, msg.pose.pose.orientation.w)
             
        euler = euler_from_quaternion(q)
        theta = euler[1]
        
        # make theta from 0 to 360(deg)
        
        if theta < 0:
            theta = theta + radians(360)
        if theta > 2 * pi:
            theta = theta - radians(360)
        
        return theta
    
    
    def get_alti(self, msg):
        self.alti = msg.altitude
        
        
    def get_ref(self):
        self.ref_th = self.theta
        self.ref_d  = self.pos_z * sin(self.ref_th)
        print "theta = %s, dist = %s" %(self.ref_th, self.ref_d)
        return (self.ref_th, self.ref_d)
          

if __name__ == '__main__':
    try:        
        mp  = MarkerPose()
        bb2 = Bebop2Move()
        '''
        print "--- step1. up to target height"
        
        mp.tw.linear.z = LIN_SPD
        
        while mp.alti < TARGET_H:
            mp.pub.publish(mp.tw)
            
        print "    step1 ends"
        '''
        mp.tw.linear.z = 0.0
        mp.pub.publish(mp.tw)
        
        print "--- step2. searching target marker"
        
        mp.tw.angular.z = ANG_SPD
        
        while mp.target_found is False:
            mp.pub.publish(mp.tw)
            
        print "    step2 ends"
        
        mp.tw.angular.z = 0.0
        mp.pub.publish(mp.tw)
        
        print "--- step3. align to marker"
        
        mp.tw.angular.z = ANG_SPD
        while mp.pos_x < -0.25 or mp.pos_x > 0.25:
            mp.pub.publish(mp.tw)
            
        print "    step3 ends"
        
        mp.tw.angular.z = 0.0
        mp.pub.publish(mp.tw)
        
        (theta, dist) = mp.get_ref()
        
        print "--- step4. rotate to right angle"
        
        bb2.rotate(-theta * ROTATION_COEF, ROTATION_TOLERENCE)
            
        print "    step4 ends"
        
        print "--- step5. move to front of marker"
        
        bb2.move_y( dist * LIN_Y_COEF, 0.05)
            
        print "    step5 ends"

        print "--- step6. align to marker"
        
        mp.tw.angular.z = ANG_SPD
        while mp.pos_x < -0.25 or mp.pos_x > 0.25:
            mp.tw.angular.z = ANG_SPD
            mp.tw.angular.z *= (-mp.pos_x/abs(mp.pos_x))
            mp.pub.publish(mp.tw)
            
        print "    step6 ends"
        
        mp.tw.angular.z = 0.0
        mp.pub.publish(mp.tw)
           
        '''
        if mp.theta_ref >= 0:
            bb2.move_y( mp.dist_ref * 1.25, 0.025)
            print(mp.dist_ref)
        else:
            bb2.move_y(-mp.dist_ref * 1.25, 0.025)
            print(mp.dist_ref)
        '''
        
        #bb2.move_x(0.4, 0.05)
        
        bb2.landing()
            
        print "mission complete!!!"
        
        rospy.spin()
        
    except rospy.ROSInterruptException:  pass
