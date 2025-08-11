
import pyglet
import math

# Constants
WIDTH = 800
HEIGHT = 800
BACKGROUND_COLOR = (0, 0, 0)
WHITE_POINT_LIGHTS = 15

# Define the initial positions and velocities of the point-lights
positions = [
    [250, 100], [340, 200], [450, 270], [530, 300], [630, 250], [750, 150],
    [850, 90], [930, 50], [940, 100], [930, 150], [850, 200], [750, 250],
    [630, 300], [540, 350], [510, 350]
]
velocities = [
    (-2, 0), (-4, -4), (-5, -8), (-6, -10), (-7, -10), (-8, -8),
    (-10, -10), (-12, -12), (-14, -12), (-15, -10), (-16, -8), (-18, -8),
    (-20, -8), (-22, -8), (-25, -4)
]

# Function to ensure point-lights are within bounds
def wrap_around(position, width, height):
    if position[0] < 0:
        position[0] += width
    elif position[0] > width:
        position[0] -= width
    if position[1] < 0:
        position[1] += height
    elif position[1] > height:
        position[1] -= height
    return position

# Initialize Pyglet window and set callback functions
angle = 0
timedelta = 0.02  # update delta time for smooth motion

@pyglet.event_loop.event
def draw():
    global width, height, angle, timedelta
    pyglet.gl.glClear(pyglet.gl.COLOR_BUFFER_BIT)
    pyglet.gl.glColor3f(1, 1, 1)
    for pos in positions:
        x, y = pos
        while timedelta > 0:
            angle += timedelta
            if angle >= 2 * math.pi:
                angle -= 2 * math.pi
            for velocity in velocities:
                x += velocity[0] * timedelta
                y += velocity[1] * timedelta
                x = wrap_around([x, y], WIDTH, HEIGHT)[0]
                if x!= wrap_around([x, y], WIDTH, HEIGHT)[0]:
                    break
            timedelta = 0
        pyglet.gl.glPushMatrix()
        pyglet.gl.glTranslate(x - WIDTH / 2, y - HEIGHT / 2, 0)
        pyglet.gl.glPointSize(20)
        pyglet.gl.glBegin(pyglet.gl.POINTS)
        for p in positions:
            pyglet.gl.glVertex2f(p[0], p[1])
        pyglet.gl.glEnd()
        pyglet.gl.glPopMatrix()

pyglet.app.run()
