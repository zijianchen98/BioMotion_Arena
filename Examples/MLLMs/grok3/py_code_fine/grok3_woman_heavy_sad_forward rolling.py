
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions of 15 point-lights (approximating a human figure rolling forward)
# These are simplified coordinates for head, torso, arms, legs, and joints
t = np.linspace(0, 2 * np.pi, 100)  # Time steps for one full roll
num_points = 15
positions = np.zeros((num_points, 2, len(t)))

# Approximate joint positions for a rolling woman (simplified biomechanics)
# Head, shoulders, elbows, wrists, hips, knees, ankles, torso points
base_positions = [
    [0, 1], [0.5, 0.8], [-0.5, 0.8], [1, 0.5], [-1, 0.5],  # Head, shoulders, elbows
    [0.7, 0], [-0.7, 0], [0.5, -0.2], [-0.5, -0.2], [0, -0.5],  # Wrists, hips, knees
    [0.3, -0.7], [-0.3, -0.7], [0, -1], [0.2, -0.3], [-0.2, -0.3]  # Ankles, torso points
]

# Simulate rolling motion (circular path with slight oscillation for natural movement)
radius = 1.0
for i in range(num_points):
    x = radius * np.cos(t + i * 0.1) + base_positions[i][0] * np.sin(t)
    y = radius * np.sin(t + i * 0.1) + base_positions[i][1] * np.cos(t)
    positions[i] = np.array([x, y])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Scatter plot for point-lights
scat = ax.scatter([], [], c='white', s=100)

# Animation update function
def update(frame):
    scat.set_offsets(positions[:, :, frame].T)
    return scat,

# Create animation
ani = FuncAnimation(fig, update, frames=len(t), interval=50, blit=True)

plt.show()
