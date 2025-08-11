
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
frames = 60
fps = 24

# Initial positions of the points (approximate)
initial_positions = np.array([
    [0.5, 0.9],  # Head
    [0.4, 0.7],  # Left Shoulder
    [0.6, 0.7],  # Right Shoulder
    [0.3, 0.5],  # Left Elbow
    [0.7, 0.5],  # Right Elbow
    [0.2, 0.3],  # Left Hand
    [0.8, 0.3],  # Right Hand
    [0.5, 0.6],  # Torso Top
    [0.5, 0.4],  # Torso Bottom
    [0.4, 0.3],  # Left Hip
    [0.6, 0.3],  # Right Hip
    [0.3, 0.1],  # Left Knee
    [0.7, 0.1],  # Right Knee
    [0.2, -0.1], # Left Foot
    [0.8, -0.1]  # Right Foot
])

# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(-0.5, 1)
ax.set_aspect('equal')
ax.axis('off')

# Points plot
points, = ax.plot([], [], 'o', markersize=10, color='white')

def init():
    points.set_data([], [])
    return points,

def animate(i):
    t = i / frames * 2 * np.pi  # Time parameter
    positions = initial_positions.copy()

    # Jumping motion
    jump_height = 0.2 * np.sin(t)
    positions[:, 1] += jump_height

    # Arm swing
    arm_angle = 0.5 * np.sin(t + np.pi / 2)
    positions[3, 0] -= arm_angle * 0.1
    positions[4, 0] += arm_angle * 0.1

    # Leg swing
    leg_angle = 0.5 * np.sin(t)
    positions[11, 0] -= leg_angle * 0.1
    positions[12, 0] += leg_angle * 0.1

    points.set_data(positions[:, 0], positions[:, 1])
    return points,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, interval=1000/fps, blit=True)

plt.show()
