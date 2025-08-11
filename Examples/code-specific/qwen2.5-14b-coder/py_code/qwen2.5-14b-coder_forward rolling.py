
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_LIGHTS = 15
FRAME_RATE = 60
DURATION = 2  # seconds
FRAMES = FRAME_RATE * DURATION

# Initial positions of the lights
positions = np.zeros((NUM_LIGHTS, 2))
positions[:, 0] = np.linspace(-1, 1, NUM_LIGHTS)  # Spread out horizontally

# Function to update light positions for forward rolling
def update(frame):
    t = frame / FRAME_RATE
    for i in range(NUM_LIGHTS):
        # Simple model of forward rolling with some variation
        x = np.sin(2 * np.pi * (t + i / NUM_LIGHTS)) * (1 - i / NUM_LIGHTS)
        y = np.cos(2 * np.pi * (t + i / NUM_LIGHTS)) * (1 - i / NUM_LIGHTS)
        positions[i] = [x, y]
    scatter.set_offsets(positions)
    return scatter,

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 6), facecolor='black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')

# Create scatter plot for point lights
scatter = ax.scatter(positions[:, 0], positions[:, 1], color='white', s=50)

# Create animation
ani = FuncAnimation(fig, update, frames=FRAMES, interval=1000 / FRAME_RATE, blit=True)

# Show the animation
plt.show()
