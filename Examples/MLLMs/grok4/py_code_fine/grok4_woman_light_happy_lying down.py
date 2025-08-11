
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_POINTS = 15
FPS = 30
DURATION = 3  # seconds

# Point-light positions in a lying down position (x, y)
# These points can be adjusted to resemble the anatomy better
initial_positions = np.array([
    [0, 1.5],  # Head
    [-0.5, 1.0], [0.5, 1.0],  # Shoulders
    [-0.8, 0.5], [0.8, 0.5],  # Elbows
    [-0.5, 0], [0.5, 0],  # Hands
    [-0.5, -0.5], [0.5, -0.5],  # Hips
    [-0.8, -1.0], [0.8, -1.0],  # Knees
    [-0.4, -1.5], [0.4, -1.5],  # Feet
    [0, 0]  # Center of body
])

# Function to create a lying down motion
def update(frame):
    plt.cla()  # Clear the current axes
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.axis('off')  # Turn off the axis

    # Update the positions for lying down motion (simple vertical oscillation)
    y_offset = np.sin(frame * 0.1) * 0.1  # Modify this for different motion
    positions = initial_positions + np.array([0, y_offset])
    
    # Add points to plot
    plt.scatter(positions[:, 0], positions[:, 1], color='white', s=100)

# Set up the figure
fig = plt.figure(figsize=(4, 4), facecolor='black')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=FPS * DURATION, interval=1000 / FPS)

# Show the animation
plt.show()
