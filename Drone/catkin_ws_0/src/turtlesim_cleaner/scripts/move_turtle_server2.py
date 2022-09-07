#!/usr/bin/env python
from turtlesim_cleaner.srv import XAndY, XAndYResponse
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import radians

TOLERANCE = 0.05

pose = Pose()

def svc_cb(req):
    res = within(req.x, req.y)
    
    if res is True:
        print "turtle is arrived destination!"
    return XAndYResponse(res)

def turtlesim_svc_svr():
    rospy.init_node('turtlesim_svc_node')
    svc = rospy.Service('turtlesim_svc', XAndY, svc_cb)
    print "turtle1 ready to move~"
    rospy.spin()

def update_pose(data):
    global pose
    pose = data

def within(angle):
    p = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    t = Twist()
    tolerance  = TOLERANCE

    sub = rospy.Subscriber('/turtle1/pose', Pose, update_pose)
    
    
    if pose.x < :
        t.linear.x = -speed
    else:
        t.angular.z =  speed

    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < abs(angle)):
        p.publish(t)
        t1 = rospy.Time.now().to_sec()
        current_angle = speed * (t1 - t0)
    
    t.angular.z = 0;    p.publish(t);   print "end rotate"
    return True


if __name__ == "__main__":
    turtlesim_svc_svr()
