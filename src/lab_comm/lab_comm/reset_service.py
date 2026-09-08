from std_srvs.srv import Trigger


class ResetService(Node):
    def __init__(self):
        super().__init__('reset_service')
        self.counter = 0

        self.srv = self.create_service(
            Trigger, 'reset_system', self.on_reset
        )

    def on_reset(self, request, response):
        old = self.counter
        self.counter = 0
        response.success = True
        response.message = f'counter reset from {old}'
        return response


ros2 service list -t

ros2 service call /reset_system std_srvs/srv/Trigger "{}"
