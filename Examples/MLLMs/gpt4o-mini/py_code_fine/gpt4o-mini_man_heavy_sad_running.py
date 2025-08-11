
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the number of lights
num_lights = 15

# Establish coordinates for point lights to resemble a running sadman
# Base positions
base_positions = np.array([
    [0, 5],   # Head
    [-1, 4], [0, 4], [1, 4],  # Shoulders
    [-1, 3], [0, 3], [1, 3],  # Torso
    [-2, 2], [-1, 2], [0, 2], [1, 2], [2, 2],  # Arms
    [-1, 1], [0, 1], [1, 1],  # Upper legs
    [-1, 0], [0, 0], [1, 0]   # Lower legs
])

# Create an animation function
def update(frame):
    plt.clf()
    plt.xlim(-5, 5)
    plt.ylim(-1, 6)
    plt.gca().set_facecolor('black')
    plt.axis('off')

    # Update positions for running
    running_motion = 0.1 * frame  # Forward motion to simulate running
    # Adjust y-coordinates to simulate sadder posture
    sad_posture = np.array([0, -0.1 * np.sin(2 * np.pi * (frame / 30))])

    # Apply transformations for animation
    positions = base_positions + sad_posture + np.array([running_motion, 0])
    plt.scatter(positions[:, 0], positions[:, 1], color='white', s=100)    

# Create a figure
fig = plt.figure()

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

# Show the animation
plt.show()
