
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 5)
ax.set_facecolor('black')
ax.set_xticks([], [])
ax.set_yticks([], [])

# Number of point-lights
num_points = 15
points_pos = np.array([
    [0, 4],       # head
    [-0.5, 3],    # left shoulder
    [0.5, 3],     # right shoulder
    [-0.5, 2.5],  # left elbow
    [0.5, 2.5],   # right elbow
    [-0.5, 2],    # left hand
    [0.5, 2],     # right hand
    [-0.5, 1],    # left hip
    [0.5, 1],     # right hip
    [-0.5, 0],    # left knee
    [0.5, 0],     # right knee
    [-0.5, -1],   # left ankle
    [0.5, -1],    # right ankle
    [0, 3.5],     # body
    [0, 1.5]      # body center
])

# Create scatter plot for point-lights
points = ax.scatter(points_pos[:, 0], points_pos[:, 1], color='white', s=100)

def update(frame):
    # Update positions for running motion
    global points_pos

    # Modify the y-coordinates to simulate running
    points_pos[:, 1] += np.sin(frame / 10) * 0.1  
    points_pos[:, 0] += np.sin(frame / 15) * 0.1  # left-right motion

    # Update points positions
    points.set_offsets(points_pos)
    
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show animation
plt.show()
