
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points representing the woman lying down
points = [
    (0.5, 0.9),  # Head
    (0.4, 0.8),  # Left shoulder
    (0.6, 0.8),  # Right shoulder
    (0.3, 0.7),  # Left elbow
    (0.7, 0.7),  # Right elbow
    (0.2, 0.6),  # Left hand
    (0.8, 0.6),  # Right hand
    (0.4, 0.5),  # Left hip
    (0.6, 0.5),  # Right hip
    (0.3, 0.4),  # Left knee
    (0.7, 0.4),  # Right knee
    (0.2, 0.3),  # Left foot
    (0.8, 0.3),  # Right foot
    (0.5, 0.2),  # Lower back
    (0.5, 0.1)   # Pelvis
]

# Convert points to numpy array for easier manipulation
points = np.array(points)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
ax.axis('off')

# Initialize the scatter plot
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Function to update the positions of the points
def update(frame):
    global points
    # Simulate the lying down motion
    if frame < 50:
        # Initial lying down motion
        points[:, 1] -= 0.01
        points[0, 1] += 0.01
    else:
        # Small random movements to simulate breathing
        points += 0.01 * (np.random.rand(*points.shape) - 0.5)
    
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Display the animation
plt.show()
