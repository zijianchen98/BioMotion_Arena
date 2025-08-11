
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_LIGHTS = 15
FRAME_RATE = 30
DURATION = 5  # seconds
BACKGROUND_COLOR = 'black'
POINT_COLOR = 'white'

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')

# Create point lights
points, = ax.plot([], [], 'o', color=POINT_COLOR)

# Define forward rolling motion
def forward_rolling(t):
    x = np.linspace(0, 10, NUM_LIGHTS)
    y = np.sin(x + t) + 5  # Sine wave for up-and-down motion
    return x, y

# Update function for animation
def update(frame):
    t = frame / FRAME_RATE
    x, y = forward_rolling(t)
    points.set_data(x, y)
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=int(FRAME_RATE * DURATION), interval=1000 / FRAME_RATE, blit=True)

# Show animation
plt.show()
