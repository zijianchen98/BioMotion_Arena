
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions and velocities of the 15 point-lights
num_lights = 15
positions = np.random.uniform(-1, 1, size=(num_lights, 2))
velocities = np.random.normal(0, 0.01, size=(num_lights, 2))

# Define the figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_facecolor('black')

# Define the function that updates the position of the point-lights for each frame
def update(frame):
    global positions, velocities
    
    # Update the positions of the point-lights based on their velocities
    positions += velocities
    
    # Keep the point-lights within the boundaries of the animation window
    positions = np.clip(positions, -1.9, 1.9)
    
    # Bounce back from the walls
    mask_x = ((positions[:, 0] <= -1.9) | (positions[:, 0] >= 1.9))
    mask_y = ((positions[:, 1] <= -1.9) | (positions[:, 1] >= 1.9))
    velocities[mask_x, 0] *= -1
    velocities[mask_y, 1] *= -1
    
    # Clear the previous frame
    ax.clear()
    
    # Plot the point-lights on the current frame
    ax.scatter(positions[:, 0], positions[:, 1], color='white', s=10)

# Create the animation using the update function
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

# Show the animation
plt.show()
