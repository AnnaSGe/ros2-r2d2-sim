import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
import tf2_ros
import math

class MoveRobot(Node):
    def __init__(self):
        super().__init__('move_robot')
        self.br = tf2_ros.TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.update)
        self.x = 0.0
        self.yaw = 0.0

    def update(self):
        t = TransformStamped()

        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'world'
        t.child_frame_id = 'base_link'

        # move forward
        self.x += 0.02

        t.transform.translation.x = self.x
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0

        # orientation (yaw rotation)
        self.yaw += 0.02
        t.transform.rotation.z = math.sin(self.yaw/2)
        t.transform.rotation.w = math.cos(self.yaw/2)

        self.br.sendTransform(t)

def main():
    rclpy.init()
    node = MoveRobot()
    rclpy.spin(node)
    rclpy.shutdown()