
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points
num_points = 15

# Define the initial positions of the point lights (x, y coordinates)
# Creating a rough silhouette for a sad man bowing
points_initial = np.array([
    [0, 1],    # Head
    [-0.5, 0.5], [0.5, 0.5],  # Shoulders
    [-0.4, 0.3], [0.4, 0.3],  # Elbows
    [-0.2, 0.1], [0.2, 0.1],  # Hands
    [0, -0.5],  # Body
    [-0.3, -0.7], [0.3, -0.7],  # Legs
    [-0.4, -1], [0.4, -1],  # Feet
    [-0.1, -0.1], [0.1, -0.1],  # Additional points for better effect
    [0, 0.5],   # Center point above head for effect
])

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')

# Create a scatter plot
scat = ax.scatter(points_initial[:, 0], points_initial[:, 1], color='white')

# Function to update the frame
def update(frame):
    # Calculate the angle of the bend
    angle = np.radians(frame)
    
    # Define a transformation for bowing motion
    # Scaling down y coordinates for a bowing effect
    points = points_initial.copy()
    points[:, 1] = points_initial[:, 1] * (1 - (frame / 90))  # Bend down with frame

    # Update scatter plot
    scat.set_offsets(points)
    return scat,

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=90, interval=50, blit=True)

# Show the animation
plt.show()
