
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create the point-light positions for the bowing action
def generate_bowing_motion(num_frames):
    # Create a simple bowing motion trajectory
    positions = []
    for frame in range(num_frames):
        # Iterating for a bowing movement
        y_offset = -0.5 * np.sin(frame / num_frames * np.pi)  # Bowing down
        x_offset = 0
        
        # Define body joints; in a real model, positions should be biomechanically realistic.
        joints = np.array([
            [x_offset, 1 + y_offset],  # Head
            [x_offset, 0.7 + y_offset],  # Shoulders
            [-0.1 + x_offset, 0.5 + y_offset],  # Left Hand
            [0.1 + x_offset, 0.5 + y_offset],  # Right Hand
            [x_offset, 0.3 + y_offset],  # Waist
            [-0.2 + x_offset, 0 + y_offset],  # Left Foot
            [0.2 + x_offset, 0 + y_offset],  # Right Foot
        ])
        
        positions.append(joints)
    return np.array(positions)

# Parameters
num_frames = 60  # Total frames for the animation
points = generate_bowing_motion(num_frames)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 2)
ax.set_facecolor('black')
points_scatters = [ax.plot([], [], 'o', color='white')[0] for _ in range(7)]

# Initialization function
def init():
    for scatter in points_scatters:
        scatter.set_data([], [])
    return points_scatters

# Animation function
def update(frame):
    for i, scatter in enumerate(points_scatters):
        scatter.set_data(points[frame, i, 0], points[frame, i, 1])
    return points_scatters

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, interval=1000/24)

# Show the animation
plt.show()
