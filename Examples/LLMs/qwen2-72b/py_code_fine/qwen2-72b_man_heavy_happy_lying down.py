
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and points
num_frames = 100
num_points = 15

# Define the initial positions and velocities of the points
positions = np.random.rand(num_points, 2) * 100
velocities = np.random.normal(0, 1, (num_points, 2))

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim([0, 100])
ax.set_ylim([0, 100])
ax.set_facecolor('black')

# Define the function to update the animation
def update(frame):
    global positions, velocities
    
    # Update the positions based on the velocities
    positions += velocities
    
    # Keep the points within the screen boundaries
    positions[positions > 100] -= 100
    positions[positions < 0] += 100
    
    # Clear the previous frame
    ax.clear()
    
    # Plot the points
    ax.scatter(positions[:, 0], positions[:, 1], color='white', s=50)
    
    # Set the title
    ax.set_title("Happy man with heavy weight lying down")

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

# Show the animation
plt.show()
