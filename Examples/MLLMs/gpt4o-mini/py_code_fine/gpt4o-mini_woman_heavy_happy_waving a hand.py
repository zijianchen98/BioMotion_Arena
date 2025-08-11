
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the setup for the animation
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')

# Define the initial positions of the points representing the happy woman's body in a waving motion
num_points = 15
points = np.zeros((num_points, 2))

# Assign initial positions for the point-lights representing an approximate body structure
# Indices correspond to different parts of the body
points[0] = [0, 5]   # head
points[1] = [0, 4]   # neck
points[2] = [-1, 3]  # left shoulder
points[3] = [1, 3]   # right shoulder
points[4] = [-1, 1]  # left elbow
points[5] = [1, 1]   # right elbow
points[6] = [-1.5, 0]# left hand
points[7] = [1.5, 0] # right hand
points[8] = [0, 3]   # torso
points[9] = [0, 2]   # waist
points[10] = [-1, -1] # left knee
points[11] = [1, -1]  # right knee
points[12] = [-1, -3] # left ankle
points[13] = [1, -3]  # right ankle
points[14] = [0, -4]  # feet

# Create a scatter plot
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Define the waving motion pattern (for simplicity, we will animate the right hand)
def update(frame):
    # Calculate the new positions for the points based on a simple waving motion
    points[6, 1] = np.sin(frame / 5)  # adjust left hand
    points[7, 1] = 1.5 * np.sin(frame / 5 + np.pi / 2)  # right hand going up and down
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

# Show the animation
plt.show()
