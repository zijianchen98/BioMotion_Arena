
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions and velocities of the points
positions = np.array([[0, 0], [0, 0.5], [0, 1], [0.5, 0], [0.5, 1], [1, 0], [1, 0.5], [1, 1],
                      [0.25, 0.25], [0.25, 0.75], [0.75, 0.25], [0.75, 0.75],
                      [0.125, 0.125], [0.125, 0.875], [0.875, 0.125]])
velocities = np.random.uniform(-0.01, 0.01, size=(15, 2))

# Define the update function for the animation
def update(frame):
    global positions, velocities
    # Update the positions based on the velocities
    positions += velocities
    # Keep the points within the bounds of the plot
    positions %= 1
    # Clear the previous frame
    plt.cla()
    # Plot the points
    plt.scatter(positions[:, 0], positions[:, 1], color='white')
    # Set the plot limits and background color
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.axis('off')
    plt.gca().set_facecolor('black')

# Create the figure and axis for the plot
fig, ax = plt.subplots(figsize=(6, 6))
# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

# Show the animation
plt.show()
