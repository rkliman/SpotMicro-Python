import matplotlib.pyplot as plt


# Mathematical Utility Functions
def factorial(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


def choose(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


# Trajectory modeling Functions
# def basis_function(t):
#     # control_points = [[-60, -130], [-50, -170], [50, -170], [60, -130]]
#     control_points = [(1, 1), (1, 2)]
#     out = []
#     l = len(control_points)
#     for i in range(l):
#         out.append()
#     return out


def bezier(t, control_points):
    x = 0
    y = 0
    l = len(control_points)
    for i in range(l):
        bez = choose(l-1, i) * ((1 - t) ** (l-1 - i)) * (t ** i)
        x += bez * control_points[i][0]
        y += bez * control_points[i][1]
    return x, y


px = []
py = []
t = 0
swing = [[-40,-170],
         [-60, -170],
         [-60, -140],
         [-60, -140],
         [-60, -140],
         [60, -130],
         [60, -130],
         [60, -140],
         [60, -170],
         [40, -170]]

stance = [[40,-170],
          [0,-180],
          [-40,-170]]

while t <= 1:
    value = bezier(t, swing)
    px.append(value[0])
    py.append(value[1])
    t += 0.001
plt.plot(px, py)

px = []
py = []
t = 0
while t <= 1:
    value = bezier(t, stance)
    px.append(value[0])
    py.append(value[1])
    t += 0.001
plt.plot(px, py)

ax=plt.gca()
ax.set_aspect('equal')
plt.show()
