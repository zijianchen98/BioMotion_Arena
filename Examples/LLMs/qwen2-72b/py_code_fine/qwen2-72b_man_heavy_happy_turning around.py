
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0.2, 0.8],  # head
    [0.15, 0.7], [0.25, 0.7],  # shoulders
    [0.1, 0.6], [0.3, 0.6],  # elbows
    [0.05, 0.5], [0.35, 0.5],  # wrists
    [0.2, 0.4],  # torso
    [0.15, 0.3], [0.25, 0.3],  # knees
    [0.1, 0.2], [0.3, 0.2],  # ankles
])

# Define the animation function
def animate(i):
    # Clear the plot
    ax.clear()
    
    # Set the background color to black
    ax.set_facecolor('black')
    
    # Set the limits of the plot
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    
    # Calculate the angle of rotation for this frame
    angle = i * 2 * np.pi / num_frames
    
    # Rotate the point-lights around the center of the plot
    rotated_positions = np.dot(initial_positions - [0.5, 0.5], 
                                np.array([[np.cos(angle), -np.sin(angle)], 
                                          [np.sin(angle), np.cos(angle)]])) + [0.5, 0.5]
    
    # Plot the point-lights
    ax.scatter(rotated_positions[:, 0], rotated_positions[:, 1], color='white')

# Create the figure and axes objects
fig, ax = plt.subplots()

# Create the animation object
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50)

# Show the animation
plt.show()
