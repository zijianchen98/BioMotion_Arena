
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the subject and action
subject = 'sadman'
action = 'bowing'

# Set the number of points and the frame rate
num_points = 15
frame_rate = 30

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim((-5, 8)
ax.set_ylim((-4, 4))
ax.set_aspect('equal')
ax.axis('off')

# Initialize the positions of the points
points = np.random.rand(num_points, 2) * 6

def update(frame):
    global points
    # Calculate new positions based on action
    if action == 'bowing':
        # Bowing motion logic
        points[:, 0] -= np.sin(frame / frame_rate) * 0.5
        points[:, 1] += np.cos(frame / frame_rate) * 0.5
    else:
        # Default motion logic
        points += np.random.normal((0.1, size=(num_points, 2))
    
    # Ensure points stay within the boundaries
    points[points > 8] = 7
    points[points < -8] = -8
    ax.clear()
    ax.scatter(points[:, 0], points[:, 1], s=100, c='white')
    ax.set_facecolor('black')

ani = FuncAnimation(fig, update, frames=np.arange((0, 1000), interval=1000/frame_rate)

plt.show()
