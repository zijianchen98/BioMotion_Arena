
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_POINTS = 15
FRAME_RATE = 30
DURATION = 5  # seconds
TOTAL_FRAMES = FRAME_RATE * DURATION

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of the points for a standing person
initial_positions = np.array([
    [0.0, 0.9],  # Head
    [-0.1, 0.7], # Left eye
    [0.1, 0.7],  # Right eye
    [0.0, 0.6],  # Nose
    [0.0, 0.5],  # Neck
    [-0.1, 0.4], # Left shoulder
    [0.1, 0.4],  # Right shoulder
    [-0.2, 0.3], # Left elbow
    [0.2, 0.3],  # Right elbow
    [-0.3, 0.2], # Left hand
    [0.3, 0.2],  # Right hand
    [0.0, 0.3],  # Spine
    [-0.1, 0.2], # Left hip
    [0.1, 0.2],  # Right hip
    [0.0, 0.1]   # Waist
])

# Create scatter plot for points
points, = ax.plot([], [], 'o', color='white', markersize=10)

def init():
    points.set_data([], [])
    return points,

def animate(frame):
    t = frame / TOTAL_FRAMES
    positions = initial_positions.copy()

    # Bowing motion
    bow_amplitude = 0.2 * np.sin(2 * np.pi * t)
    positions[:, 1] -= bow_amplitude

    # Arm swing
    arm_swing = 0.1 * np.sin(2 * np.pi * (t + 0.25))
    positions[[8, 9], 0] += arm_swing  # Left hand
    positions[[10, 11], 0] -= arm_swing  # Right hand

    points.set_data(positions[:, 0], positions[:, 1])
    return points,

ani = animation.FuncAnimation(fig, animate, frames=TOTAL_FRAMES, init_func=init, blit=True, interval=1000/FRAME_RATE)
plt.show()
