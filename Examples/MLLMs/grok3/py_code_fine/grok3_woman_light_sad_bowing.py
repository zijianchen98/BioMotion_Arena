
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions and structure of the 15 point-lights for a bowing sad woman
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles, spine points
initial_positions = np.array([
    [0, 10],  # head
    [-2, 8], [2, 8],  # shoulders
    [-4, 6], [4, 6],  # elbows
    [-6, 4], [6, 4],  # wrists
    [0, 0],  # spine base
    [-1, -2], [1, -2],  # hips
    [-2, -6], [2, -6],  # knees
    [-3, -10], [3, -10],  # ankles
    [-1, -4], [1, -4]   # additional spine points for smooth bending
])

# Number of frames for the animation
n_frames = 60

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-12, 12)
ax.axis('off')

# Scatter plot for point-lights
points, = ax.plot([], [], 'wo', markersize=10)

def update(frame):
    # Calculate bowing motion: head and upper body move down, knees bend slightly
    angle = np.pi / 6 * (1 - np.cos(2 * np.pi * frame / n_frames))  # Smooth bowing motion
    positions = initial_positions.copy()
    
    # Apply bowing transformation
    for i in range(len(positions)):
        if i == 0:  # head
            positions[i] += [0, -5 * (1 - np.cos(angle))]
        elif i in [1, 2, 3, 4, 5, 9, 10]:  # upper body and arms
            positions[i] += [0, -3 * (1 - np.cos(angle))]
        elif i in [6, 7, 8]:  # lower spine and hips
            positions[i] += [0, -2 * (1 - np.cos(angle))]
        elif i in [11, 12, 13, 14]:  # legs
            positions[i, 1] += -6 * np.sin(angle) if i % 2 == 0 else -4 * np.sin(angle)
    
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=n_frames, interval=50, blit=True)

plt.show()
