
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights
point_lights = {
    'head': np.array([0, 1]),
    'left_shoulder': np.array([-0.5, 0.8]),
    'right_shoulder': np.array([0.5, 0.8]),
    'left_elbow': np.array([-0.7, 0.4]),
    'right_elbow': np.array([0.7, 0.4]),
    'left_wrist': np.array([-0.8, 0.1]),
    'right_wrist': np.array([0.8, 0.1]),
    'left_hip': np.array([-0.3, -0.5]),
    'right_hip': np.array([0.3, -0.5]),
    'left_knee': np.array([-0.4, -0.8]),
    'right_knee': np.array([0.4, -0.8]),
    'left_ankle': np.array([-0.5, -1.1]),
    'right_ankle': np.array([0.5, -1.1]),
    'left_foot': np.array([-0.6, -1.2]),
    'right_foot': np.array([0.6, -1.2]),
}

# Define the movement of each point-light
def move_point_lights(frame):
    movement = np.array([
        [0, 0],  # head
        [-0.1 * np.sin(frame / 10), 0],  # left_shoulder
        [0.1 * np.sin(frame / 10), 0],  # right_shoulder
        [-0.2 * np.sin(frame / 10), 0.1 * np.cos(frame / 10)],  # left_elbow
        [0.2 * np.sin(frame / 10), 0.1 * np.cos(frame / 10)],  # right_elbow
        [-0.3 * np.sin(frame / 10), 0.2 * np.cos(frame / 10)],  # left_wrist
        [0.3 * np.sin(frame / 10), 0.2 * np.cos(frame / 10)],  # right_wrist
        [-0.1 * np.sin(frame / 10), -0.1 * np.cos(frame / 10)],  # left_hip
        [0.1 * np.sin(frame / 10), -0.1 * np.cos(frame / 10)],  # right_hip
        [-0.2 * np.sin(frame / 10), -0.2 * np.cos(frame / 10)],  # left_knee
        [0.2 * np.sin(frame / 10), -0.2 * np.cos(frame / 10)],  # right_knee
        [-0.3 * np.sin(frame / 10), -0.3 * np.cos(frame / 10)],  # left_ankle
        [0.3 * np.sin(frame / 10), -0.3 * np.cos(frame / 10)],  # right_ankle
        [-0.4 * np.sin(frame / 10), -0.4 * np.cos(frame / 10)],  # left_foot
        [0.4 * np.sin(frame / 10), -0.4 * np.cos(frame / 10)],  # right_foot
    ])
    return {key: point_lights[key] + movement[i] for i, key in enumerate(point_lights)}

# Create the animation
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

def animate(frame):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    point_lights_moved = move_point_lights(frame)
    for point_light in point_lights_moved.values():
        ax.plot(point_light[0], point_light[1], 'o', markersize=5, color='white')

ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
