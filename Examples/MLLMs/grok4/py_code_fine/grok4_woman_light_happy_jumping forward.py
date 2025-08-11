
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(0, 3)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Initialize the positions of the point lights
points = np.zeros((15, 2))

# Define a function to initialize the point lights
def init():
    scat.set_offsets(points)
    return scat,

# Function to update the frame
def update(frame):
    # Define jump trajectory parameters
    t = frame / 30  # Normalize the frame rate over 30 frames
    jump_height = 1.0 * np.sin(np.pi * t)  # Sinusoidal jump
    forward_step = 0.05 * frame  # Forward motion
    
    # Update point light positions
    points[:, 0] = np.random.uniform(-0.15, 0.15) + forward_step  # Random x position, moving forward
    points[:, 1] = np.random.uniform(1.0 + jump_height, 1.5 + jump_height)  # y position with jump height
    
    # Update scatter plot
    scat.set_offsets(points)
    return scat,

# Create scatter plot for point lights
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Create animation
anim = FuncAnimation(fig, update, frames=60, init_func=init, blit=True, interval=50)

# Show the animation
plt.show()
