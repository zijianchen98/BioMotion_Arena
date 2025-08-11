
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point lights
num_points = 15

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')

# Initial positions for 15 point lights (x, y)
# Representing positions of joints
points = np.array([
    [0, 2],   # Head
    [-0.5, 1], [0.5, 1],  # Shoulders
    [-1, 0.5], [1, 0.5],  # Arms
    [-0.5, 0], [0.5, 0],  # Elbows
    [-1, -1], [1, -1],    # Hands
    [0, 0],               # Torso
    [-0.5, -1], [0.5, -1], # Hips
    [-0.3, -1.5], [0.3, -1.5],  # Knees
    [-0.5, -2], [0.5, -2]  # Feet
])

# Update function for animation
def update(frame):
    ax.clear()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_facecolor('black')

    # Animate the bowing motion by modifying the y-coordinates
    bowing_factor = 0.1 * (frame % 30)  # Bowing motion over frames
    points[0, 1] -= bowing_factor  # Head moves downwards
    points[1:3, 1] -= bowing_factor / 2  # Shoulders slightly down
    points[4:6, 1] -= bowing_factor / 3  # Elbows slightly down
    points[8:10, 1] -= bowing_factor / 4  # Hips slightly down
    points[12:14, 1] -= bowing_factor / 5  # Feet slightly down

    # Draw the points
    ax.plot(points[:, 0], points[:, 1], 'o', color='white', markersize=10)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=60, interval=100)

# Display the animation
plt.show()
