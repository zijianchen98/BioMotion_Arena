
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuration
num_points = 15
frames = 100
weight = 5

# Initial positions of point-lights
initial_positions = np.array([
    [0, 1.5],  # Head
    [0, 1],    # Shoulders
    [-0.5, 1], # Left Shoulder
    [0.5, 1],  # Right Shoulder
    [0, 0.5],  # Waist
    [-0.5, 0], # Left Hip
    [0.5, 0],  # Right Hip
    [-0.3, -0.5], # Left Knee
    [0.3, -0.5],  # Right Knee
    [-0.3, -1],   # Left Ankle
    [0.3, -1],    # Right Ankle
    [0, 0.5 - weight/10],  # Holding weight (lowered)
    [-0.5, 0.2 - weight/10], # Left Finger
    [0.5, 0.2 - weight/10],  # Right Finger
    [0, 0.2 - weight/10],  # Center of mass
    [0, 0]  # Ground support
])

# Function to update positions
def update(frame):
    plt.cla()  # Clear previous frame
    plt.xlim(-2, 2)  # Set x-axis limits
    plt.ylim(-2, 2)  # Set y-axis limits
    plt.gca().set_facecolor('black')

    # Update positions for jumping motion
    y_offset = np.sin(frame / 10.0) * 0.5  # Jumping up and down
    x_offset = frame / frames * 2   # Moving forward on x-axis

    positions = initial_positions + np.array([x_offset, y_offset])

    # Plot each point-light
    plt.scatter(positions[:, 0], positions[:, 1], color='white', s=100)

# Create animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50)
plt.show()
