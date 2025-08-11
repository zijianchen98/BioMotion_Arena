
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of frames for the animation
num_frames = 30

# Define starting positions (standing) for the 15 points
start_positions = np.array([
    [0, 10],   # head
    [0, 9],    # neck
    [-1, 9],   # left shoulder
    [1, 9],    # right shoulder
    [-1.5, 7], # left elbow
    [1.5, 7],  # right elbow
    [-1.5, 5], # left wrist
    [1.5, 5],  # right wrist
    [0, 7],    # torso center
    [-0.5, 5], # left hip
    [0.5, 5],  # right hip
    [-0.5, 3], # left knee
    [0.5, 3],  # right knee
    [-0.5, 1], # left ankle
    [0.5, 1]   # right ankle
])

# Define ending positions (sitting) for the 15 points
end_positions = np.array([
    [0, 6],    # head
    [0, 5],    # neck
    [-1, 5],   # left shoulder
    [1, 5],    # right shoulder
    [-1.5, 4], # left elbow
    [1.5, 4],  # right elbow
    [-1.5, 3], # left wrist
    [1.5, 3],  # right wrist
    [0, 4],    # torso center
    [-0.5, 2], # left hip
    [0.5, 2],  # right hip
    [-0.5, 1], # left knee
    [0.5, 1],  # right knee
    [-0.5, 0], # left ankle
    [0.5, 0]   # right ankle
])

# Set up the figure and axis with black background
fig, ax = plt.subplots()
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.set_xlim(-3, 3)
ax.set_ylim(0, 12)
ax.axis('off')

# Create the scatter plot for the point-lights
points = ax.scatter(start_positions[:, 0], start_positions[:, 1], color='white', s=50)

# Define the update function for the animation
def update(frame):
    t = frame / num_frames
    current_positions = (1 - t) * start_positions + t * end_positions
    points.set_offsets(current_positions)
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
