#!/usr/bin/env python
import sys
import rospy
from turtlesim_cleaner.srv import XAndY

def move_turtle_client(x, y):
    rospy.wait_for_service('turtlesim_svc')

    try:
        svc = rospy.ServiceProxy('turtlesim_svc', XAndY)
        res = svc(x, y)
        return res.complete
        
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x] [y]" %sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
    else:
        print usage()
        sys.exit(1)

    print "Requesting x: %s(deg) & y: %s(m)"%(x, y)
    print "Request is %s" \
    %("complete!" if move_turtle_client(x, y) else "incomplete")
