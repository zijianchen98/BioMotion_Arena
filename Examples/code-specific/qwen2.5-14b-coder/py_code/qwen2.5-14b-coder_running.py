
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_LIGHTS = 15
FRAMES = 100
FPS = 30

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Create point lights
points, = ax.plot([], [], 'o', color='white', markersize=5)

# Define the trajectory of each point light
def trajectory(t, i):
    # Simple model of running motion
    x = (t / FRAMES + i / NUM_LIGHTS) % 1
    y = 0.5 + 0.3 * np.sin(4 * np.pi * t / FRAMES + 2 * np.pi * i / NUM_LIGHTS)
    return x, y

# Update function for animation
def update(frame):
    x_data = [trajectory(frame, i)[0] for i in range(NUM_LIGHTS)]
    y_data = [trajectory(frame, i)[1] for i in range(NUM_LIGHTS)]
    points.set_data(x_data, y_data)
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=FRAMES, interval=1000/FPS, blit=True)

# Show animation
plt.show()
