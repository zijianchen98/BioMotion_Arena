
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial joint positions for a sadman
def initialize_positions():
    positions = np.array([
        [0, 1],  # head
        [-0.1, 0.9],  # neck
        [-0.2, 0.8],  # upper body
        [-0.3, 0.7],  # lower body
        [-0.25, 0.75],  # left shoulder
        [-0.35, 0.65],  # left elbow
        [-0.45, 0.55],  # left hand
        [0.25, 0.75],  # right shoulder
        [0.35, 0.65],  # right elbow
        [0.45, 0.55],  # right hand
        [-0.1, 0.4],  # left hip
        [-0.2, 0.3],  # left knee
        [-0.25, 0.1],  # left foot
        [0.1, 0.4],  # right hip
        [0.2, 0.3],  # right knee
        [0.25, 0.1],  # right foot
    ])
    return positions

# Wave the right hand
def wave_hand(frame, positions):
    angle = np.sin(frame / 10) * 0.1
    positions[9] = positions[8] + np.array([np.cos(angle), np.sin(angle)]) * 0.1
    return positions

# Update function for animation
def update(frame, positions, scat):
    new_positions = wave_hand(frame, positions.copy())
    scat.set_offsets(new_positions)
    return scat,

# Initialize positions
positions = initialize_positions()

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Create scatter plot for point lights
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, fargs=(positions, scat), interval=50, blit=True)

plt.axis('off')
plt.show()
