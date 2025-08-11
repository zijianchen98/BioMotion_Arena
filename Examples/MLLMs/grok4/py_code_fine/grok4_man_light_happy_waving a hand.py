
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.axis('equal')
ax.axis('off')
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)

# Define the initial positions of the point lights (15 in total)
num_points = 15
points = np.array([
    [0, 2.5],     # head
    [-1.5, 1.5],  # left shoulder
    [1.5, 1.5],   # right shoulder
    [-1, 0.5],    # left elbow
    [1, 0.5],     # right elbow
    [-1.5, 0],    # left hand
    [1.5, 0],     # right hand
    [-2, -1.5],   # left knee
    [2, -1.5],    # right knee
    [-2, -3],     # left foot
    [2, -3],      # right foot
    [-1.5, 2.0],  # left wrist
    [1.5, 2.0],   # right wrist
    [0, 0.5],     # center of body
    [0, 3],       # hand waving position
    [0, 1.5]      # torso
])

def update(frame):
    ax.clear()
    ax.axis('equal')
    ax.axis('off')
    
    # Wave hand motion by modifying y position for right hand
    y_hand_offset = 0.5 * np.sin(np.radians(frame * 10))
    
    # Update the position of the right hand
    points[5, 1] = y_hand_offset  # Update right hand y position
    points[11, 1] = y_hand_offset + 0.5  # Update right wrist y position

    # Plot the points
    ax.scatter(points[:, 0], points[:, 1], c='white', s=100)

    # Set background color
    ax.set_facecolor('black')

# Create animation
ani = animation.FuncAnimation(fig, update, frames=60, interval=100)

# Show the animation
plt.show()
