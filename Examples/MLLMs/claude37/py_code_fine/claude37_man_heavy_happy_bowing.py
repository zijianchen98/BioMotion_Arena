
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the number of point-lights
num_points = 15

# Define the positions of the point-lights
# This is a simplified representation of a "happyman" bowing action
initial_positions = np.array([
    [0, 2], [1, 4], [-1, 4],  # Head
    [0, 1], [1, 3], [-1, 3],  # Upper body
    [0, 0], [0.5, 2], [-0.5, 2],  # Hands
    [0, -1], [0.3, -1.5], [-0.3, -1.5],  # Legs
    [0, -2], [0.25, -2.5], [-0.25, -2.5]  # Feet
])

# Update function for the animation
def update(frame):
    plt.clf()  # Clear the previous frame
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.axis('off')  # Remove axes

    # Adjust the positions to simulate the bowing motion
    # The "bowing" is represented by a change in the y-coordinate
    bow_angle = frame / 10.0  # Adjust the bowing angle
    bow_offset = np.array([0, -2 * np.sin(bow_angle)])  # Bowing effect
    current_positions = initial_positions + bow_offset

    # Plot point-lights
    plt.scatter(current_positions[:, 0], current_positions[:, 1], color='white')

# Create a figure for the animation
fig = plt.figure(facecolor='black')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

# Show the animation
plt.show()
