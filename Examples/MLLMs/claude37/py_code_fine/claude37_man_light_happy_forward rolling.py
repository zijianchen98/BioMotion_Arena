
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants for figure size
WIDTH, HEIGHT = 6, 6

# Define the number of point-lights (joints) and their initial positions
NUM_POINTS = 15
points = np.zeros((NUM_POINTS, 2))

# Initialize the position for (x, y) of each point-light (representing the joints)
# You can modify these to represent your character's joints in a more realistic way
init_positions = [
    [0, 4], [1, 5], [-1, 5],  # Head
    [-1, 3], [1, 3], [0, 2],  # Shoulders
    [-1, 1], [1, 1],          # Elbows
    [0, 0],                   # Waist
    [-1, -1], [1, -1],       # Knees
    [-1, -3], [1, -3],       # Feet
]

# Set initial positions
for i in range(NUM_POINTS):
    points[i] = init_positions[i]

# Create figure and set limits
fig, ax = plt.subplots(figsize=(WIDTH, HEIGHT))
ax.set_xlim(-3, 3)
ax.set_ylim(-4, 6)
ax.set_facecolor('black')
ax.axis('off')

# Create scatter plot for point-lights
scatter = ax.scatter(points[:, 0], points[:, 1], color='white', s=100)

def update(frame):
    global points
    # Define forward roll motion through rotation and translation
    theta = np.radians(frame)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], 
                                 [np.sin(theta), np.cos(theta)]])
    
    translation = np.array([0, -0.1])  # Move down to simulate forward roll
    points = np.dot(rotation_matrix, points.T).T + translation

    # Apply limits to keep the animation within the view
    if points[-1, 1] < -4:
        points = np.array(init_positions)  # Reset positions after roll

    scatter.set_offsets(points)
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=360, interval=20, blit=True)

# Show the animation
plt.show()
