
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Number of point-lights
num_points = 15

# Initial positions of point-lights
# 5 for the head and torso, 2 for each knee, and 3 for the feet
positions = np.array([
    [0, 0.8],   # Head
    [0, 0.5],   # Torso
    [-0.1, 0.45],  # Left Should
    [0.1, 0.45],   # Right Shoulder
    [-0.075, 0.25],  # Left Elbow
    [0.075, 0.25],   # Right Elbow
    [0, 0.1],   # Hip center
    [-0.1, 0.1],  # Left Hip
    [0.1, 0.1],  # Right Hip
    [-0.1, -0.2], # Left Knee
    [0.1, -0.2],  # Right Knee
    [-0.075, -0.5],  # Left Ankle
    [0.075, -0.5],   # Right Ankle
    [-0.15, -0.6], # Left Foot
    [0.15, -0.6],  # Right Foot
])

# Initialize point lights
point_lights, = ax.plot([], [], 'o', color='white', markersize=10)

# Update function for animation
def update(frame):
    # Simulate the downward movement for sitting down
    offset = frame * 0.01
    new_positions = positions.copy()
    new_positions[:, 1] -= offset
    
    point_lights.set_data(new_positions[:, 0], new_positions[:, 1])
    return point_lights,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 50), interval=50, blit=True)

# Display the animation
plt.show()
