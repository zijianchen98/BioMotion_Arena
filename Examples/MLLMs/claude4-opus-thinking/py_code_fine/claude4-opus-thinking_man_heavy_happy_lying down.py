
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Define the initial positions of the point lights (representing body joints)
# Example coordinates representing "lying down" orientation
initial_positions = np.array([
    [0, 0.1],   # Head
    [-0.1, 0.05], # Left shoulder
    [0.1, 0.05],  # Right shoulder
    [-0.15, 0],  # Left elbow
    [0.15, 0],   # Right elbow
    [-0.1, -0.05],  # Left hand
    [0.1, -0.05],  # Right hand
    [-0.1, -0.25],  # Left hip
    [0.1, -0.25],  # Right hip
    [-0.2, -0.4],  # Left knee
    [0.2, -0.4],  # Right knee
    [-0.15, -0.5],  # Left foot
    [0.15, -0.5],  # Right foot
    [0, -0.15],   # Torso
    [0, -0.3],    # Lower torso
    [0, -0.4],    # Mid torso
])

# Initialize frames for animation
num_frames = 60
positions = np.zeros((num_frames, initial_positions.shape[0], 2))

# Populate movements over time
for t in range(num_frames):
    # Simulate slight movements for realism
    positions[t] = initial_positions + np.array([
        np.sin(t/10) * 0.02,  # Slight head movement
        0.0,                  # No movement for simpler animation
    ]).reshape(-1, 1)

# Initialize the animation function
def init():
    points.set_data([], [])
    return points,

# Animation update function
def update(frame):
    points.set_data(positions[frame, :, 0], positions[frame, :, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_frames,
                              init_func=init, blit=True, interval=100)

# Show the animation
plt.show()
