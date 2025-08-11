
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_LIGHTS = 15
FPS = 30
DURATION = 5  # seconds
TOTAL_FRAMES = FPS * DURATION

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 8)
ax.set_ylim(0, 6)
ax.set_facecolor('black')

# Generate initial positions for the lights
x = np.random.uniform(0, 8, NUM_LIGHTS)
y = np.random.uniform(0, 6, NUM_LIGHTS)

# Create scatter plot for the lights
lights = ax.scatter(x, y, color='white', s=100)

def update(frame):
    # Calculate the progress of the animation (0 to 1)
    t = frame / TOTAL_FRAMES
    
    # Define the bowing motion for the woman
    # This is a simplified model and can be improved for realism
    center_x = 4
    center_y = 3
    radius = 1.5
    angle = np.pi * (t - 0.5)  # Bowing motion from left to right
    
    # Update positions of the lights
    for i in range(NUM_LIGHTS):
        # Distribute lights around the bowing arc
        theta = 2 * np.pi * i / NUM_LIGHTS
        x[i] = center_x + radius * np.cos(theta) * np.cos(angle)
        y[i] = center_y + radius * np.sin(theta) + radius * np.sin(angle) * 0.5
    
    # Update the scatter plot
    lights.set_offsets(np.c_[x, y])
    return lights,

# Create the animation
ani = FuncAnimation(fig, update, frames=TOTAL_FRAMES, blit=True, interval=1000/FPS)

# Show the animation
plt.show()
