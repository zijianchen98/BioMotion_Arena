
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames for the animation
num_frames = 100

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0.0, 2.0],  # Head
    [-0.3, 1.5], [0.3, 1.5], # Shoulders
    [-0.6, 1.0], [0.6, 1.0], # Elbows
    [-0.9, 0.5], [0.9, 0.5], # Hands
    [-0.3, 0.0], [0.3, 0.0], # Hips
    [-0.3, -0.5], [0.3, -0.5], # Knees
    [-0.3, -1.0], [0.3, -1.0], # Ankles
    [-0.1, -1.5], [0.1, -1.5]   # Feet
])

# Define the animation function
def animate(i):
    # Clear the previous frame
    plt.cla()
    
    # Define the new positions of the point-lights based on the frame number
    positions = initial_positions.copy()
    
    # Simulate waving motion in the right arm
    angle = np.sin(i / 10) * 0.5
    positions[5, 0] = 0.9 + np.cos(angle) * 0.3
    positions[5, 1] = 0.5 + np.sin(angle) * 0.3

    # Simulate waving motion in the left arm
    angle = np.cos(i / 10) * 0.5
    positions[4, 0] = -0.6 + np.cos(angle) * 0.3
    positions[4, 1] = 1.0 + np.sin(angle) * 0.3

    # Simulate walking
    positions[[11,13],1] -= np.sin(i/5)*0.1
    positions[[12,14],1] += np.sin(i/5)*0.1

    # Plot the point-lights
    plt.plot(positions[:, 0], positions[:, 1], 'wo', markersize=8)
    
    # Set the limits of the plot
    plt.xlim(-1.5, 1.5)
    plt.ylim(-2, 2.5)
    
    # Set the background color to black
    plt.gca().set_facecolor('black')
    
    # Remove the axis labels
    plt.xticks([])
    plt.yticks([])
    
    # Return the plot
    return plt

# Create the animation
fig = plt.figure(facecolor='black')
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=False)

# Save the animation as a gif
ani.save('waving_sadman.gif', writer='pillow', fps=10)

# Show the animation
plt.show()
