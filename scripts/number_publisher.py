#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64


cont_pub = Int64()
def pub_num():
    pub = rospy.Publisher('number', Int64, queue_size=1)
    rospy.init_node('number_publisher')
    rate = rospy.Rate(2) # 2hz
    cont=0
    while not rospy.is_shutdown():
	cont=cont+1
	cont_pub.data=cont
	rospy.loginfo(cont)
        pub.publish(cont_pub)
        rate.sleep()

if __name__ == '__main__':
	try:
		pub_num()
	except rospy.ROSInterruptException:
		pass

