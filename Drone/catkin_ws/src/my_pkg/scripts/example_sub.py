#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1행은 셔뱅(Shebang)으로, 이 스크립트 해석기의 위치를 지정한다. 모든 파이썬으로 작성된 ROS 노드는 반드
# 시 이 셔뱅으로 시작해야 한다.
# 2행은 한글 지원

import rospy                    # roscpp 코드의 "#include <ros.h>"에 해당하는 구문
from std_msgs.msg import String	# ROS 표준 메세지형식 중 String 모듈 import. 
                                # roscpp 코드 "#include <std_msgs/String.h>"에 해당한다.
# 메세지 수신 이벤트 발생 시 호출될 콜백함수 callback() 정의
def cb_func(msg):
    # time stamp + subscribe 노드명 + ' msg: ' + subscribe data 를 화면 출력 
    rospy.loginfo(rospy.get_caller_id() + 'subscribed message: %s', msg.data)

def simple_sub():               # "simple_sub()"함수 정의 시작
    # ROS 환경에서 노드는 중복되지 않는 유일한 이름을 가져야만 한다. 이름이 같은 두 개의 
# 노드가 실행된다면, 먼저 실행된 노드는 두 번째 노드가 실행될 때 강제종료된다.
    # 'anonymous=True' 플래그는 이 노드의 이름을 rospy가 관리할 수 있도록 하여 이 노드와 
    # 같은 이름의 노드가 실행되어 있더라도 rospy가 적당한 중복없는 이름으로 노드명을 변경
# 함으로써 같은 토픽을 구독하는 다수의 구독노드를 실행할 수 있게 한다는 의미이다.
    # rospy.init_node('sample_sub', anonymous=True)
    rospy.init_node('sample_sub') # 수신 메세지 String 길이를 짧게 하기위해 수정 
    # 토픽명:'hello', 토픽형식:String, 콜백함수명:cb_func인 서브스크라이버 설정
    rospy.Subscriber('hello', String, cb_func)
    # roscpp의 'ros::spin();'에 해당하는 코드. 프로그램 종료 시점까지 제어가 유지되도록 
# 한다.
    rospy.spin()                # Ctrl-C 입력이 있을 때까지 새 메세지가 발행되면 콜백함수
# 를 호출한다.
if __name__ == '__main__':      # 인터프리터 전역변수 __name__ 의 값이 '__main__' 이면
    simple_sub()                # 'simple_sub()' 함수 호출
