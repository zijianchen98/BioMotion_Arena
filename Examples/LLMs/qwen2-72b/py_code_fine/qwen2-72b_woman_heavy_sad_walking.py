
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions and velocities of the point-lights
positions = np.random.uniform(low=0, high=1, size=(15, 2))
velocities = np.random.normal(loc=0, scale=0.01, size=(15, 2))

# Define the function to update the positions of the point-lights at each frame
def update_positions(frame):
    global positions
    # Update the positions based on the velocities
    positions += velocities
    # Ensure the point-lights stay within the boundaries of the plot
    positions %= 1
    # Clear the previous plot
    plt.cla()
    # Plot the point-lights
    plt.scatter(positions[:, 0], positions[:, 1], color='white')
    # Set the plot limits to ensure a consistent view
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    # Set the background color to black
    ax = plt.gca()
    ax.set_facecolor('black')

# Create the figure and axis for the animation
fig, ax = plt.subplots()

# Create the animation using FuncAnimation
ani = animation.FuncAnimation(fig, update_positions, frames=num_frames, interval=50)

# Show the animation
plt.show()
