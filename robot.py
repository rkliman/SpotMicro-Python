import util
import time
from adafruit_servokit import ServoKit


# Trajectory modeling Functions
def bezier(t: float, control_points: list):
    x: float = 0
    y: float = 0
    for i in range(len(control_points)):
        bez: float = util.choose(len(control_points) - 1, i) * ((1 - t) ** (len(control_points) - 1 - i)) * (t ** i)
        x += bez * control_points[i][0]
        y += bez * control_points[i][1]
    return x, y


class Robot:
    def __init__(self):
        self.kit = ServoKit(channels=16)

        # FL
        self.kit.servo[0].actuation_range = 140
        self.kit.servo[1].actuation_range = 140
        self.kit.servo[2].actuation_range = 140

        # FR
        self.kit.servo[3].actuation_range = 140
        self.kit.servo[4].actuation_range = 130
        self.kit.servo[5].actuation_range = 130

        # BR
        self.kit.servo[6].actuation_range = 136
        self.kit.servo[7].actuation_range = 134
        self.kit.servo[8].actuation_range = 130

        self.kit.servo[9].actuation_range = 132  # add a 4 degrees to 66 for zero pos
        self.kit.servo[10].actuation_range = 140
        self.kit.servo[11].actuation_range = 140

    def homeLegs(self):
        self.kit.servo[0].angle = 60
        self.kit.servo[1].angle = 70
        self.kit.servo[2].angle = 0

        self.kit.servo[3].angle = 60
        self.kit.servo[4].angle = 65
        self.kit.servo[5].angle = 130

        self.kit.servo[6].angle = 70  # midpoint 68, requires 2 degree offset for zero pos.
        self.kit.servo[7].angle = 67
        self.kit.servo[8].angle = 130

        self.kit.servo[9].angle = 70  # midpoint 66, requires 4 degree offset for zero pos
        self.kit.servo[10].angle = 70
        self.kit.servo[11].angle = 0
        time.sleep(0.5)

    def commandFL(self, x: float, y: float):
        alpha1, alpha2 = util.invkin(x, y)
        print("Calculated Angles: ", alpha1, alpha2)
        a1: float = util.complement(alpha1) + self.kit.servo[1].actuation_range / 2 + 15
        a2: float = util.complement(alpha2) - 15
        print("Commanded Angles: ", a1, a2)
        self.kit.servo[1].angle = a1
        self.kit.servo[2].angle = a2

    def commandFR(self, x: float, y: float):
        alpha1, alpha2 = util.invkin(x, y)
        # print("Calculated Angles: ", alpha1, alpha2)
        a1: float = util.complement(-alpha1) + self.kit.servo[4].actuation_range / 2 - 15
        a2: float = self.kit.servo[5].actuation_range - (180 - alpha2) + 15
        # print("Commanded Angles: ", a1, a2)
        self.kit.servo[4].angle = a1
        self.kit.servo[5].angle = a2

    def commandBR(self, x: float, y: float):
        alpha1, alpha2 = util.invkin(x, y)
        # print("Calculated Angles: ", alpha1, alpha2)
        a1: float = util.complement(-alpha1) + self.kit.servo[7].actuation_range / 2 - 15
        a2: float = self.kit.servo[8].actuation_range - (180 - alpha2) + 15
        # print("Commanded Angles: ", a1, a2)
        self.kit.servo[7].angle = a1
        self.kit.servo[8].angle = a2

    def commandBL(self, x: float, y: float):
        alpha1, alpha2 = util.invkin(x, y)
        # print("Calculated Angles: ", alpha1, alpha2)
        a1: float = util.complement(alpha1) + self.kit.servo[10].actuation_range / 2 + 15
        a2: float = util.complement(alpha2) - 15
        # print("Commanded Angles: ", a1, a2)
        self.kit.servo[10].angle = a1
        self.kit.servo[11].angle = a2
