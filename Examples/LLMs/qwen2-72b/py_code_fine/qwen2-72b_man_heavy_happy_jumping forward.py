
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the point-lights
# For simplicity, we'll just have them move horizontally and vertically
positions = np.zeros((15, 2))
positions[:, 0] = np.linspace(0, 1, 15)  # x-coordinates
positions[:, 1] = np.random.uniform(0, 1, 15)  # y-coordinates

# Create a figure and axis for plotting
fig, ax = plt.subplots()
ax.set_xlim([0, 2])
ax.set_ylim([0, 1])
ax.set_facecolor('black')  # Set the background color to black

# Function to update the frame
def update(frame):
    ax.clear()
    ax.set_facecolor('black')
    
    # Update the positions of the point-lights based on the frame number
    positions[:, 0] += 0.01 * (frame % 100) / 100  # Horizontal movement
    positions[:, 1] += 0.01 * np.sin(frame / 10)  # Vertical oscillation
    
    # Plot the point-lights
    ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

# Show the animation
plt.show()
