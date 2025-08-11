
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
duration = 2  # seconds
frames_per_second = 30
total_frames = duration * frames_per_second

# Creating a figure
fig, ax = plt.subplots()

# Setting the background color to black
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_xticks([])
ax.set_yticks([])

# Function to create the initial positions of the point-lights
def initial_positions():
    # Arrange points in a basic body structure (approx)
    positions = np.array([
        [0, 1],  # Head
        [-0.5, 0.5],  # Left arm
        [0.5, 0.5],  # Right arm
        [-0.5, -0.5],  # Left leg
        [0.5, -0.5],  # Right leg
        [0, 0],  # Torso
    ])
    return positions

# Update function for animation
def update(frame):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Calculate the angle for the turning motion
    angle = (frame / total_frames) * 2 * np.pi  # Full rotation (360 degrees)

    # Generate positions for point-lights based on turning motion
    positions = initial_positions()
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    # Apply rotation
    rotated_positions = positions @ rotation_matrix

    # Plot the point-lights
    for (x, y) in rotated_positions:
        ax.plot(x, y, 'o', color='white', markersize=10)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=1000/frames_per_second)

# Display the animation
plt.show()
