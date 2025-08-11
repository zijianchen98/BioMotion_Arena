
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the number of points in the point-light display
num_points = 15

# Define the initial positions of the points
# (x, y) coordinates for each point
initial_positions = np.array([
    [0.0, 2.0],  # head
    [-0.5, 1.5], # left shoulder
    [0.5, 1.5],  # right shoulder
    [-1.0, 1.0], # left elbow
    [1.0, 1.0],   # right elbow
    [-1.5, 0.5], # left wrist
    [1.5, 0.5],  # right wrist
    [-0.2, 0.5], # left hip
    [0.2, 0.5],  # right hip
    [-0.7, 0.0], # left knee
    [0.7, 0.0],  # right knee
    [-0.7, -0.7], # left ankle
    [0.7, -0.7],  # right ankle
    [-0.2, -1.2], # left foot
    [0.2, -1.2]   # right foot
])

# Define the range for random motion
motion_range = 0.05

# Define the function to update the positions of the points for each frame
def update_points(frame_num):
    # Generate random motion for each point
    motion = np.random.uniform(-motion_range, motion_range, size=(num_points, 2))
    
    # Update the positions of the points
    new_positions = initial_positions + motion
    
    # Update the plot with the new positions
    scatter.set_offsets(new_positions)
    
    return scatter,

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')

# Set the limits of the axes
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Remove the axes ticks and labels
ax.set_xticks([])
ax.set_yticks([])

# Create the scatter plot for the points
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update_points, frames=num_frames, blit=True)

# Display the animation
plt.show()
