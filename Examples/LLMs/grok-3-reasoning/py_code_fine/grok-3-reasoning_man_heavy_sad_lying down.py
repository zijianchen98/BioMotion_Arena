
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of the 15 points at t=0 (standing position)
P0 = np.array([
    (0, 175),    # head
    (0, 165),    # neck
    (-10, 155),  # left shoulder
    (10, 155),   # right shoulder
    (-15, 140),  # left elbow
    (15, 140),   # right elbow
    (-10, 120),  # left wrist
    (10, 120),   # right wrist
    (0, 100),    # waist
    (-5, 90),    # left hip
    (5, 90),     # right hip
    (-5, 50),    # left knee
    (5, 50),     # right knee
    (-5, 10),    # left ankle
    (5, 10)      # right ankle
])

# Define the positions of the 15 points at t=1 (lying down position)
P1 = np.array([
    (180, 0),    # head
    (170, 0),    # neck
    (160, 5),    # left shoulder
    (160, -5),   # right shoulder
    (150, 10),   # left elbow
    (150, -10),  # right elbow
    (140, 15),   # left wrist
    (140, -15),  # right wrist
    (90, 0),     # waist
    (80, 5),     # left hip
    (80, -5),    # right hip
    (50, 5),     # left knee
    (50, -5),    # right knee
    (20, 5),     # left ankle
    (20, -5)     # right ankle
])

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-50, 200)
ax.set_ylim(-20, 190)
ax.set_aspect('equal')
ax.axis('off')  # Hide axes

# Plot the points
points, = ax.plot([], [], 'o', color='white', markersize=8)

# Update function for animation
def update(t):
    P = (1 - t) * P0 + t * P1
    points.set_data(P[:, 0], P[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 1, 100), interval=50, blit=True)

# Show the animation
plt.show()
