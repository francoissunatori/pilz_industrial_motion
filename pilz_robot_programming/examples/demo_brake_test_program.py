#!/usr/bin/env python
# Copyright (c) 2019 Pilz GmbH & Co. KG
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from pilz_robot_programming.robot import *
from pilz_robot_programming.commands import *

__REQUIRED_API_VERSION__ = "1"


def start_program():
    print("Executing " +__file__)

    r = Robot(__REQUIRED_API_VERSION__)

    # Execute a brake test if required
    if r.is_brake_test_required():
        try:
            r.execute_brake_test()
        except RobotBrakeTestException as e:
            rospy.logerr(e)
        except rospy.ROSException as e:
            rospy.logerr("failed to call the service")


if __name__ == "__main__":
    # Init a ros node
    rospy.init_node('gripper_program_node', anonymous=True)

    start_program()
