
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the points' initial positions
points = np.zeros((num_points, 2))
points[:, 0] = np.linspace(0.1, 0.9, num_points)

# Define the points' initial velocities
velocities = np.zeros((num_points, 2))
velocities[:, 0] = np.linspace(-0.5, 0.5, num_points)

# Define the points' initial accelerations
accelerations = np.zeros((num_points, 2))
accelerations[:, 0] = np.linspace(-0.1, 0.1, num_points)

# Define the time parameters
dt = 0.01
t_max = 10

# Create a new figure
fig, ax = plt.subplots()

# Initialize the points' positions
points[:, 0] = points[:, 0]

# Function to update the points' positions
def update(frame):
    global points, velocities, accelerations
    
    # Update the points' accelerations
    accelerations[:, 0] = np.sin(2 * np.pi * frame / t_max)
    
    # Update the points' velocities
    velocities[:, 0] = velocities[:, 0] + accelerations[:, 0] * dt
    
    # Update the points' positions
    points[:, 0] = points[:, 0] + velocities[:, 0] * dt
    
    # Update the points' y-positions
    points[:, 1] = np.sin(2 * np.pi * frame / t_max)
    
    # Clear the current axes
    ax.clear()
    
    # Set the background color to black
    ax.set_facecolor('black')
    
    # Plot the points
    ax.scatter(points[:, 0], points[:, 1], color='white', s=100)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=int(t_max / dt), interval=dt * 1000)

# Show the animation
plt.show()
