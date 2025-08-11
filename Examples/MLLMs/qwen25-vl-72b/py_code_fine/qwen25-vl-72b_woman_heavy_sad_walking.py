
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points based on the provided image
initial_positions = np.array([
    [0, 1], [-0.5, 0.7], [0.5, 0.7], [-0.8, 0.4], [0, 0.4], [0.8, 0.4],
    [-1, 0], [0, 0], [1, 0], [-0.5, -0.4], [0.5, -0.4], [-0.8, -0.7], [0, -0.7], [0.8, -0.7], [0, -1]
])

# Define the walking motion parameters
num_frames = 100
frame_rate = 30
amplitude = 0.1
frequency = 0.1

# Create a function to update the positions of the points for each frame
def update(frame):
    time = frame / frame_rate
    phase_shift = frequency * time
    
    # Update the positions of the points based on the walking motion
    new_positions = initial_positions.copy()
    new_positions[:, 0] += amplitude * np.sin(2 * np.pi * frequency * time + phase_shift)
    
    # Update the positions of the points in the scatter plot
    scat.set_offsets(new_positions)
    
    return scat,

# Set up the figure and axis for the animation
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Create the scatter plot for the points
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=50, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000/frame_rate, blit=True)

# Display the animation
plt.show()
