
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and frames
num_points = 15
num_frames = 60

# Define the initial positions of the points
positions = np.random.rand(num_points, 2)

# Define the velocities of the points
velocities = np.random.randn(num_points, 2)
velocities /= np.linalg.norm(velocities, axis=1, keepdims=True)

# Define the acceleration due to gravity
gravity = np.array([0, -9.8])

# Create a figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create a scatter plot for the points
scatter = ax.scatter(positions[:, 0], positions[:, 1], color='white', s=50)

def update(frame):
    global positions, velocities
    
    # Update the positions based on velocities and gravity
    positions += velocities
    
    # Apply friction to slow down the points
    velocities *= 0.99
    
    # Add some random noise to simulate real-world motion
    velocities += np.random.randn(num_points, 2) * 0.1
    
    # Keep the points within the bounds of the animation area
    positions = np.clip(positions, -1, 1)
    
    # Update the scatter plot
    scatter.set_offsets(positions)
    
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
