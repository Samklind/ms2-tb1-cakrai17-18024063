#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String

# This node subscribes to a Twist message from the randomizer node and
# republishes the data to the movement_reader node's two topics.
class TwistRepublisher(Node):

    def __init__(self):
        super().__init__('twist_republisher_node')
        
        # Define the topic names for subscribing and publishing.
        self.input_twist_topic = '/autonomous_vel'
        self.output_vel_topic = '/cmd_vel'
        self.output_type_topic = '/cmd_type'
        
        # Create a publisher that will send Twist messages to the /cmd_vel topic.
        self.cmd_vel_pub = self.create_publisher(Twist, self.output_vel_topic, 10)
        
        # Create a publisher that will send String messages to the /cmd_type topic.
        self.cmd_type_pub = self.create_publisher(String, self.output_type_topic, 10)
        
        # Create a subscriber that will listen for Twist messages from the randomizer node.
        self.subscription = self.create_subscription(
            Twist,
            self.input_twist_topic,
            self.twist_callback,
            10
        )
        # Prevent the subscription object from being garbage collected.
        self.subscription
        
        self.get_logger().info(f'Twist Republisher Node started. Subscribing to {self.input_twist_topic}...')
        self.get_logger().info(f'Republishing to {self.output_vel_topic} and {self.output_type_topic}...')

    def twist_callback(self, twist_msg):
        """
        Callback function for the incoming Twist messages.
        It takes the received message and republishes it to two different topics.
        """
        # Publish the received Twist message directly to the /cmd_vel topic.
        self.cmd_vel_pub.publish(twist_msg)
        
        # Create a new String message to indicate the command source.
        cmd_type_msg = String()
        cmd_type_msg.data = "autonomous"
        
        # Publish the String message to the /cmd_type topic.
        self.cmd_type_pub.publish(cmd_type_msg)
        
        # Log the action for verification.
        self.get_logger().info(f'Republished Twist and String from autonomous command.')


def main(args=None):
    rclpy.init(args=args)
    twist_republisher = TwistRepublisher()
    
    try:
        rclpy.spin(twist_republisher)
    except KeyboardInterrupt:
        pass
    finally:
        twist_republisher.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
