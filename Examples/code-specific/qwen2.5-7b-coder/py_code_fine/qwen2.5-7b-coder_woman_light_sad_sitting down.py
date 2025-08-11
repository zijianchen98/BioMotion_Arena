
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters for the animation
num_points = 15
frames = 60
frame_interval = 50  # milliseconds

# Define the initial positions of the points
initial_positions = np.random.rand(num_points, 2)

# Define the velocity vectors for each point
velocities = np.random.randn(num_points, 2)
velocities /= np.linalg.norm(velocities, axis=1, keepdims=True)

# Define the acceleration vectors for each point
accelerations = np.zeros((num_points, 2))

# Define the gravity vector
gravity = np.array([0, -0.05])

# Define the damping factor
damping = 0.98

# Define the function to update the positions of the points
def update(frame):
    global initial_positions, velocities, accelerations
    
    # Update the accelerations due to gravity
    accelerations += gravity
    
    # Update the velocities based on the accelerations
    velocities *= damping
    velocities += accelerations
    
    # Update the positions based on the velocities
    initial_positions += velocities
    
    # Reset the positions if they go out of bounds
    initial_positions[:, 0] = np.clip(initial_positions[:, 0], 0, 1)
    initial_positions[:, 1] = np.clip(initial_positions[:, 1], 0, 1)
    
    # Clear the current plot
    ax.clear()
    
    # Set the limits of the axes
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Plot the points
    ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')
    
    return ax,

# Create the figure and axis objects
fig, ax = plt.subplots()

# Create the animation object
ani = animation.FuncAnimation(fig, update, frames=frames, interval=frame_interval, blit=False)

# Show the animation
plt.show()
