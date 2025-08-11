
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the initial positions of the points (standing position)
initial_positions = np.array([
    [0, 2.0],  # Head
    [-0.3, 1.8], # Left Shoulder
    [0.3, 1.8],  # Right Shoulder
    [-0.6, 1.5], # Left Elbow
    [0.6, 1.5],  # Right Elbow
    [-0.9, 1.2], # Left Wrist
    [0.9, 1.2],  # Right Wrist
    [-0.1, 1.3], # Left Hip
    [0.1, 1.3],  # Right Hip
    [-0.3, 0.8], # Left Knee
    [0.3, 0.8],  # Right Knee
    [-0.5, 0.3], # Left Ankle
    [0.5, 0.3],  # Right Ankle
    [-0.1, 0.0], # Left Foot
    [0.1, 0.0],  # Right Foot
])

# Define the final positions of the points (sitting position)
final_positions = np.array([
    [0, 1.5],  # Head
    [-0.3, 1.3], # Left Shoulder
    [0.3, 1.3],  # Right Shoulder
    [-0.6, 1.0], # Left Elbow
    [0.6, 1.0],  # Right Elbow
    [-0.9, 0.7], # Left Wrist
    [0.9, 0.7],  # Right Wrist
    [-0.1, 0.8], # Left Hip
    [0.1, 0.8],  # Right Hip
    [-0.3, 0.3], # Left Knee
    [0.3, 0.3],  # Right Knee
    [-0.2, 0.1], # Left Ankle
    [0.2, 0.1],  # Right Ankle
    [-0.1, 0.0], # Left Foot
    [0.1, 0.0],  # Right Foot
])

# Number of frames for the animation
num_frames = 100

# Interpolate positions for each frame to create the sitting down motion
def sitting_motion(frame_num):
    t = frame_num / num_frames  # Normalize frame number
    positions = initial_positions + t * (final_positions - initial_positions)
    return positions

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)  # Adjust limits to frame the figure
ax.set_ylim(-0.5, 2.5)  # Adjust limits to frame the figure
ax.set_aspect('equal')
plt.axis('off')

# Create scatter plot for the points
points, = ax.plot([], [], 'wo', markersize=8)

# Animation function
def animate(frame_num):
    positions = sitting_motion(frame_num)
    x = positions[:, 0]
    y = positions[:, 1]
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

plt.show()
