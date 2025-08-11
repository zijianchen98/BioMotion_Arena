
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0.5, 0.8],  # Head
    [0.4, 0.6],  # Shoulder left
    [0.6, 0.6],  # Shoulder right
    [0.3, 0.4],  # Elbow left
    [0.7, 0.4],  # Elbow right
    [0.2, 0.2],  # Hand left
    [0.8, 0.2],  # Hand right
    [0.5, 0.5],  # Hip
    [0.4, 0.3],  # Knee left
    [0.6, 0.3],  # Knee right
    [0.3, 0.1],  # Foot left
    [0.7, 0.1],  # Foot right
    [0.4, 0.7],  # Eye left
    [0.6, 0.7],  # Eye right
    [0.5, 0.7]   # Nose
])

# Define the trajectory function for each joint based on sitting down motion
def get_trajectory(frame):
    t = frame / num_frames * 2 * np.pi
    amplitude = 0.1
    phase_shift = np.pi / 4
    displacement = amplitude * np.sin(t + phase_shift)
    return displacement

# Create the figure and axis for plotting
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide the axes

# Scatter plot for the point-lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

# Update function for the animation
def update(frame):
    updated_positions = initial_positions.copy()
    updated_positions[0, 1] -= get_trajectory(frame) * 0.5  # Head goes down
    updated_positions[1:3, 1] -= get_trajectory(frame) * 0.4  # Shoulders go down
    updated_positions[3:5, 1] -= get_trajectory(frame) * 0.3  # Elbows move slightly
    updated_positions[5:7, 1] -= get_trajectory(frame) * 0.2  # Hands stay relatively still
    updated_positions[7, 1] -= get_trajectory(frame) * 0.6  # Hip goes down more
    updated_positions[8:10, 1] -= get_trajectory(frame) * 0.5  # Knees bend
    updated_positions[10:12, 1] -= get_trajectory(frame) * 0.4  # Feet stay on ground
    updated_positions[12:15, 1] -= get_trajectory(frame) * 0.5  # Face moves with head
    
    scat.set_offsets(updated_positions)

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=50, repeat=False)

plt.show()
