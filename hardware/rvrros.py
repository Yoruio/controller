import time
import os
import sys
import rclpy
from rclpy.node import Node

from std_msgs.msg import Int8MultiArray

class RemoPublisher(Node):

    def __init__(self):
        super().__init__('remo_publisher')
        self.publisher_ = self.create_publisher(Int8MultiArray, 'drive', 10)
        #timer_period = 0.5  # seconds
        #self.timer = self.create_timer(timer_period, self.timer_callback)

    def send_ints(self, data):
        msg = Int8MultiArray()
        msg.data = data
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

rclpy.init()
remo_publisher = RemoPublisher()

def setup(robot_config):
    # your hardware setup code goes here
    print("initializing ROS node")

    return

def move(args):
    command = args['button']['command']
    print(args)
    print (command)

    try:
        if command == 'F' or command == 'f' :
            # your hardware movement code for forward goes here
            remo_publisher.send_ints([10,10])
            return
        elif command == 'B' or command == 'b':
            # your hardware movement code for backwards goes here
            remo_publisher.send_ints([-10,-10])
            return
        elif command == 'L' or command == 'l':
            # your hardware movement code for left goes here
            remo_publisher.send_ints([-10,10])
            return
        elif command == 'R' or command == 'r':
            # your hardware movement code for right goes here
            remo_publisher.send_ints([10,-10])
            return
        elif command == 'S' or command == 's':
            remo_publisher.send_ints([0,0])
            return
    except:
        import traceback
        print(traceback.format_exc())
    return
