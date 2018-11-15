import matplotlib.pyplot as plt
import random
import math
import numpy as np
R = 1.
n_rings = 10.
n_angles = 120.
dr = R/n_rings
da = 2*math.pi/n_angles

density = 2./(dr*da)
points = []
ring = 0
while ring < n_rings:
    angle = 0
    base_points_per_division = density*math.pi*(dr**2)*(2*ring+1)/n_angles
    while angle < n_angles:
        for i in xrange(int(base_points_per_division)):
             ra = angle*da + min(da,da*random.random())
             rr = ring*dr + dr*random.random()
             x = rr*math.cos(ra)
             y = rr*math.sin(ra)
             points.append((x,y))
        angle += 1
    ring += 1

X = [i[0] for i in points]
Y = [i[1] for i in points]

plt.plot(X,Y,'bo')
plt.show()

plt.plot(X,Y,'bo')
a = np.linspace(0, 2*np.pi, 500)
for ring in xrange(int(n_rings)+1):
    cx,cy = ring*dr*np.cos(a), ring*dr*np.sin(a)
    plt.plot(cx,cy,'-',alpha=.5)

a = np.linspace(-R-1, R+1, 500)
angle = 0.
for _angle in xrange(int(n_angles/2.)+1):
    cx,cy = a,a*np.tan(angle)
    plt.plot(cx,cy,'-',alpha=.5)
    angle += da
lim = min(R*1.1,R+1)
plt.xlim(-lim,lim)
plt.ylim(-lim,lim)
plt.show()


