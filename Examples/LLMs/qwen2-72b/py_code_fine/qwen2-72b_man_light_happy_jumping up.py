
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters for the animation
num_points = 15
fps = 30
duration = 3 # seconds
frames = fps * duration

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

# Generate random starting positions for the points
positions = np.random.rand(num_points, 2) * 10

# Function to update the positions of the points
def update(frame):
    global positions
    
    # Calculate the new positions of the points
    # Here we simulate a jumping motion by adding sinusoidal movement in y-direction
    # and some random noise to simulate natural movement
    positions[:, 1] += 0.5 * np.sin(frame / (fps/2)) + np.random.normal(0, 0.1, num_points)
    
    # Keep the x-position constant but add some noise
    positions[:, 0] += np.random.normal(0, 0.1, num_points)
    
    # Clear the previous frame
    ax.clear()
    ax.set_facecolor('black')
    
    # Plot the points
    ax.scatter(positions[:, 0], positions[:, 1], color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps)

# Show the animation
plt.show()
