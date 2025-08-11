
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set parameters
n_points = 15
duration = 20  # total seconds of the animation
fps = 30  # frames per second
frames = duration * fps

# Define the initial positions of the point lights representing a sad woman
# These positions will change throughout the animation to represent a jump
initial_positions = np.array([
    [0, 4],  # Head
    [-1, 3], [1, 3],  # Shoulders
    [-1, 2], [0, 2.5], [1, 2],  # Arms
    [-0.5, 1], [0, 0], [0.5, 1],  # Torso and hips
    [-1, 0], [0, -1], [1, 0],  # Legs in initial position
    [-0.5, -2], [0, -2.5], [0.5, -2]  # Feet
])

# Create an animation function
def update(frame):
    plt.clf()  # Clear the plot
    plt.xlim(-2, 2)
    plt.ylim(-3, 5)
    plt.gca().set_facecolor('black')
    plt.gca().set_xticks([])  # Hide x ticks
    plt.gca().set_yticks([])  # Hide y ticks

    # Define jump motion parameters
    height_jump = 3
    jump_duration = frames // 2
    phase = frame % jump_duration
    # Smooth jump, using a sine function for realism
    jump_height = height_jump * np.sin(np.pi * phase / jump_duration)

    # Apply positions and add jump height
    y_positions = initial_positions[:, 1] + jump_height

    # Plot point lights
    plt.scatter(initial_positions[:, 0], y_positions, c='white', s=100)

# Set up the animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000 / fps)

# Show the animation
plt.show()
