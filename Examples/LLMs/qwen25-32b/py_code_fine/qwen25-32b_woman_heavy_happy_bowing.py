
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights representing the bowing woman
initial_positions = {
    'head': np.array([0.5, 0.8]),
    'left_shoulder': np.array([0.4, 0.7]),
    'right_shoulder': np.array([0.6, 0.7]),
    'left_elbow': np.array([0.3, 0.6]),
    'right_elbow': np.array([0.7, 0.6]),
    'left_hand': np.array([0.2, 0.5]),
    'right_hand': np.array([0.8, 0.5]),
    'left_hip': np.array([0.4, 0.4]),
    'right_hip': np.array([0.6, 0.4]),
    'left_knee': np.array([0.4, 0.3]),
    'right_knee': np.array([0.6, 0.3]),
    'left_ankle': np.array([0.4, 0.2]),
    'right_ankle': np.array([0.6, 0.2]),
    'left_toe': np.array([0.4, 0.1]),
    'right_toe': np.array([0.6, 0.1])
}

# Bowing motion parameters
max_bow_angle = 45  # Maximum bow angle in degrees
bow_speed = 0.5  # Speed of the bowing motion
time_steps = 100  # Number of frames in the animation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide axes

# Scatter plot for point-lights
scat = ax.scatter([], [], color='white')

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    angle = np.radians(max_bow_angle * np.sin(bow_speed * frame / time_steps * 2 * np.pi))
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    
    new_positions = {}
    for key, pos in initial_positions.items():
        new_pos = np.dot(rotation_matrix, pos - np.array([0.5, 0.5])) + np.array([0.5, 0.5])
        new_positions[key] = new_pos
    
    scat.set_offsets(list(new_positions.values()))
    return scat,

ani = FuncAnimation(fig, update, frames=np.arange(time_steps),
                    init_func=init, blit=True, repeat=True)

plt.show()
