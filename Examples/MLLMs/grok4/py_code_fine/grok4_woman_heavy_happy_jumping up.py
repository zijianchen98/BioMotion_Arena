
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
num_points = 15  # Total point lights
duration = 2  # Duration of the animation in seconds
fps = 30  # Frames per second

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 5)
ax.set_facecolor('black')
ax.axis('off')  # Hide axes

# Function to initialize points
def init():
    global points
    points = np.array([
        [-0.5, 0], [0.5, 0],  # Feet
        [-1, 1], [1, 1],      # Knees
        [-1.5, 2], [1.5, 2],  # Hips
        [-1, 3], [1, 3],      # Arms
        [0, 4],                # Head
        [0, 0],                # Center of mass
        [0.5, 1], [-0.5, 2],  # Jump assist points
        [0.3, 3.5], [-0.3, 3.5],  # Upper torso 
        [-1, 4], [1, 4]       # Hands
    ])
    points = ax.scatter(points[:, 0], points[:, 1], color='white', s=100)
    return points,

# Function to update points
def update(frame):
    t = frame / fps
    jump_height = np.abs(np.sin(np.pi * t))  # Jump motion
    new_positions = np.copy(points.get_offsets())
    
    # Update x positions to simulate arms and legs moving
    new_positions[0:2, 1] = jump_height * 2  # Feet
    new_positions[2:4, 1] = jump_height * 1.5  # Knees
    new_positions[4:6, 1] = jump_height  # Hips
    new_positions[6:8, 1] = jump_height  # Arms
    new_positions[8, 1] = jump_height + 1  # Head/helper point
    new_positions[9, 1] = jump_height  # Center of mass

    # Updating point positions
    points.set_offsets(new_positions)
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, duration * fps), init_func=init, blit=True, repeat=True)

# Display the animation
plt.show()
