
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
ax.axis('off')

# Define the points representing the woman lying down
points = [
    [0, 0],  # Head
    [1, 1],  # Right shoulder
    [1, -1],  # Left shoulder
    [2, 2],  # Right elbow
    [2, -2],  # Left elbow
    [3, 3],  # Right hand
    [3, -3],  # Left hand
    [1, -4],  # Right hip
    [1, -6],  # Right knee
    [1, -8],  # Right foot
    [-1, -4],  # Left hip
    [-1, -6],  # Left knee
    [-1, -8],  # Left foot
    [-2, -2],  # Stomach
    [-3, -3]  # Pelvis
]

# Convert points to a numpy array
points = np.array(points)

# Create scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Function to update the position of the points
def update(frame):
    # Apply a small random perturbation to simulate breathing
    perturbation = 0.1 * np.sin(2 * np.pi * frame / 30)
    new_points = points + np.random.normal(0, perturbation, points.shape)
    
    # Update the scatter plot
    scat.set_offsets(new_points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(300), interval=50, blit=True)

# Show the animation
plt.show()
