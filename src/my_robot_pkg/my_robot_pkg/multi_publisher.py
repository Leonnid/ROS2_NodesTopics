#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32

class MultiPublisher(Node):
    def __init__(self):
        super().__init__('multi_publisher')

        self.cmd_pub = self.create_publisher(String, '/cmd_vel', 10)

        self.battery_pub = self.create_publisher(Int32, '/battery_level', 10)

        self.timer = self.create_timer(1.0, self.publish_data)
        self.counter = 0

    def publish_data(self):
        cmd_msg = String()
        cmd_msg.data = f'Command_{self.counter}'
        self.cmd_pub.publish(cmd_msg)
        self.get_logger().info(f'Published cmd: {cmd_msg.data}')

        battery_msg = Int32()
        battery_msg.data = 100 - (self.counter % 10)
        self.battery_pub.publish(battery_msg)
        self.get_logger().info(f'Published battery: {battery_msg.data}%')

        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = MultiPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
