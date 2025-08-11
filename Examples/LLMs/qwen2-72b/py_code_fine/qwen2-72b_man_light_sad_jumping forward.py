
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial position and velocity of the points
positions = np.random.uniform(-10, 10, (15, 2))
velocities = np.random.normal(0, 0.1, (15, 2))

# Define the figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
ax.set_facecolor('black')

# Define the function to update the animation frame
def update(frame):
    global positions, velocities
    
    # Update the positions of the points
    positions += velocities
    
    # Keep the points within the bounds of the screen
    positions[positions > 15] -= 30
    positions[positions < -15] += 30
    
    # Clear the previous frame
    ax.clear()
    
    # Plot the points on the axis
    ax.scatter(positions[:, 0], positions[:, 1], color='white')
    
    # Set the axis limits and background color
    ax.set_xlim([-20, 20])
    ax.set_ylim([-20, 20])
    ax.set_facecolor('black')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

# Show the animation
plt.show()
