from graph import graph,graph_parametric
from math import pi, cos, sin

def f_x(t):
    return 2*sin(t) - sin(2*t)

def f_y(t):
    return -10*cos(t)

img = graph_parametric(f_x,f_y,0,2*pi,
        step_size=0.0001,
        color=(0,151,144,255),
        img_type="RGBA",
        bg_color=(0,0,0,0))
img.save("test.png")
