
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and the duration of the animation
num_points = 15
duration = 10 # seconds

# Define the total number of frames in the animation
num_frames = int(duration * 30)  # 30 frames per second

# Define the initial positions of the points
initial_positions = np.random.rand(num_points, 2)

# Define the function to update the positions of the points
def update(frame):
    global initial_positions
    
    # Calculate the time elapsed
    t = frame / num_frames
    
    # Define the motion parameters
    amplitude = 0.5
    frequency = 1.5
    phase = 0.0
    
    # Update the positions based on the sine wave motion
    positions = initial_positions + amplitude * np.sin(2 * np.pi * frequency * t + phase)
    
    # Ensure the positions stay within the bounds (0 to 1)
    positions[:, 0] = np.clip(positions[:,  t],  0, 1)
    positions[:, 1] = np.clip(positions[:, 1],  0, 1)
    
    # Clear the current plot
    ax.clear()
    
    # Plot the point lights
    ax.scatter(positions[:,  t], positions[:, 1], color='white')
    
    # Set the limits for the plot
    ax.set_xlim([  , 1])
    ax.set_ylim([  , 1])
    ax.set_aspect('equal')
    ax.axis('off')

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 4))

# Set the background color to black
ax.set_facecolor('black')

# Create the animation
animation = FuncAnimation(fig, update, frames=num_frames, interval=33, repeat=False)

# Show the animation
plt.show()
