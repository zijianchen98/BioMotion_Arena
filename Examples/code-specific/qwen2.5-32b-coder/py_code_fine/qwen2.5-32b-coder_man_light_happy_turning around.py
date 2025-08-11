
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
frames = 100
fps = 30
radius = 0.5
angle_step = 2 * np.pi / frames

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(6, 6), facecolor='black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')

# Initial positions of lights
angles = np.linspace(0, 2 * np.pi, num_lights, endpoint=False)
x = radius * np.cos(angles)
y = radius * np.sin(angles)

# Scatter plot for lights
scat = ax.scatter(x, y, s=100, color='white')

def update(frame):
    # Update angles for turning around
    new_angles = angles + frame * angle_step
    
    # Update positions based on new angles
    x = radius * np.cos(new_angles)
    y = radius * np.sin(new_angles)
    
    # Apply a simple transformation to simulate "happyman" shape
    # Adjust y positions to create a more dynamic and "happy" appearance
    y += 0.2 * np.sin(2 * new_angles)
    
    # Update scatter plot data
    scat.set_offsets(np.c_[x, y])

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Show animation
plt.show()
