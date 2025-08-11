
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
initial_positions = np.array([
    [0.1, 0.2], [0.2, 0.3], [0.3, 0.4], [0.4, 0.5], [0.5, 0.6],
    [0.6, 0.5], [0.7, 0.4], [0.8, 0.3], [0.9, 0.2], [0.5, 0.3],
    [0.6, 0.4], [0.7, 0.5], [0.8, 0.6], [0.6, 0.7], [0.7, 0.8]
])

# Define the target positions for the sitting down action
target_positions = np.array([
    [0.1, 0.2], [0.2, 0.3], [0.3, 0.4], [0.4, 0.5], [0.5, 0.6],
    [0.6, 0.5], [0.7, 0.4], [0.8, 0.3], [0.9, 0.2], [0.5, 0.3],
    [0.6, 0.4], [0.7, 0.5], [0.8, 0.6], [0.6, 0.7], [0.7, 0.8]
])

# Define the duration of the animation in seconds
duration = 5

# Define the number of frames per second
fps = 30

# Calculate the total number of frames
total_frames = int(duration * fps)

# Calculate the time step between frames
dt = 1 / fps

# Define the easing function for smooth motion
def ease_in_out_quad(t):
    if t < 0.5:
        return 2 * t**2
    else:
        return -1 + (4 - 2 * t) * t

# Define the update function for the animation
def update(frame):
    # Calculate the progress of the animation
    progress = frame / total_frames
    
    # Calculate the interpolated positions using the easing function
    interpolated_positions = initial_positions + (target_positions - initial_positions) * ease_in_out_quad(progress)
    
    # Update the positions of the point lights
    for i in range(num_lights):
        scat._offsets3d = (interpolated_positions[:, 0], interpolated_positions[:, 1], np.zeros(num_lights))
    
    return scat,

# Create a figure and axis for the animation
fig, ax = plt.subplots(figsize=(6, 6), facecolor='black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Create the point lights as scatter plot
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=100)

# Create the animation
ani = FuncAnimation(fig, update, frames=total_frames, interval=int(1000 / fps), blit=True)

# Show the animation
plt.show()
