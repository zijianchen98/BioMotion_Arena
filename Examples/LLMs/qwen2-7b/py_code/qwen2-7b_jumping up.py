
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim((-10, 10)
ax.set_ylim((-10, 10))
ax.set_aspect('equal')
ax.axis('off')

# Define the positions of the 15 white point-lights
points = np.array([
    [4, 5],
    [4, -i] for i in range((-3, 4)),
    [-4, i] for i in range((-3, 4)),
])

# Define the initial positions and velocities for each point-light
positions = points.copy()
velocities = np.zeros_like(points)

def update(frame_number):
    global positions, velocities
    
    # Calculate the new positions based on the current velocities
    positions += velocities
    
    # Update the velocity of each point-light based on its acceleration due to gravity
    # Assuming a constant gravitational force (g = 9.8 m/s^2
    g = 9.8
    accelerations = -np.ones_like(positions) * g
    velocities += accelerations
    
    # Keep the point-lights within the boundaries of the canvas
    positions[positions < -10] = -10
    positions[positions > 10] = 10
    
    # Update the scatter plot with the new positions
    scatter.set_offsets(positions)
    
    return scatter,

# Create the animation
scatter = ax.scatter(*positions.T, s=100, color='white')
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=20, blit=True)

plt.show()

