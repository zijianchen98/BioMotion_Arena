
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 200
dt = 0.1

# Initial positions and velocities (x, y)
initial_positions = np.array([
    [0.5, 0.1],  # Head
    [0.4, 0.2],  # Left Shoulder
    [0.6, 0.2],  # Right Shoulder
    [0.3, 0.3],  # Left Elbow
    [0.7, 0.3],  # Right Elbow
    [0.2, 0.4],  # Left Wrist
    [0.8, 0.4],  # Right Wrist
    [0.5, 0.5],  # Torso
    [0.4, 0.6],  # Left Hip
    [0.6, 0.6],  # Right Hip
    [0.3, 0.7],  # Left Knee
    [0.7, 0.7],  # Right Knee
    [0.2, 0.8],  # Left Ankle
    [0.8, 0.8],  # Right Ankle
    [0.5, 0.9]   # Feet Center
])

# Define the movement functions for each part of the body
def move_head(t):
    return np.array([0.5 + 0.02 * np.sin(0.5 * t), 0.1])

def move_left_shoulder(t):
    return np.array([0.4 + 0.01 * np.sin(0.5 * t), 0.2])

def move_right_shoulder(t):
    return np.array([0.6 + 0.01 * np.sin(0.5 * t), 0.2])

def move_left_elbow(t):
    return np.array([0.3 + 0.01 * np.sin(0.5 * t), 0.3])

def move_right_elbow(t):
    return np.array([0.7 + 0.01 * np.sin(0.5 * t), 0.3])

def move_left_wrist(t):
    return np.array([0.2 + 0.01 * np.sin(0.5 * t), 0.4])

def move_right_wrist(t):
    return np.array([0.8 + 0.01 * np.sin(0.5 * t), 0.4])

def move_torso(t):
    return np.array([0.5, 0.5])

def move_left_hip(t):
    return np.array([0.4 + 0.02 * np.sin(0.5 * t), 0.6])

def move_right_hip(t):
    return np.array([0.6 + 0.02 * np.sin(0.5 * t), 0.6])

def move_left_knee(t):
    return np.array([0.3 + 0.02 * np.sin(0.5 * t) + 0.05 * np.sin(1.0 * t), 0.7])

def move_right_knee(t):
    return np.array([0.7 + 0.02 * np.sin(0.5 * t) - 0.05 * np.sin(1.0 * t), 0.7])

def move_left_ankle(t):
    return np.array([0.2 + 0.02 * np.sin(0.5 * t) + 0.1 * np.sin(1.5 * t), 0.8])

def move_right_ankle(t):
    return np.array([0.8 + 0.02 * np.sin(0.5 * t) - 0.1 * np.sin(1.5 * t), 0.8])

def move_feet_center(t):
    return np.array([0.5, 0.9])

# List of movement functions
movement_functions = [
    move_head,
    move_left_shoulder,
    move_right_shoulder,
    move_left_elbow,
    move_right_elbow,
    move_left_wrist,
    move_right_wrist,
    move_torso,
    move_left_hip,
    move_right_hip,
    move_left_knee,
    move_right_knee,
    move_left_ankle,
    move_right_ankle,
    move_feet_center
]

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=100, c='white')

# Update function for animation
def update(frame):
    t = frame * dt
    new_positions = np.array([func(t) for func in movement_functions])
    scat.set_offsets(new_positions)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

# Show plot
plt.show()
