
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point lights
num_points = 15

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')  # Background color
ax.set_xticks([])  # Remove x ticks
ax.set_yticks([])  # Remove y ticks

# Initial positions of point lights (as a simple representation)
points = np.array([[0, -2],  # Center of body
                   [-0.5, -1.5], [0.5, -1.5],  # Legs
                   [-0.7, -1], [0.7, -1],  # Hips
                   [-1, 0], [1, 0],  # Arms
                   [-0.5, 1], [0.5, 1],  # Shoulders
                   [0, 2],  # Head
                   [0, 1.5],  # Upper back
                   [0.5, 1.5],  # Right elbow
                   [-0.5, 1.5], # Left elbow
                   [-0.7, 2],   # Right head position
                   [0.7, 2],    # Left head position
                   [0, 0.5]])   # Center chest

# Create scatter plot
sc = ax.scatter(points[:, 0], points[:, 1], color='white')

# Define update function
def update(frame):
    global points
    # Simple jumping motion
    height = 0.5 * np.sin(np.pi * frame / 20)  # Jumping up and down
    points[:, 1] = points[:, 1] + height
    
    # Ensure points are within bounds
    points[:, 1] = np.clip(points[:, 1], -3, 3)

    # Update scatter plot
    sc.set_offsets(points)
    return sc,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 80), interval=50, blit=True)

plt.show()
