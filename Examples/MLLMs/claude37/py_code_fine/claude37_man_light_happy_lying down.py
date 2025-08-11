
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of point lights
num_points = 15

# Initial positions for the point lights representing a lying figure
initial_positions = np.array([
    [0, 1],     # Head
    [-0.5, 0.5], # Left Shoulder
    [0.5, 0.5],  # Right Shoulder
    [-0.5, 0],   # Left Elbow
    [0.5, 0],    # Right Elbow
    [-0.5, -0.5], # Left Knee
    [0.5, -0.5],  # Right Knee
    [0, 0.5],     # Chest
    [0, 0],       # Hip
    [0, -0.5],    # Center of the body (Pelvis)
    [-0.3, -0.5], # Left Foot
    [0.3, -0.5],  # Right Foot
])

# Setting up the figure
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
points, = ax.plot(initial_positions[:, 0], initial_positions[:, 1], 'o', color='white', markersize=10)

# Animation function
def update(frame):
    # Simulated smooth motion (you can tweak the values for more realism)
    offset = np.sin(frame / 10) * 0.02
    new_positions = initial_positions + np.array([[offset, 0]] * num_points)
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

# Display the animation
plt.show()
