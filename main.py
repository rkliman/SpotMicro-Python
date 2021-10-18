import time
import robot
import gc

Spot = robot.Robot()
print(gc.mem_free())

Lspan: float = 40
dL: float = 20
floor: float = -170
delta: float = 10
swing: list[list[float]] = [[-Lspan, floor],
                            [-Lspan - dL, floor],
                            [-60, -140],
                            [-60, -140],
                            [-60, -140],
                            [60, -130],
                            [60, -130],
                            [60, -140],
                            [Lspan + dL, floor],
                            [Lspan, floor]]

stance: list[list[float]] = [[Lspan, floor],
                             [0, floor - delta],
                             [-Lspan, floor]]
vd: float = 40  # mm/s
print(gc.mem_free())
T_stance: float = 2 * Lspan / vd
T_swing: float = 0.25
T_stride: float = T_stance + T_swing
dS_trot: list[float] = [0, 0.5, 0.5, 0]

print(gc.mem_free())
# Setup and Calibration Step
Spot.homeLegs()
Spot.commandFL(0, -118.5)
Spot.commandFR(0, -118.5)
Spot.commandBL(0, -118.5)
Spot.commandBR(0, -118.5)
time.sleep(1)
gc.collect()

# Actual Program

t: float = 0
# One swing of the leg
pos: list[float] = [0, 0]
while t <= T_stride:
    for i in range(4):
        pos: list[float] = [0, 0]
        # Stance
        t_i: float = (t + T_stride * dS_trot[i]) % T_stride
        if t_i <= T_stance:
            pos = robot.bezier(t_i / T_stance, stance)
            gc.collect()
        # Swing
        else:
            pos = robot.bezier((t_i - T_stance) / T_swing, swing)
            gc.collect()
        if i == 0:
            Spot.commandFL(pos[0], pos[1])
        elif i == 1:
            Spot.commandFR(pos[0], pos[1])
        elif i == 2:
            Spot.commandBL(pos[0], pos[1])
        elif i == 3:
            Spot.commandBR(pos[0], pos[1])
        gc.collect()
    t += 0.05

# Finish up and reset robot positions
Spot.homeLegs()
