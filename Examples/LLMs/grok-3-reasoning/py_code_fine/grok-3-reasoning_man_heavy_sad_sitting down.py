
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define standing positions
points_standing = np.array([
    [5, 0],   # head
    [5, 10],  # neck
    [3, 20],  # left shoulder
    [7, 20],  # right shoulder
    [2, 30],  # left elbow
    [8, 30],  # right elbow
    [1, 40],  # left wrist
    [9, 40],  # right wrist
    [5, 25],  # torso center
    [0, 50],  # left hip
    [10, 50], # right hip
    [0, 70],  # left knee
    [10, 70], # right knee
    [0, 100], # left ankle
    [10, 100] # right ankle
])

# Define seated positions
# For upper body, shift down by 30 units
shift = 30
points_seated = points_standing.copy()
points_seated[:9, 1] += shift  # shift y for head to torso center
# For hips, move to y=80
points_seated[9, 1] = 80  # left hip
points_seated[10, 1] = 80 # right hip
# For knees, set to calculated positions
points_seated[11] = [-17.32, 90]  # left knee
points_seated[12] = [27.32, 90]   # right knee
# Ankles remain the same

# Set up the figure
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-25, 35)
ax.set_ylim(0, 105)
ax.invert_yaxis()

# Create scatter plot
scatter = ax.scatter(points_standing[:,0], points_standing[:,1], c='white', s=50)

# Number of frames
N = 100

# Update function
def update(frame):
    t = frame / (N - 1)
    points = points_standing * (1 - t) + points_seated * t
    scatter.set_offsets(points)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=N, interval=50, blit=True)

# Show the animation
plt.show()
