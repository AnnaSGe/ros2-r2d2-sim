import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class T(Node):
    def __init__(self):
        super().__init__('talker')
        self.p=self.create_publisher(String,'chatter',10)
        self.create_timer(1.0,self.cb)
    def cb(self):
        m=String()
        m.data="hi"
        self.p.publish(m)

def main():
    rclpy.init()
    rclpy.spin(T())
    rclpy.shutdown()