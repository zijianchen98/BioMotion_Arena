
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and frames
num_points = 15
num_frames = 200

# Create a figure and axis
fig, ax = plt.subplots()

# Set the background to black
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')

# Initial positions of the point lights (15 points for body)
points = np.array([
    [0, 4],  # head
    [-1, 3], [1, 3],  # shoulders
    [-1.5, 2.5], [1.5, 2.5],  # elbows
    [-2, 1], [2, 1],  # wrists
    [-1, 0], [1, 0],  # waist
    [-1, -1.5], [1, -1.5],  # knees
    [-1, -3], [1, -3],  # feet
]) 

# Function to update the points for rolling motion
def update(frame):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.axis('off')

    # Define rolling motion parameters
    rolling_offset = np.sin(frame / 10) * 0.5
    for i in range(num_points):
        y_offset = -2 + (i // 2) * 0.5  # Spread points vertically
        ax.plot(points[i, 0], points[i, 1] + rolling_offset + y_offset, 'wo', markersize=10)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

plt.show()
