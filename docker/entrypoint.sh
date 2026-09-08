#!/bin/bash

set -e

# Source ROS 2 environment
source /opt/ros/humble/setup.bash

# Source workspace environment if available
if [ -f /ws/install/setup.bash ]; then
    source /ws/install/setup.bash
fi

# Execute the given command
exec "$@"
