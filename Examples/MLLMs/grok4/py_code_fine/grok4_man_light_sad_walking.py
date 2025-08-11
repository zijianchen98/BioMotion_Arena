
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')

# Define the number of point lights and their initial configuration
num_points = 15
points = np.zeros((num_points, 2))  # Store (x, y) coordinates of each point

# Define the initial position of the point lights
# The points will be organized to represent a sad man's walking posture
initial_positions = np.array([
    [0, 1],  # Head
    [-1, 0], [1, 0],  # Shoulders
    [-1.5, -1], [1.5, -1],  # Arms
    [-1, -3], [1, -3],  # Hips
    [-1, -4], [1, -4],  # Legs (upper)
    [-1, -5], [1, -5],  # Legs (lower)
    [-2, -4], [2, -4],  # Feet
    [-1.5, -0.5], [1.5, -0.5],  # Hands
    [0, -2]  # Center of body
])

points[:len(initial_positions)] = initial_positions

# Set marker for points
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

def update(frame):
    global points
    # Update point positions to simulate walking
    theta = frame * 0.1  # angle for sine motion
    for i, (x, y) in enumerate(initial_positions):
        new_y = y + np.sin(theta + i)  # simple oscillation for walking motion
        points[i] = [x, new_y]
    
    scat.set_offsets(points)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 60), interval=100)

# Show the animation
plt.show()
