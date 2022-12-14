#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy, sys
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
from bebop_msgs.msg import Ardrone3PilotingStateAttitudeChanged, \
                           Ardrone3PilotingStatePositionChanged, \
                           Ardrone3PilotingStateAltitudeChanged
#from scipy import sqrt, cos, sin, arctan2, pi
from math import sqrt, cos, sin, pi, atan2
from math import degrees, radians
from bebop_move import Bebop2Move

USE_SPHINX = bool(int(sys.argv[1]))
'''
    GPS for center of map  (  37.4089445,  126.691189833 )  인천 인력개발원
    Parot-Sphinx start GPS (  48.8789000,    2.367780000 )
    diffrence              ( -11.4699555, +124.323409833 )
'''
OFFSET_LAT = -11.469955500
OFFSET_LON = 124.323409833

LIN_SPD    =   0.55 * 4
ANG_SPD    =   0.25 * pi *4

FLIGHT_ALT =   4.0

DEG_PER_M  =   0.00000899320363721
'''
                               p2 (lat2,lon2)
                       | | |   /         
                       | | |  / 
                       | | |0/  
                       | | |/              
                       | |0/    
                       | |/      
                       |0/<--- bearing         
                       |/________     
                       p1 (lat1,lon1)
                       
  when center is (a,b), equation of circle : pow((x-a),2) + pow((y-b),2) = pow(r,2)
'''
class Move2GPS:
    
    def __init__(self):
        rospy.init_node('bb2_move_to_gps', anonymous = True)
        
        rospy.Subscriber('/bebop/states/ardrone3/PilotingState/AttitudeChanged',
                         Ardrone3PilotingStateAttitudeChanged,
                         self.cb_get_atti)
        rospy.Subscriber('/bebop/states/ardrone3/PilotingState/PositionChanged',
                         Ardrone3PilotingStatePositionChanged,
                         self.cb_get_gps)
        '''
        rospy.Subscriber('/bebop/states/ardrone3/PilotingState/AltitudeChanged',
                         Ardrone3PilotingStateAttitudeChanged,
                         self.cb_get_alti)
        '''
        self.atti_now    = self.atti_tmp = 0.0        
        self.use_tmp     = False        
        self.lati_now    = self.long_now = self.alti_gps = 500.0
        self.alti_bar    = 0.0
        self.bearing_now = self.bearing_ref = 0.0
        
        
        self.margin_angle  = radians(2.5)
        self.margin_radius = DEG_PER_M * 1.5
        self.margin_alt    = 0.125
        
        rospy.sleep(3.0)

    
    def cb_get_alti(self, msg):
        self.alti_bar = msg.altitude
    

    def cb_get_gps(self, msg):
        
        if USE_SPHINX is True:
            self.lati_now = msg.latitude  + OFFSET_LAT
            self.long_now = msg.longitude + OFFSET_LON
        else:
            self.lati_now = msg.latitude
            self.long_now = msg.longitude
            
        self.alti_gps = msg.altitude


    def cb_get_atti(self, msg):
    
        self.atti_now = msg.yaw
        
        if   msg.yaw < 0:
            self.atti_tmp = msg.yaw + pi 
        elif msg.yaw > 0:
            self.atti_tmp = msg.yaw - pi
        else:
            self.atti_tmp = 0.0
            
    
    def get_atti(self):
        if self.use_tmp == True:
            return self.atti_tmp
        else:
            return self.atti_now
            
    
    def get_bearing(self, lat1, lon1, lat2, lon2):
    
        Lat1,  Lon1 = radians(lat1), radians(lon1) 
        Lat2,  Lon2 = radians(lat2), radians(lon2) 
        
        y = sin(Lon2-Lon1) * cos(Lat2) 
        x = cos(Lat1) * sin(Lat2) - sin(Lat1) * cos(Lat2) * cos(Lon2-Lon1) 
        
        return atan2(y, x)
    
        
    def get_gps_now(self):
        return self.lati_now, self.long_now
            
    
    def rotate(self, lat2, lon2, speed):
        
        pub = rospy.Publisher('/bebop/cmd_vel', Twist, queue_size = 1)
        tw  = Twist()
        
        lat1, lon1 = self.get_gps_now()
        
        target  = self.get_bearing(lat1, lon1, lat2, lon2)
        
        current = self.atti_now;        angle = abs(target-current)
        
        if angle > pi:  #   if angle > radians(180):
            self.use_tmp = True            
            if   target > 0.0:
                target = target - pi
            elif target < 0.0:
                target = target + pi
            else:   pass
            current = self.get_atti();  angle = abs(target - current)
        else:           #   if angle > radians(180):
            self.use_tmp = False        
        
        print "start rotate from: %s" %(degrees(self.atti_now))
            
        if   target > current:    # cw, -angular.z
            
            tw.angular.z = -speed
            
            if   angle > radians(50):
                target = target - radians(5)
            elif angle > radians(20): 
                target = target - radians(10)
            else:
                tw.angular.z = -0.1125
                
            while target > current:
                if abs(tw.angular.z) > 0.125:
                    tw.angular.z = -speed * abs(target - current) / angle
                else:
                    tw.angular.z = -0.125
                current = self.get_atti();  pub.publish(tw)
                
        elif target < current:    # ccw,  angular.z            
            
            tw.angular.z =  speed
            
            if   angle > radians(50):
                target = target + radians(5)
            elif angle > radians(20): 
                target = target + radians(10)
            else:
                tw.angular.z =  0.1125
                
            while target < current:
                if abs(tw.angular.z) > 0.125:
                    tw.angular.z =  speed * abs(target - current) / angle
                else:
                    tw.angular.z =  0.125
                current = self.get_atti();  pub.publish(tw)
                
        else:   pass
        
        print "stop rotate to   : %s" %(degrees(self.atti_now))
        
        
    def check_route(self, lat2, lon2):
        
        lat_now, lon_now = self.get_gps_now()
        
        bearing = self.get_bearing(lat_now, lon_now, lat2, lon2)
        
        if bearing > self.bearing_ref - self.margin_angle and \
           bearing < self.bearing_ref + self.margin_angle:
            return True
        else:
            return False
        
        
    def check_alt(self):
        if self.alti_bar > FLIGHT_ALT - self.margin_alt and \
           self.alti_bar < FLIGHT_ALT + self.margin_alt:
            return True
        else:
            return False
            
    
    def check_arrived(self, lat2, lon2):
        '''
        when center is (a,b), equation of circle : pow((x-a),2) + pow((y-b),2) = pow(r,2)
        pow((lat_now-lat2), 2) + pow((lon_now-lon2), 2) = pow(self.margin_radius, 2)
        self.margin_radius = sqrt(pow((lat_now-lat2), 2) + pow((lon_now - lon2), 2))
        '''
        lat_now, lon_now = self.get_gps_now()
        radius = sqrt(pow((lat_now-lat2), 2) + pow((lon_now - lon2), 2))
        
        if radius < self.margin_radius:
            return True
        else:
            return False
    
    
    def move_to_target(self, lat1, lon1, lat2, lon2):
        
        pub   = rospy.Publisher('/bebop/cmd_vel', Twist, queue_size=1)
        tw    = Twist()
        land  = rospy.Publisher('/bebop/land', Empty, queue_size = 1)
        empty = Empty()
        
        while self.check_arrived(lat2, lon2) is False:
            
            if self.check_alt() is False:
                if self.check_alt() > FLIGHT_ALT:
                    tw.linear.z = -0.1
                else:
                    tw.linear.z =  0.1
            else:
                tw.linear.z = 0.0
            
            if self.check_route(lat2, lon2) is True:
                tw.linear.x = LIN_SPD;  pub.publish(tw)
                
            else:
                lat1, lon1 = self.get_gps_now()
                self.bearing_ref = self.get_bearing(lat1, lon1, lat2, lon2)
                self.rotate(lat2, lon2, radians(45))
                
        tw.linear.x = 0;  pub.publish(tw); rospy.sleep(2.0)
        print "arrived at HOME location(%s, %s)" %(self.lati_now, self.long_now)
        
        land.publish(empty)
        rospy.sleep(5)
        print "landing finished"
        print "#### all missions are finished!!! ####"
        sys.exit(1)
              
            
if __name__ == '__main__':
    
    take = rospy.Publisher('/bebop/takeoff', Empty, queue_size = 1)
    land = rospy.Publisher('/bebop/land',    Empty, queue_size = 1)
    cmd  = rospy.Publisher('/bebop/cmd_vel', Twist, queue_size = 1)
    
    m2g  = Move2GPS()
    bb2  = Bebop2Move()
    tw   = Twist()
    off  = empty = Empty()
    
    while m2g.lati_now == 500.0 or m2g.long_now == 500.0 or m2g.alti_gps == 500.0:
        pass
    
    while rospy.get_param('mission_2_finished') is False:
        pass
    
    print "--- 1-1. valid gps info recieved!!!"
    
    height = FLIGHT_ALT - m2g.alti_bar
    bb2.move_z(height, 0.05)
    
    print "--- 1-2. reached flight altitude!"
    
    tw.linear.z = 0.0;  cmd.publish(tw)       
    
    try:
        while not rospy.is_shutdown():
            p2_lati_deg = rospy.get_param('home_lati') #float(input("input target latitude : "))
            p2_long_deg = rospy.get_param('home_long') #float(input("input target longitude: "))
            
            p1_lati_deg = m2g.lati_now
            p1_long_deg = m2g.long_now
            print "p1(%s, %s), p2(%s, %s)" %(p1_lati_deg, p1_long_deg, p2_lati_deg, p2_long_deg)
            
            m2g.bearing_ref = m2g.get_bearing(p1_lati_deg, p1_long_deg, p2_lati_deg, p2_long_deg)
            
            m2g.rotate(p2_lati_deg, p2_long_deg, radians(45))        
            m2g.move_to_target(p1_lati_deg, p1_long_deg, p2_lati_deg, p2_long_deg)
        
        rospy.spin()
        
    except rospy.ROSInterruptException:
        land.publish(empty);    rospy.sleep(5.0)
