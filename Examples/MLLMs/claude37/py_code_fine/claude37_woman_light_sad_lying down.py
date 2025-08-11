
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points (lights)
num_points = 15

# Define the initial positions of the points representing the body
# These positions should resemble a lying down figure
initial_positions = np.array([
    [0, 5],     # Head
    [-1, 4],    # Left Shoulder
    [1, 4],     # Right Shoulder
    [-1, 3],    # Left Elbow
    [1, 3],     # Right Elbow
    [-1.5, 2],  # Left Hand
    [1.5, 2],   # Right Hand
    [0, 2],     # Chest
    [-1, 1],    # Left Hip
    [1, 1],     # Right Hip
    [0, 0],     # Pelvis
    [-1, -1],   # Left Knee
    [1, -1],    # Right Knee
    [-1, -2],   # Left Ankle
    [1, -2],    # Right Ankle
])

# Function to create animation
def animate(frame):
    plt.clf()
    plt.xlim(-3, 3)
    plt.ylim(-3, 6)
    plt.gca().set_facecolor('black')

    # Update vertical positions for realistic 'lying down' effect
    y_offset = np.sin(np.radians(frame)) * 0.1  # Small vertical bobbing effect
    current_positions = initial_positions + np.array([[0, y_offset]] * num_points)
    
    plt.scatter(current_positions[:, 0], current_positions[:, 1], color='white', s=100)

# Set up the figure
fig = plt.figure()
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 360, 2), interval=50)

# Show the animation
plt.show()
