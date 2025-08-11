
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')
plt.axis('off')  # Hide axes

# Initialize the points for the "happy man"
num_points = 15
# Initial positions of the points (representing a simplified human figure)
points = np.array([
    [5, 7],  # Head
    [4.5, 6], [5.5, 6],  # Shoulders
    [4, 5], [6, 5],       # Elbows
    [4, 4], [6, 4],       # Hips
    [4, 3], [6, 3],       # Knees
    [4, 2], [5, 1], [6, 2],  # Feet
    [3.5, 5.5], [6.5, 5.5], # Hands
    [5, 4], [5, 3.5]      # Center points (adjusted for natural movement)
])

# Create a scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Define the jump motion
def update(frame):
    # Calculate new Y positions for jump animation
    y_offset = np.abs(np.sin(frame / 10.0) * 2)  # Creates a bouncing effect
    new_points = points.copy()
    new_points[:, 1] += y_offset
    scat.set_offsets(new_points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), blit=True, interval=50)

# Show the animation
plt.show()
