
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_lights = 15

# Define the size of the animation
width, height = 800, 600

# Define the position of the point lights
positions = np.array([
    [200, 200],
    [200, 400],
    [400, 200],
    [400, 400],
    [600, 200],
    [600, 400],
    [400, 600],
    [200, 600],
    [200, 400],
    [400, 200],
    [400, 400],
    [600, 200],
    [600, 400],
    [400, 600],
    [200, 600],
    [200, 400],
])

# Define the angle of rotation
angle = 0

# Define the speed of the animation
speed = 0.05

# Create the figure and axes
fig, ax = plt.subplots(figsize=(width / 100, height / 100))

# Create the animation
def animate(i):
    global angle
    # Rotate the point lights
    for j in range(num_lights):
        x = positions[j][0] + speed * np.cos(angle)
        y = positions[j][1] + speed * np.sin(angle)
        ax.plot(x, y, 'w', marker='o', markersize=5)
    angle += 0.01
    return ax,

# Create the animation object
ani = animation.FuncAnimation(fig, animate, frames=100, interval=10, blit=True)

# Show the animation
plt.show()
