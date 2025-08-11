
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the joints and their connections
joints = {
    'head': 0,
    'neck': 1,
    'right_shoulder': 2,
    'right_elbow': 3,
    'right_hand': 4,
    'left_shoulder': 5,
    'left_elbow': 6,
    'left_hand': 7,
    'right_hip': 8,
    'right_knee': 9,
    'right_foot': 10,
    'left_hip': 11,
    'left_knee': 12,
    'left_foot': 13,
    'torso': 14
}

connections = [
    (joints['head'], joints['neck']),
    (joints['neck'], joints['right_shoulder']),
    (joints['right_shoulder'], joints['right_elbow']),
    (joints['right_elbow'], joints['right_hand']),
    (joints['neck'], joints['left_shoulder']),
    (joints['left_shoulder'], joints['left_elbow']),
    (joints['left_elbow'], joints['left_hand']),
    (joints['neck'], joints['torso']),
    (joints['torso'], joints['right_hip']),
    (joints['right_hip'], joints['right_knee']),
    (joints['right_knee'], joints['right_foot']),
    (joints['torso'], joints['left_hip']),
    (joints['left_hip'], joints['left_knee']),
    (joints['left_knee'], joints['left_foot'])
]

# Define the initial positions of the joints
initial_positions = np.array([
    [0, 1.8],  # head
    [0, 1.6],  # neck
    [-0.2, 1.5],  # right_shoulder
    [-0.4, 1.3],  # right_elbow
    [-0.6, 1.1],  # right_hand
    [0.2, 1.5],  # left_shoulder
    [0.4, 1.3],  # left_elbow
    [0.6, 1.1],  # left_hand
    [-0.2, 1.0],  # right_hip
    [-0.4, 0.6],  # right_knee
    [-0.6, 0.2],  # right_foot
    [0.2, 1.0],  # left_hip
    [0.4, 0.6],  # left_knee
    [0.6, 0.2],  # left_foot
    [0, 1.2]  # torso
])

# Define the animation function
def animate(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(0, 2)
    ax.set_aspect('equal')
    ax.axis('off')

    # Simulate the jumping motion
    t = frame / 100.0
    y_offset = np.sin(t * 2 * np.pi) * 0.5

    positions = initial_positions.copy()
    positions[:, 1] += y_offset

    # Draw the point-lights
    for i in range(len(positions)):
        ax.plot(positions[i, 0], positions[i, 1], 'wo', markersize=10)

    # Draw the connections
    for conn in connections:
        ax.plot([positions[conn[0], 0], positions[conn[1], 0]],
                [positions[conn[0], 1], positions[conn[1], 1]], 'w-', linewidth=2)

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

plt.show()
