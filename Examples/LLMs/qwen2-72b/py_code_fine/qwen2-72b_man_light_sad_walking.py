
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters for the animation
n_frames = 100  # Number of frames in the animation
fps = 30  # Frames per second
interval = 1000 / fps  # Interval between frames in milliseconds

# Define the initial positions of the point-lights
positions = np.array([
    [0.1, 0.4],  # Head
    [0.2, 0.6],  # Right shoulder
    [0.2, 0.8],  # Right hip
    [0.3, 0.9],  # Right knee
    [0.2, 1.0],  # Right ankle
    [0.8, 0.6],  # Left shoulder
    [0.8, 0.8],  # Left hip
    [0.7, 0.9],  # Left knee
    [0.8, 1.0],  # Left ankle
    [0.45, 0.5],  # Right elbow
    [0.55, 0.5],  # Right wrist
    [0.65, 0.5],  # Left elbow
    [0.55, 0.5],  # Left wrist
    [0.45, 0.3],  # Right hand
    [0.55, 0.3]   # Left hand
]) * 100  # Scale up the positions

# Define the walking motion
def update_positions(frame):
    # Calculate the new positions based on the frame number
    step = frame % 10
    positions[1:3, 1] += 0.5 * np.sin(step * np.pi / 5)
    positions[4:6, 1] -= 0.5 * np.sin(step * np.pi / 5)
    positions[6:8, 1] += 0.5 * np.sin((step + 5) * np.pi / 5)
    positions[9:11, 1] -= 0.5 * np.sin((step + 5) * np.pi / 5)

    # Update the positions of the scatter plot
    scat.set_offsets(positions)
    return scat,

# Create the figure and axes
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_facecolor('black')

# Create the scatter plot for the point-lights
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update_positions, frames=n_frames, interval=interval, blit=True)

# Show the animation
plt.show()
