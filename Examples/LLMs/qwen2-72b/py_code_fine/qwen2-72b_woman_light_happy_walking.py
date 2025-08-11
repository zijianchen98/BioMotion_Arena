
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the positions of the 15 point-lights for a walking motion
# These positions are approximations based on a simplified model of a walking woman
light_positions = np.array([
    [0.1, 0.8], [0.2, 0.7], [0.3, 0.6], [0.4, 0.5], [0.5, 0.4],
    [0.6, 0.3], [0.7, 0.2], [0.8, 0.1], [0.9, 0.0], [0.1, 0.6],
    [0.2, 0.5], [0.3, 0.4], [0.4, 0.3], [0.5, 0.2], [0.6, 0.1]
])

# Function to update the frame of the animation
def update(frame):
    # Clear the current plot
    plt.cla()
    
    # Update the positions of the lights based on the frame number
    updated_positions = light_positions + np.sin(frame / 10.0) * 0.1
    
    # Scatter plot the updated positions of the point-lights
    plt.scatter(updated_positions[:, 0], updated_positions[:, 1], color='white')
    
    # Set the plot limits and background color
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.axis('off')
    plt.gca().set_facecolor('black')

# Create the figure and axis for the animation
fig, ax = plt.subplots(figsize=(5, 5))

# Create the animation using FuncAnimation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

# Show the animation
plt.show()
