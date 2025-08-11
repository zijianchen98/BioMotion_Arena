
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.axis('off')

# Define the number of points and their initial positions
num_points = 15
points = np.array([
    [0, 0.8],  # Head
    [-0.3, 0.6], [0.3, 0.6],  # Shoulders
    [-0.5, 0.4], [0.5, 0.4],  # Elbows
    [-0.5, 0.2], [0.5, 0.2],  # Hands
    [-0.3, -0.2], [0.3, -0.2],  # Hips
    [0, -0.6],  # Feet
])

# Create scatter plot
sc = ax.scatter(points[:, 0], points[:, 1], color='white')

# Define the bowing action positions over time
def bowing_motion(frame):
    t = frame / 20  # Normalize frame to time
    # Update y-coordinates for each point to simulate bowing
    updated_y = np.array([
        0.8 - t * 0.3,      # Head towards ground
        0.6 - t * 0.3,      # Shoulders towards ground
        0.6 - t * 0.3,
        0.4 - t * 0.2,      # Elbows towards ground
        0.4 - t * 0.2,
        0.2 - t * 0.1,      # Hands towards ground
        0.2 - t * 0.1,
        -0.2 + t * 0.1,     # Hips rise slightly
        -0.6 + t * 0.3      # Feet lift slightly
    ])
    points[:, 1] = updated_y
    sc.set_offsets(points)
    return sc,

# Create animation
ani = animation.FuncAnimation(fig, bowing_motion, frames=np.arange(0, 100), interval=50)

# Show the animation
plt.show()
