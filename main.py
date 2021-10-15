import time
import math
from adafruit_servokit import ServoKit

# Set up servos
kit = ServoKit(channels=16)
# FL
kit.servo[0].actuation_range = 140
kit.servo[1].actuation_range = 140
kit.servo[2].actuation_range = 140

# FR
kit.servo[3].actuation_range = 140
kit.servo[4].actuation_range = 130
kit.servo[5].actuation_range = 130

curX = -11.126
curY = -28.761


def invkin(x, y):
    l1 = 111.126
    l2 = 118.5
    a2 = math.acos((x ** 2 + y ** 2 - l1 ** 2 - l2 ** 2) / (2 * l1 * l2))
    a1 = math.atan2(y, x) - math.atan2(l2 * math.sin(a2), l1 + l2 * math.cos(a2))
    a2 = math.degrees(a2)
    a1 = math.degrees(a1)
    return a1, a2


def homeLegs():
    kit.servo[1].angle = 70
    kit.servo[2].angle = 0

    kit.servo[3].angle = 60
    kit.servo[4].angle = 60

    kit.servo[4].angle = 65
    kit.servo[5].angle = 130


def commandFL(x, y):
    alpha1, alpha2 = invkin(x, y)
    print("Calculated Angles: ", alpha1, alpha2)
    a1 = complement(alpha1) + kit.servo[1].actuation_range/2 + 15
    a2 = complement(alpha2) - 15
    print("Commanded Angles: ", a1, a2)
    kit.servo[1].angle = a1
    kit.servo[2].angle = a2



def commandFR(x, y):
    alpha1, alpha2 = invkin(x, y)
    print("Calculated Angles: ", alpha1, alpha2)
    a1 = complement(-alpha1)+ kit.servo[4].actuation_range / 2 - 15
    a2 = kit.servo[5].actuation_range - (180-alpha2) + 15
    print("Commanded Angles: ", a1, a2)
    kit.servo[4].angle = a1
    kit.servo[5].angle = a2


def complement(angle):
    if angle < 0:
        return (-180-angle)
    return (180-angle)


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
homeLegs()
time.sleep(0.5)

x = -111.126
y = -118.5
commandFL(x, y)
commandFR(x, y)
time.sleep(0.01)
