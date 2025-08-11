
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points representing the happy man with heavy weight turning around
points = [
    # Head
    [0, 10],
    # Shoulders
    [-4, 8], [4, 8],
    # Elbows
    [-6, 6], [6, 6],
    # Hands
    [-8, 4], [8, 4],
    # Hips
    [-3, 4], [3, 4],
    # Knees
    [-5, 2], [5, 2],
    # Feet
    [-7, 0], [7, 0],
    # Center of mass (due to heavy weight)
    [0, 2],
    # Additional points for realism
    [-2, 6], [2, 6], [-4, 2], [4, 2]
]

# Convert points to numpy array
points = np.array(points)

# Function to update the frame
def update(frame):
    global points
    angle = np.radians(frame * 2)  # Turning around
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    rotated_points = np.dot(points, rotation_matrix)
    sc.set_offsets(rotated_points)
    return sc,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
sc = ax.scatter(points[:, 0], points[:, 1], s=50, color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 5), interval=50, blit=True)

# Show the animation
plt.show()
