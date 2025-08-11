
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points for the lying down man with heavy weight
# Points are in (x, y) format where (0, 0) is the center of the screen
points = [
    (-0.5, 0.5),  # Head
    (-0.4, 0.4),  # Neck
    (-0.3, 0.3),  # Shoulder left
    (-0.2, 0.3),  # Elbow left
    (-0.1, 0.3),  # Wrist left
    (-0.3, -0.3),  # Hip left
    (-0.2, -0.4),  # Knee left
    (-0.1, -0.5),  # Ankle left
    (0.3, 0.3),  # Shoulder right
    (0.2, 0.3),  # Elbow right
    (0.1, 0.3),  # Wrist right
    (0.3, -0.3),  # Hip right
    (0.2, -0.4),  # Knee right
    (0.1, -0.5),  # Ankle right
    (0, -0.6)  # Center of weight
]

# Function to update the frame
def update(frame):
    global points
    new_points = []
    for point in points:
        # Apply a small random perturbation to simulate breathing or slight movement
        x, y = point
        x += np.random.normal(0, 0.01)
        y += np.random.normal(0, 0.01)
        new_points.append((x, y))
    points = new_points
    scat.set_offsets(points)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
ax.axis('off')

# Create the scatter plot for the points
scat = ax.scatter(*zip(*points), color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

# Show the animation
plt.show()
