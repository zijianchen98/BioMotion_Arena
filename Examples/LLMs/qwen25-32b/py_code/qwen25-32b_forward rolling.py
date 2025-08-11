
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis.
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')  # Hide the axes

# Number of lights
num_lights = 15

# Initial positions of the lights
positions = np.random.rand(num_lights, 2) * 10

# Define the path for forward rolling motion
def forward_roll(t):
    x = t % 10
    y = np.sin(t / 2) + 5  # Sine wave to simulate rolling motion
    return x, y

# Scatter plot for the lights
scat = ax.scatter(positions[:, 0], positions[:, 1])

# Update function for the animation
def update(frame):
    global positions
    for i in range(num_lights):
        x, y = forward_roll(frame + i)
        positions[i] = [x, y]
    scat.set_offsets(positions)

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 20 * np.pi, 200), interval=50, blit=False)

plt.show()
