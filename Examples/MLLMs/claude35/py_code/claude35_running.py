
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define parameters
num_points = 15
duration = 5  # Duration of the animation in seconds
fps = 30      # Frames per second
total_frames = duration * fps

# Define the initial positions of the points representing the key joints in running
# This simulation will define a simple model for running.
initial_positions = np.array([
    [0, 1],   # Head
    [-0.5, 0.5],  # Left shoulder
    [0.5, 0.5],   # Right shoulder
    [-0.5, 0],  # Left elbow
    [0.5, 0],    # Right elbow
    [-0.5, -0.5],  # Left hip
    [0.5, -0.5],   # Right hip
    [-0.7, 0],    # Left knee
    [0.7, 0],     # Right knee
    [-1.0, -1],   # Left foot
    [1.0, -1],    # Right foot
    [0, 0],       # Center of mass
    [0, 0],       # Midpoint between shoulder joints
    [0, 0],       # Midpoint between hip joints
    [0, 0],       # Midpoint between knees
    [0, 0],       # Midpoint between feet
])

# Function to update positions of points based on running motion
def update_positions(frame):
    # Simple running motion model
    phase = 2 * np.pi * (frame / total_frames)
    
    running_positions = initial_positions.copy()
    # Adjust y-position for a simple leg movement
    running_positions[8, 1] += 0.2 * np.sin(phase)  # Left foot up-down
    running_positions[9, 1] -= 0.2 * np.sin(phase)  # Right foot down-up
    running_positions[5, 1] += 0.1 * np.sin(phase)  # Left hip up-down
    running_positions[6, 1] -= 0.1 * np.sin(phase)  # Right hip down-up
    running_positions[:, 0] += 0.02  # Move forward

    return running_positions.T

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)  # White points

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Animation function
def animate(frame):
    positions = update_positions(frame)
    points.set_data(positions[0], positions[1])
    return points,

# Call the animator
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=total_frames, interval=1000/fps, blit=True)

# Show the animation
plt.show()
