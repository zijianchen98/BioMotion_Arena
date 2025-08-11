
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames for the animation
num_frames = 100

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0.0, 2.0],  # Head
    [-0.3, 1.5], [0.3, 1.5],  # Shoulders
    [-0.6, 1.0], [0.6, 1.0],  # Elbows
    [-0.9, 0.5], [0.9, 0.5],  # Wrists
    [-0.3, 0.0], [0.3, 0.0],  # Hips
    [-0.5, -0.5], [0.5, -0.5],  # Knees
    [-0.7, -1.0], [0.7, -1.0],  # Ankles
    [-0.9, -1.5], [0.9, -1.5]   # Feet
])

# Define the animation function that updates the positions of the point-lights
def animate(i):
    # Clear the previous frame
    plt.cla()
    
    # Define the bowing motion parameters
    bow_angle = np.sin(i / 20) * 0.5  # Bow angle changes over time
    head_bend = np.sin(i / 10) * 0.2   # Head bend changes over time
    
    # Update the positions of the point-lights based on the bowing motion
    positions = initial_positions.copy()
    positions[:, 1] -= positions[:, 1] * bow_angle  # Bowing down
    positions[0, 1] -= head_bend  # Head bending forward
    
    # Plot the point-lights
    plt.plot(positions[:, 0], positions[:, 1], 'wo')
    
    # Set the plot limits
    plt.xlim(-1.5, 1.5)
    plt.ylim(-2.0, 2.5)
    
    # Set the background color to black
    plt.gca().set_facecolor('black')
    
    # Remove axes
    plt.axis('off')

# Create the animation
fig = plt.figure(facecolor='black')
ani = animation.FuncAnimation(fig, animate, frames=num_frames, repeat=True)

# Show the animation
plt.show()
