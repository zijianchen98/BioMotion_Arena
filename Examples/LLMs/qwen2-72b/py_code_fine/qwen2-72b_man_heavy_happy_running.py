
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0.2, 0.8], [0.25, 0.9], [0.3, 0.8], [0.2, 0.7], [0.25, 0.6],
    [0.3, 0.7], [0.4, 0.6], [0.5, 0.6], [0.6, 0.6], [0.7, 0.6],
    [0.8, 0.6], [0.9, 0.6], [0.4, 0.5], [0.6, 0.5], [0.5, 0.4]
])

# Define the animation function
def animate(i):
    # Clear the plot
    plt.clf()

    # Set the background color to black
    plt.gca().set_facecolor('black')

    # Calculate the new positions of the point-lights based on the running motion
    new_positions = initial_positions + np.array([0.01*i, -0.01*i*np.sin(0.1*i)])

    # Plot the point-lights
    plt.scatter(new_positions[:, 0], new_positions[:, 1], color='white', s=50)

    # Set the axis limits
    plt.xlim(0, 1)
    plt.ylim(0, 1)

    # Remove the axis labels and ticks
    plt.axis('off')

# Create the figure and axes objects
fig, ax = plt.subplots()

# Create the animation object
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50)

# Show the animation
plt.show()
