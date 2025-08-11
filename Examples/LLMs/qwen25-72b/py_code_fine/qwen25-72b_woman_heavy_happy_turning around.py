
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
plt.axis('off')

# Define the points representing the woman's body parts
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
    [1.5, 2],  # Right elbow
    [-1.5, 2],  # Left elbow
    [2.5, 3],  # Right wrist
    [-2.5, 3],  # Left wrist
    [0, 2],  # Head
    [0, -2]  # Pelvis
]

# Convert points to a NumPy array
points = np.array(points)

# Create scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Function to update the positions of the points
def update(frame):
    global points
    angle = frame * np.pi / 180  # Convert frame number to angle in radians
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    # Apply rotation to each point
    rotated_points = np.dot(points, rotation_matrix)
    
    # Update the scatter plot
    scat.set_offsets(rotated_points)
    
    # Add some random noise to simulate the heaviness and natural movement
    noise = np.random.normal(0, 0.1, rotated_points.shape)
    scat.set_offsets(rotated_points + noise)
    
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 5), interval=50, blit=True)

# Show the animation
plt.show()
