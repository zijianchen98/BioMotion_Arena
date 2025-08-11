
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(0, 150)
ax.set_ylim(0, 200)

# Coordinates for running motion points
points = [
    [5, 10],  # Head
    [2, 20],  [8, 20],  # Shoulders
    [0, 30],  [10, 30],  # Elbows
    [-2, 40], [12, 40],  # Hands
    [1, 50],  [9, 50],  # Hips
    [0, 60],  [10, 60],  # Knees
    [0, 70],  [10, 70],  # Ankles
]

# Convert points to numpy array for animation
import numpy as np
points = np.array(points)

# Scatter plot for the white dots
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Animation update function to move points
def update(frame):
    # Simulate running motion by shifting x-coordinates
    points[:, 0] += 1
    # Wrap around the x-coordinate to create cyclic running motion
    points[:, 0] %= 150
    scat.set_offsets(points)
    return scat,

# Create the animation
anim = animation.FuncAnimation(fig, update, frames=300, interval=50, blit=True)

# Show the plot
plt.axis('off')
plt.show()
