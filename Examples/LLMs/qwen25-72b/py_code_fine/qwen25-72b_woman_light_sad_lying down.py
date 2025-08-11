
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points for the woman lying down
# These points are simplified and may need to be adjusted for realism
points = np.array([
    [0.4, 0.9],  # Head
    [0.45, 0.8],  # Neck
    [0.5, 0.7],  # Shoulder right
    [0.6, 0.6],  # Elbow right
    [0.7, 0.5],  # Wrist right
    [0.4, 0.7],  # Shoulder left
    [0.3, 0.6],  # Elbow left
    [0.2, 0.5],  # Wrist left
    [0.5, 0.5],  # Hip right
    [0.6, 0.4],  # Knee right
    [0.7, 0.3],  # Ankle right
    [0.4, 0.5],  # Hip left
    [0.3, 0.4],  # Knee left
    [0.2, 0.3],  # Ankle left
    [0.5, 0.2]   # Pelvis
])

# Normalize points to fit in the plot area
points[:, 0] *= 10
points[:, 1] *= 10

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')
ax.axis('off')

# Create the scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Function to update the position of the points
def update(frame):
    global points
    # Apply a small random perturbation to simulate breathing or slight movements
    perturbation = 0.05 * np.random.randn(*points.shape)
    points += perturbation
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Show the animation
plt.show()
