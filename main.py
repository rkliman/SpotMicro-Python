import time
import math
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
kit.servo[0].actuation_range = 140
kit.servo[1].actuation_range = 140
kit.servo[2].actuation_range = 140

curX = -11.126
curY = -28.761


def invkin(x, y):
    l1 = 111.126
    l2 = 118.5
    a2 = math.acos((x ** 2 + y ** 2 - l1 ** 2 - l2 ** 2) / (2 * l1 * l2))
    a1 = math.atan2(y, x) + math.atan2(l2 * math.sin(a2), l1 + l2 * math.cos(a2));
    a2 = math.degrees(a2)
    a1 = math.degrees(a1)
    return a1, a2


def homeLeg():
    kit.servo[1].angle = 70
    kit.servo[2].angle = 0


def commandLeg(x, y):
    alpha1, alpha2 = invkin(x, y)
    print("Calculated Angles: ", alpha1, alpha2)
    print("Commanded Angles: ",ang(alpha1)+70+13,ang(alpha2)-15)
    kit.servo[1].angle = ang(alpha1) + 70 + 13
    kit.servo[2].angle = (180-ang(alpha2)) - 15

def ang(angle):
    if angle > 180:
        return -(180-angle%180)
    return angle


# def moveTo(x, y, curX, curY):
#     diffX = x - curX
#     diffY = y - curY
#     print("Diffs: ", diffX, diffY)
#     stepX = 1 / diffX
#     stepY = 1 / diffY
#     while abs(diffX) > 1e-2 and abs(diffY) > 1e-2:
#         commandLeg(curX + stepX, curY + stepY)
#         curX += stepX
#         curY += stepY
#         diffX = x - curX
#         diffY = y - curY
#         print("Diffs: ", diffX, diffY)
#         time.sleep(0.001)


# Setup and Calibration Step
homeLeg()
time.sleep(0.5)

x = 0
y = -118.5
commandLeg(x,y)
time.sleep(0.01)
