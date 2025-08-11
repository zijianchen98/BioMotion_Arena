
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights for the happy man with heavy weight
# Each point-light represents a joint in the body
point_lights = {
    'head': np.array([0, 10]),
    'left_shoulder': np.array([-3, 8]),
    'right_shoulder': np.array([3, 8]),
    'left_elbow': np.array([-5, 5]),
    'right_elbow': np.array([5, 5]),
    'left_wrist': np.array([-7, 2]),
    'right_wrist': np.array([7, 2]),
    'left_hip': np.array([-2, 0]),
    'right_hip': np.array([2, 0]),
    'left_knee': np.array([-2, -5]),
    'right_knee': np.array([2, -5]),
    'left_ankle': np.array([-2, -10]),
    'right_ankle': np.array([2, -10]),
    'left_foot': np.array([-2, -12]),
    'right_foot': np.array([2, -12]),
}

# Define the walking motion
def walking_motion(t):
    # Calculate the position of each point-light at time t
    positions = {
        'head': np.array([0, 10 + 2 * np.sin(t)]),
        'left_shoulder': np.array([-3 + 1 * np.sin(t), 8 + 1 * np.cos(t)]),
        'right_shoulder': np.array([3 + 1 * np.sin(t), 8 + 1 * np.cos(t)]),
        'left_elbow': np.array([-5 + 2 * np.sin(t), 5 + 2 * np.cos(t)]),
        'right_elbow': np.array([5 + 2 * np.sin(t), 5 + 2 * np.cos(t)]),
        'left_wrist': np.array([-7 + 3 * np.sin(t), 2 + 3 * np.cos(t)]),
        'right_wrist': np.array([7 + 3 * np.sin(t), 2 + 3 * np.cos(t)]),
        'left_hip': np.array([-2 + 1 * np.sin(t), 0 + 1 * np.cos(t)]),
        'right_hip': np.array([2 + 1 * np.sin(t), 0 + 1 * np.cos(t)]),
        'left_knee': np.array([-2 + 2 * np.sin(t), -5 + 2 * np.cos(t)]),
        'right_knee': np.array([2 + 2 * np.sin(t), -5 + 2 * np.cos(t)]),
        'left_ankle': np.array([-2 + 3 * np.sin(t), -10 + 3 * np.cos(t)]),
        'right_ankle': np.array([2 + 3 * np.sin(t), -10 + 3 * np.cos(t)]),
        'left_foot': np.array([-2 + 4 * np.sin(t), -12 + 4 * np.cos(t)]),
        'right_foot': np.array([2 + 4 * np.sin(t), -12 + 4 * np.cos(t)]),
    }
    return positions

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-15, 15)
ax.set_aspect('equal')
ax.set_facecolor('black')

def animate(t):
    ax.clear()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-15, 15)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    positions = walking_motion(t)
    for position in positions.values():
        ax.plot(position[0], position[1], 'o', markersize=5, color='white')

ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 2 * np.pi, 128), interval=50)

plt.show()
