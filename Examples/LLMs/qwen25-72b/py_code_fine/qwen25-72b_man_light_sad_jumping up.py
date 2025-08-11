
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(0, 20)
ax.axis('off')

# Define the initial positions of the points
points = [
    [0, 0],  # Center of mass
    [-2, 1], [2, 1],  # Shoulders
    [-1, 2], [1, 2],  # Elbows
    [-0.5, 3], [0.5, 3],  # Wrists
    [-1, -1], [1, -1],  # Hips
    [-2, -2], [2, -2],  # Knees
    [-3, -3], [3, -3],  # Ankles
    [-4, -4], [4, -4]  # Feet
]

# Convert points to a NumPy array
points = np.array(points)

# Create the scatter plot
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Define the jumping motion
def update(frame):
    t = frame / 10.0  # Time parameter
    amplitude = 2.0  # Jump height
    frequency = 1.0  # Frequency of the jump

    # Update the y-coordinates of the points
    points[:, 1] = points[:, 1] + amplitude * np.sin(frequency * t)

    # Update the scatter plot
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(300), interval=20, blit=True)

# Show the animation
plt.show()
