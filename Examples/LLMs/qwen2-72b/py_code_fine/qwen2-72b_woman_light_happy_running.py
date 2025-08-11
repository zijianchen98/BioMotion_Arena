
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0.1, 0.9],  # head
    [0.15, 0.8],  # neck
    [0.1, 0.7],  # torso
    [0.05, 0.6],  # left shoulder
    [0.05, 0.5],  # left elbow
    [0.05, 0.4],  # left wrist
    [0.15, 0.6],  # right shoulder
    [0.15, 0.5],  # right elbow
    [0.15, 0.4],  # right wrist
    [0.05, 0.3],  # left hip
    [0.05, 0.2],  # left knee
    [0.05, 0.1],  # left ankle
    [0.15, 0.3],  # right hip
    [0.15, 0.2],  # right knee
    [0.15, 0.1]   # right ankle
])

# Define the animation function
def animate(i):
    # Clear the previous frame
    ax.clear()
    
    # Set the background color to black
    ax.set_facecolor('black')
    
    # Set the limits of the plot
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    
    # Remove the axis labels
    ax.axis('off')
    
    # Calculate the new positions of the point-lights
    new_positions = initial_positions + np.random.normal(0, 0.01, size=(15, 2))
    
    # Plot the point-lights
    ax.scatter(new_positions[:, 0], new_positions[:, 1], color='white', s=10)

# Create the figure and the axes
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50)

# Show the animation
plt.show()
