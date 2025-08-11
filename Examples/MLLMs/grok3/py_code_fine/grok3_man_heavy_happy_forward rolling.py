
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of 15 point-lights for a "happyman" in forward rolling pose
# Approximate joint positions (normalized to [0, 1] range)
t = 0
dt = 0.1
frames = 100

# Initial positions for 15 point-lights (head, shoulders, elbows, wrists, hips, knees, ankles, torso)
initial_positions = np.array([
    [0.5, 0.9],  # Head
    [0.4, 0.7],  # Left shoulder
    [0.3, 0.6],  # Left elbow
    [0.2, 0.5],  # Left wrist
    [0.6, 0.7],  # Right shoulder
    [0.7, 0.6],  # Right elbow
    [0.8, 0.5],  # Right wrist
    [0.45, 0.5], # Left hip
    [0.55, 0.5], # Right hip
    [0.4, 0.3],  # Left knee
    [0.5, 0.2],  # Left ankle
    [0.6, 0.3],  # Right knee
    [0.5, 0.1],  # Right ankle
    [0.5, 0.6],  # Upper torso
    [0.5, 0.4]   # Lower torso
])

# Function to update positions for forward rolling motion
def update_positions(t):
    # Simulate forward rolling motion with biomechanical plausibility
    # Rotate and translate positions to mimic rolling
    angle = np.pi * t / 10  # Rolling motion over time
    center = [0.5, 0.5]     # Center of rotation
    positions = initial_positions - center
    # Rotate around center
    rotated = np.array([
        positions[:, 0] * np.cos(angle) - positions[:, 1] * np.sin(angle),
        positions[:, 0] * np.sin(angle) + positions[:, 1] * np.cos(angle)
    ]).T
    # Translate forward
    translated = rotated + center + [t * 0.01, 0]  # Forward movement
    # Ensure positions stay within [0, 1] range
    translated = np.clip(translated, 0, 1)
    return translated

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
scatter = ax.scatter([], [], c='white', s=50)

# Animation update function
def update(frame):
    global t
    t += dt
    positions = update_positions(t)
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.show()
