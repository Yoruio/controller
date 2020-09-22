import time
import os
import sys
from sphero_sdk import SpheroRvrObserver, RawMotorModesEnum

rvr = SpheroRvrObserver()

def setup(robot_config):
    # your hardware setup code goes here
    print("setting up RVR")
    rvr.wake()
    time.sleep(2)
    rvr.reset_yaw()
    print("RVR setup")
    return

def motors(left,right):
    if left < 0:
        left = 0 - left;
        leftDirection = RawMotorModesEnum.reverse.value
    elif left == 0:
        leftDirection = RawMotorModesEnum.off.value
    else:
        leftDirection = RawMotorModesEnum.forward.value

    if right < 0:
        right = 0 - right
        rightDirection = RawMotorModesEnum.reverse.value
    elif right == 0:
        rightDirection = RawMotorModesEnum.off.value
    else:
        rightDirection = RawMotorModesEnum.forward.value

    rvr.raw_motors(
        left_mode=leftDirection,
        left_duty_cycle=left,  # Valid duty cycle range is 0-255
        right_mode=rightDirection,
        right_duty_cycle=right  # Valid duty cycle range is 0-255
    )

def move(args):
    command = args['button']['command']
    print(args)
    print (command)

    try:
        if command == 'F' or command == 'f' :
            # your hardware movement code for forward goes here
            motors(128,128)
            time.sleep(0.5)
            motors(0,0)
            print("F")
            return
        elif command == 'B' or command == 'b':
            # your hardware movement code for backwards goes here
            motors(-128,-128)
            time.sleep(0.5)
            motors(0,0)
            print("B")
            return
        elif command == 'L' or command == 'l':
            # your hardware movement code for left goes here
            motors(-128,128)
            time.sleep(0.05)
            motors(0,0)
            print("L")
            return
        elif command == 'R' or command == 'r':
            # your hardware movement code for right goes here
            motors(128,-128)
            time.sleep(0.05)
            motors(0,0)
            print("R")
            return
        elif command == 'w':
            rvr.wake()
    except:
        import traceback
        print(traceback.format_exec())
    return
