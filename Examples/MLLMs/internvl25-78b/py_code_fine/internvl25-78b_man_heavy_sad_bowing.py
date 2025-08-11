
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
def init_positions():
    return np.array([
        [0, 1],  # Head
        [-0.5, 0.8],  # Shoulder left
        [0.5, 0.8],  # Shoulder right
        [-0.3, 0.5],  # Elbow left
        [0.3, 0.5],  # Elbow right
        [-0.5, 0.2],  # Hand left
        [0.5, 0.2],  # Hand right
        [0, 0],  # Spine top
        [0, -0.3],  # Spine mid
        [0, -0.6],  # Spine bottom
        [-0.2, -0.7],  # Hip left
        [0.2, -0.7],  # Hip right
        [-0.3, -0.9],  # Knee left
        [0.3, -0.9],  # Knee right
        [-0.4, -1.2],  # Foot left
        [0.4, -1.2]  # Foot right
    ])

# Function to update the positions of the points
def update_positions(i, points):
    offset = np.sin(i / 10) * 0.2
    points[0] = [0, 1 + offset]  # Head moves up and down
    points[1:3] += [0, 0.05 * np.sin(i / 10)]  # Shoulders
    points[3:5] += [0, 0.1 * np.sin(i / 10)]  # Elbows
    points[5:7] += [0, 0.15 * np.sin(i / 10)]  # Hands
    points[8] += [0, 0.1 * np.sin(i / 10)]  # Spine mid
    points[10:12] += [0, 0.05 * np.sin(i / 10)]  # Hips
    points[12:14] += [0, 0.1 * np.sin(i / 10)]  # Knees
    points[14:16] += [0, 0.15 * np.sin(i / 10)]  # Feet

# Animation function
def animate(i, scat, points):
    update_positions(i, points)
    scat.set_offsets(points)
    return scat,

# Initialize the plot
fig, ax = plt.subplots()
ax.set_facecolor('black')
points = init_positions()

# Create scatter plot
scat = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Set plot limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1.5, 1.5)

# Create animation
ani = animation.FuncAnimation(fig, animate, fargs=(scat, points), interval=50, blit=True)

plt.show()
