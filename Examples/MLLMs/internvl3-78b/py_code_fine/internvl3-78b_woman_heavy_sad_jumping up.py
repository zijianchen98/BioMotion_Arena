
import pyglet
from pyglet.gl import *
import numpy as np

# Set up the window
window = pyglet.window.Window(width=400, height=400)
glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background

# Points configuration
points = [
    [50, 50], [150, 50], [250, 50], [350, 50], [450, 50], 
    [50, 200], [150, 200], [250, 200], [350, 200], [450, 200],
    [50, 350], [150, 350], [250, 350], [350, 350], [450, 350]
]

# Time and velocity
time = 0
velocity = -0.08

@window.event
def on_draw():
    global time
    window.clear()
    glPointSize(10)
    
    for point in points:
        new_y = point[1] * np.sin(velocity * time) + point[1]
        if 250 <= new_y <= 350:
            glBegin(GL_POINTS)
            glVertex3f(point[0], new_y, 0)
            glEnd()

    time += 0.05

pyglet.app.run()
