from vpython import *

s = sphere(pos=vector(0,0,0), radius=0.5, color=color.blue)
v = vector(0,0,0)
g = vector(0, -0.001, 0)

while True:
    rate(60)
    s.pos += v
    v += g
    if s.pos.y < -1:
        v.y *= -1
