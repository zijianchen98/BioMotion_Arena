
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights and frames
n_points = 15
n_frames = 100

# Define the initial positions of the point-lights
# These positions are chosen to represent a person lying down
initial_positions = np.array([
    [0.5, 0.5],  # Head
    [0.5, 0.3],  # Neck
    [0.4, 0.2],  # Shoulder
    [0.6, 0.2],  # Shoulder
    [0.4, 0.1],  # Elbow
    [0.6, 0.1],  # Elbow
    [0.4, 0.0],  # Wrist
    [0.6, 0.0],  # Wrist
    [0.5, 0.4],  # Hip
    [0.4, 0.5],  # Knee
    [0.6, 0.5],  # Knee
    [0.4, 0.6],  # Ankle
    [0.6, 0.6],  # Ankle
    [0.5, 0.7],  # Foot
    [0.5, 0.8]   # Foot
])

# Define the movement of each point-light over time
# These movements are chosen to represent a person lying down and moving their limbs
movements = np.array([
    [0.0, 0.0],  # Head
    [0.0, 0.0],  # Neck
    [0.1*np.sin(np.linspace(0, 2*np.pi, n_frames)), 0.0],  # Shoulder
    [-0.1*np.sin(np.linspace(0, 2*np.pi, n_frames)), 0.0],  # Shoulder
    [0.1*np.sin(np.linspace(0, 2*np.pi, n_frames)), 0.0],  # Elbow
    [-0.1*np.sin(np.linspace(0, 2*np.pi, n_frames)), 0.0],  # Elbow
    [0.1*np.sin(np.linspace(0, 2*np.pi, n_frames)), 0.0],  # Wrist
    [-0.1*np.sin(np.linspace(0, 2*np.pi, n_frames)), 0.0],  # Wrist
    [0.0, 0.0],  # Hip
    [0.1*np.sin(np.linspace(0, 2*np.pi, n_frames)), 0.0],  # Knee
    [-0.1*np.sin(np.linspace(0, 2*np.pi, n_frames)), 0.0],  # Knee
    [0.1*np.sin(np.linspace(0, 2*np.pi, n_frames)), 0.0],  # Ankle
    [-0.1*np.sin(np.linspace(0, 2*np.pi, n_frames)), 0.0],  # Ankle
    [0.1*np.sin(np.linspace(0, 2*np.pi, n_frames)), 0.0],  # Foot
    [-0.1*np.sin(np.linspace(0, 2*np.pi, n_frames)), 0.0]   # Foot
]).T

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the plot with the initial positions of the point-lights
points = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Define the update function for the animation
def update(frame):
    positions = initial_positions + movements[frame]
    points.set_offsets(positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=50)

plt.show()
