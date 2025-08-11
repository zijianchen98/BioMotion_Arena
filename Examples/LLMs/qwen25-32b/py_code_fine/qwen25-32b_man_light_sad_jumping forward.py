
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')  # Hide the axes

# Initial positions of the point-lights
points = np.array([
    [4.5, 6],  # Head
    [4, 4],    # Left shoulder
    [5, 4],    # Right shoulder
    [3.5, 2],  # Left elbow
    [5.5, 2],  # Right elbow
    [3, 1],    # Left hand
    [6, 1],    # Right hand
    [4.5, 7],  # Spine
    [4, 5],    # Left hip
    [5, 5],    # Right hip
    [3.5, 3],  # Left knee
    [5.5, 3],  # Right knee
    [3, 2],    # Left foot
    [6, 2],    # Right foot
    [4.5, 9]   # Top (for height variation)
])

# Scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

def update(frame):
    global points
    
    # Jumping motion
    vertical_offset = 0.5 * np.sin(frame / 10.0)
    
    # Forward motion
    horizontal_offset = 0.05 * frame % 1
    
    # Update the position of each point
    points[:, 1] += vertical_offset
    points[:, 0] += horizontal_offset
    
    # Adjust the spine and head
    points[7][1] = points[8][1] + (points[0][1] - points[8][1]) * 0.5
    points[0][1] = points[7][1] + (points[14][1] - points[7][1]) * 0.5
    
    # Adjust arms and legs based on the jumping motion
    points[3][1] = points[8][1] - (points[0][1] - points[8][1]) * 0.3
    points[5][1] = points[3][1]
    points[11][1] = points[10][1] = points[8][1] - (points[0][1] - points[8][1]) * 0.7
    points[13][1] = points[12][1] = points[10][1]
    
    # Update the scatter plot
    scat.set_offsets(points)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

plt.show()
