
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frame_rate = 30
duration = 5  # seconds
frames = frame_rate * duration

# Body part mapping (for simplicity, we map 15 points to represent a turning figure)
body_parts = {
    'head': [0],
    'torso': [1, 2, 3],
    'left_arm': [4, 5],
    'right_arm': [6, 7],
    'left_leg': [8, 9],
    'right_leg': [10, 11],
    'feet': [12, 13, 14]
}

# Initial positions for the lights
positions = np.array([
    [0, 0],   # head
    [-0.5, -0.5], [0, -0.5], [0.5, -0.5],  # torso
    [-1, -1], [-1.5, -1.5],  # left arm
    [1, -1], [1.5, -1.5],  # right arm
    [-1, -2], [-1, -3],  # left leg
    [1, -2], [1, -3],  # right leg
    [-1.5, -3.5], [-1, -3.5], [0.5, -3.5]  # feet
])

# Function to update the positions based on the turning angle
def update_positions(i):
    angle = 2 * np.pi * i / frames
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    
    # Apply different rotations to different body parts
    new_positions = positions.copy()
    for part, indices in body_parts.items():
        if part == 'head':
            new_positions[indices] = np.dot(positions[indices], rotation_matrix)
        elif part in ['left_arm', 'left_leg']:
            new_positions[indices] = np.dot(positions[indices], rotation_matrix) * 0.9
        elif part in ['right_arm', 'right_leg']:
            new_positions[indices] = np.dot(positions[indices], rotation_matrix) * 1.1
        else:
            new_positions[indices] = np.dot(positions[indices], rotation_matrix)
    
    return new_positions

# Setup the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 1)
ax.axis('off')

# Scatter plot for the point-lights
scatter = ax.scatter([], [], s=50, c='white')

def animate(i):
    scatter.set_offsets(update_positions(i))
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=1000/frame_rate, blit=True)

plt.show()
