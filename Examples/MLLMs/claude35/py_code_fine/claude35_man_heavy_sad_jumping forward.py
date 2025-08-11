
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set the number of points
num_points = 15

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(0, 10)
ax.set_facecolor('black')  # solid black background

# Initialize points representing the body parts in a sad man posture
points = np.array([
    [0, 9],   # head
    [-1, 8],  # left shoulder
    [1, 8],   # right shoulder
    [-1, 6],  # left elbow
    [1, 6],   # right elbow
    [-1, 4],  # left hand
    [1, 4],   # right hand
    [0, 7],   # torso
    [-1, 2],  # left knee
    [1, 2],   # right knee
    [0, 3],   # hip
    [0, 0],   # foot position
    [-1, 0],  # left foot
    [1, 0],   # right foot
])

# Create scatter plot for point lights
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Function to update the position of points
def update(frame):
    # Simple jumping motion logic
    jump_height = np.sin(np.radians(frame * 15)) * 2
    points[0, 1] = 9 + jump_height  # head
    points[1:3, 1] = 8 + jump_height / 4  # shoulders
    points[3:5, 1] = 6 + jump_height / 3  # elbows
    points[8:10, 1] = 2 + jump_height / 3  # knees
    points[5:7, 1] = 4 + jump_height / 3  # hands
    points[11:, 1] = -0.5 + jump_height / 2  # feet
    scat.set_offsets(points)  # Update the points on the scatter plot
    return scat,

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 60), blit=True, interval=50)

# Display the animation
plt.show()
