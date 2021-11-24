import math
import matplotlib.pyplot as plt
import AngleAnnotation as aa

# from https://matplotlib.org/devdocs/gallery/text_labels_and_annotations/angle_annotation.html

fig = plt.figure()
ax = plt.axes()
size = 2
ax.plot([0, 0], [-size, size], 'k--', linewidth=0.5)
ax.plot([-2, 2], [0, 0], 'k--', linewidth=0.5)
a1 = -2*math.pi/3
a2 = math.pi/2
p1 = [(0, 0), (math.cos(a1), math.sin(a1))]
p2 = [(math.cos(a1), math.sin(a1)), (math.cos(a1) + 1.1*math.cos(a1 + a2), math.sin(a1) + 1.1*math.sin(a1 + a2))]
p3 = [(math.cos(a1), math.sin(a1)), (1.3*math.cos(a1), 1.3*math.sin(a1))]
line1, = ax.plot(*zip(*p1), 'k--')
line2, = ax.plot(*zip(*p2), 'k--')
line3, = ax.plot(*zip(*p3), 'k--',linewidth=0.75)
point1, = ax.plot(*(math.cos(a1), math.sin(a1)), marker="o", color="black")
point2, = ax.plot(*(math.cos(a1) + 1.1*math.cos(a1 + a2), math.sin(a1) + 1.1*math.sin(a1 + a2)), marker="o", color="black")
ax.annotate(r"$x_e$",(p2[1][0],p2[1][1]-0.15))
an1 = aa.AngleAnnotation((0, 0), p1[1],(1, 0), ax=ax, text=r"$-\frac{2\pi}{3}$", textposition="edge")
an2 = aa.AngleAnnotation((0, 0), (-1, 0), p1[1], ax=ax, text=r"$-\frac{\pi}{3}$", size=120, textposition="edge")
an3 = aa.AngleAnnotation(p1[1], (2*math.cos(a1), 2*math.sin(a1)), p2[1], ax=ax, text=r"$\alpha_2$",textposition="edge")
ax.set_xlim(-size, size)
ax.set_ylim(-size, size)
plt.show()
