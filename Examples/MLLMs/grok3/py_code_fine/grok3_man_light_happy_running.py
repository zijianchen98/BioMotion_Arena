
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions for 15 point-lights representing a running human (stick figure approximation)
# Positions are normalized to [0, 1] for a unit square
initial_positions = np.array([
    [0.5, 0.8],  # Head
    [0.45, 0.65], [0.55, 0.65],  # Shoulders
    [0.4, 0.5], [0.6, 0.5],  # Elbows
    [0.35, 0.35], [0.65, 0.35],  # Hands
    [0.5, 0.6],  # Chest
    [0.45, 0.4], [0.55, 0.4],  # Hips
    [0.4, 0.2], [0.6, 0.2],  # Knees
    [0.35, 0.05], [0.65, 0.05]  # Feet
])

# Number of frames for one complete running cycle
n_frames = 60
positions = np.zeros((n_frames, 15, 2))

# Simulate running motion with biomechanical plausibility
for i in range(n_frames):
    t = i / n_frames * 2 * np.pi  # Cycle through one period
    # Head and torso move slightly up and down
    positions[i, 0, 1] = 0.8 + 0.05 * np.sin(t)  # Head
    positions[i, 6, 1] = 0.6 + 0.05 * np.sin(t)  # Chest
    # Shoulder and hip oscillation
    positions[i, 1:3, 0] = 0.45 + 0.05 * np.sin(t), 0.55 - 0.05 * np.sin(t)  # Shoulders
    positions[i, 7:9, 0] = 0.45 + 0.05 * np.cos(t), 0.55 - 0.05 * np.cos(t)  # Hips
    # Arm movement (elbows and hands)
    positions[i, 3, 0] = 0.4 + 0.1 * np.sin(t + np.pi/2)
    positions[i, 4, 0] = 0.6 - 0.1 * np.sin(t + np.pi/2)
    positions[i, 5, 0] = 0.35 + 0.15 * np.sin(t + np.pi)
    positions[i, 6, 0] = 0.65 - 0.15 * np.sin(t + np.pi)
    # Leg movement (knees and feet)
    positions[i, 9, 0] = 0.4 + 0.1 * np.cos(t)
    positions[i, 10, 0] = 0.6 - 0.1 * np.cos(t)
    positions[i, 11, 0] = 0.35 + 0.15 * np.cos(t + np.pi/2)
    positions[i, 12, 0] = 0.65 - 0.15 * np.cos(t + np.pi/2)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Scatter plot for point-lights
scat = ax.scatter([], [], c='white', s=50)

# Animation update function
def update(frame):
    scat.set_offsets(positions[frame])
    return scat,

# Create animation
ani = FuncAnimation(fig, update, frames=n_frames, interval=50, blit=True, repeat=True)

# Display the animation
plt.show()
