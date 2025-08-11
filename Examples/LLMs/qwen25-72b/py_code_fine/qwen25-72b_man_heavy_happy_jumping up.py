
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
plt.axis('off')

# Define the points representing the happy man
points = [
    [0, 0],  # Center of mass
    [1, 1],  # Right shoulder
    [-1, 1],  # Left shoulder
    [2, -1],  # Right hip
    [-2, -1],  # Left hip
    [3, -3],  # Right knee
    [-3, -3],  # Left knee
    [4, -5],  # Right ankle
    [-4, -5],  # Left ankle
    [0.5, 2],  # Right elbow
    [-0.5, 2],  # Left elbow
    [1.5, 3],  # Right wrist
    [-1.5, 3],  # Left wrist
    [0, -6],  # Right foot
    [0, -6]   # Left foot
]

# Convert points to a numpy array
points = np.array(points)

# Create scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Define the jumping motion
def update(frame):
    # Apply a sine wave to simulate jumping
    y_offset = 5 * np.sin(2 * np.pi * frame / 60)
    points[:, 1] += y_offset - points[:, 1]
    
    # Apply a slight delay to the lower body to simulate weight
    points[3:, 1] += 0.5 * y_offset - points[3:, 1]
    
    # Update the scatter plot
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 60), interval=50, blit=True)

# Display the animation
plt.show()
