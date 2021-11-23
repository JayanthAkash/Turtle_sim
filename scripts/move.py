#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


x = 0
y = 0
t = 0


def pose_callback(pos):  # finding the position of the turtle

    global x, y, t
    x = (pos.x)
    y = (pos.y)
    t = (pos.theta)
    print("x = {0}   y = {1}   z = {2}\n".format(x, y, t))


def mov():
    rospy.init_node("move", anonymous=True)
    velocity_publisher = rospy.Publisher(
        '/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber("/turtle1/pose", Pose, pose_callback)
    vel_msg = Twist()
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        vel_msg.linear.x = 1
        vel_msg.linear.z = 0
        vel_msg.linear.y = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0.75
        velocity_publisher.publish(vel_msg)

        if t > -0.1 and t < 0:  # stopping the turtle
            vel_msg.linear.x = 0
            vel_msg.linear.z = 0
            vel_msg.linear.y = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)
            print("stopping turtle")
            break

        rate.sleep()


if __name__ == '__main__':
    try:
        mov()
    except rospy.ROSInterruptException:
        pass
