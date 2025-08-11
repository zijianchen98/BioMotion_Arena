
import pyglet
import random

# Create a window
win = pyglet.window.Window(width=400, height=400, caption="Sadwoman Rolling")

# Define the light points
points = [pyglet.graphics.vertex_list(1, ("v2i", (random.randint(0, 400), random.randint(0, 400)))) for _ in range(15)]

# Animation function
def animate(dt):
    for point in points:
        x, y = point.vertices
        y -= 100 * dt  # downwards rolling motion
        if y < 0:  # reset position if it goes off the bottom of the screen
            y = 400
        point.vertices = (x, y)

# Set the timing of the animation
pyglet.clock.schedule_interval(animate, 0.1)

# Draw the points
@win.event
def on_draw():
    win.clear()
    for point in points:
        point.draw(pyglet.gl.GL_POINTS)

# Run the app
pyglet.app.run()
