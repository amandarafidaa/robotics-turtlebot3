import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class ProcessingNode(Node):

    def __init__(self):
        super().__init__('processing_node')

        self.declare_parameter('threshold', 0.5)

        self.subscription = self.create_subscription(
            Float32, 'sensor_data', self.listener_callback, 10
        )

    def listener_callback(self, msg):
        threshold = (
            self.get_parameter('threshold')
            .get_parameter_value()
            .double_value
        )

        if msg.data > threshold:
            self.get_logger().warn(
                f'Nilai sensor ({msg.data:.2f}) MELEBIHI threshold'
                f' ({threshold:.2f})!'
            )
        else:
            self.get_logger().info(
                f'Nilai sensor aman: {msg.data:.2f} <= {threshold:.2f}'
            )


def main(args=None):
    rclpy.init(args=args)
    node = ProcessingNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
