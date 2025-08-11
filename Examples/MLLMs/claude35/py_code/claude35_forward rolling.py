
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Setting up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')  # Solid black background

# Creating the points for the point-light display
num_points = 15
points = np.zeros((num_points, 2))

# Initial positions
# Define a basic configuration for a human subject (simplified)
# Each point corresponds to a body part
initial_positions = np.array([
    [0, 1],  # Head
    [-0.5, 0.5],  # Left Shoulder
    [0.5, 0.5],  # Right Shoulder
    [-0.5, 0],  # Left Elbow
    [0.5, 0],  # Right Elbow
    [-0.5, -0.5],  # Left Hand
    [0.5, -0.5],  # Right Hand
    [-0.5, -1],  # Left Hip
    [0.5, -1],  # Right Hip
    [0, -1.5],  # Body Center
    [0, -1.6],  # Roll position
    [0, -1.9],  # Roll position
    [0.5, -1.5], # Right Foot
    [-0.5, -1.5], # Left Foot
    [-0.1, -1.0], # Knee position
    [0.1, -1.0]   # Knee position
])

# Set the initial positions of the points
points[:] = initial_positions

# Create a scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

def update(frame):
    # Update points' positions to simulate a forward roll
    t = frame / 50  # Adjust speed here
    roll_offset = np.sin(t * np.pi) * 0.5  # Simulated rolling motion
    
    # Adjust y positions to create a rolling effect
    points[:, 1] = initial_positions[:, 1] - roll_offset

    # Update scatter plot based on new positions
    scat.set_offsets(points)
    return scat,

# Creating the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Display the animation
plt.show()
