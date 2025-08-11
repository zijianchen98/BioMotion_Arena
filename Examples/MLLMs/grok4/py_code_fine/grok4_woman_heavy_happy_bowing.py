
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and frames
num_points = 15
frames = 100

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(0, 10)
ax.set_facecolor('black')  # Background color

# Initialize points
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to update the animation's frame
def update(frame):
    # Generate movement patterns based on a "bowing" action
    # Example static positions for point lights in a bowing pose
    # These need to change to simulate the bowing action
    bowing_pattern = np.array([
        [0, 3 + np.sin(frame * 0.1) * 0.5],  # Head
        [-1, 2 + np.sin(frame * 0.1) * 0.5],  # Left shoulder
        [1, 2 + np.sin(frame * 0.1) * 0.5],   # Right shoulder
        [-1.5, 1.5 + np.sin(frame * 0.1) * 0.5],  # Left elbow
        [1.5, 1.5 + np.sin(frame * 0.1) * 0.5],   # Right elbow
        [-1.2, 1 + np.sin(frame * 0.1) * 0.5],  # Left wrist
        [1.2, 1 + np.sin(frame * 0.1) * 0.5],   # Right wrist
        [-2, 0 + np.sin(frame * 0.1) * 0.5],   # Left hand (weight)
        [2, 0 + np.sin(frame * 0.1) * 0.5],    # Right hand (weight)
        [0, 0.5 + np.sin(frame * 0.1) * 0.5],  # Body center
        [-0.5, -1],  # Left hip
        [0.5, -1],   # Right hip
        [-1, -2],    # Left knee
        [1, -2],     # Right knee
        [0, -3],     # Ankle
    ])

    points.set_data(bowing_pattern[:, 0], bowing_pattern[:, 1])
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=50)

# Show the animation
plt.show()
