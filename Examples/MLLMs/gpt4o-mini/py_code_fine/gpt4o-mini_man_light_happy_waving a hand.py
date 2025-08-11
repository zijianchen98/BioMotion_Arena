
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')

# Define the points for a happy man waving
# The positions of points represented as (x, y)
points = np.array([
    [0, 1],    # Head
    [-0.5, 0.5],  # Left shoulder
    [0.5, 0.5],   # Right shoulder
    [-0.5, 0],     # Left elbow
    [0.5, 0],      # Right elbow
    [-0.8, -0.5],  # Left hand
    [0.8, -0.5],   # Right hand
    [-0.3, 0],     # Left wrist
    [0.3, 0],      # Right wrist
    [0, -1],       # Body
    [-0.5, -1.5],  # Left leg
    [0.5, -1.5],   # Right leg
    [-0.5, -0.5],  # Left knee
    [0.5, -0.5],   # Right knee
    [0, 0],        # Center point
    [0, 0]         # Not used
])

# Adjust hand position for waving
def animate(frame):
    ax.clear()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_facecolor('black')

    # Waving animation with some sine wave motion
    wave_movement = 0.3 * np.sin(frame / 10.0)
    points[5][1] = -0.5 + wave_movement  # Adjust left hand position
    points[6][1] = -0.5 + wave_movement  # Adjust right hand position
    
    # Draw the points
    ax.scatter(points[:, 0], points[:, 1], color='white', s=100)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50)

plt.show()
