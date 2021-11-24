import math


# Mathematical Utility Functions
def factorial(n: int):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


def choose(n: int, k: int):
    return factorial(n) / (factorial(k) * factorial(n - k))


def complement(angle: float):
    if angle < 0:
        return (-180 - angle)
    return (180 - angle)


# Kinematics Functions
# l1 = 111.126
# l2 = 118.5
def invkin(x: float, y: float):
    a2: float = math.degrees(math.acos((x ** 2 + y ** 2 - 111.126 ** 2 - 118.5 ** 2) / (2 * 111.126 * 118.5)))
    a1: float = math.degrees(math.atan2(y, x) - math.atan2(118.5 * math.sin(math.radians(a2)), 111.126 + 118.5 * math.cos(math.radians(a2))))
    return a1, a2



