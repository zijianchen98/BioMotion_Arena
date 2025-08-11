
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create the positions of point lights representing a sad woman sitting down
def create_positions(t):
    # Create an array to hold the positions of the points
    positions = np.zeros((15, 2))
    
    # Define the base positions for the point lights (15 points)
    base_positions = np.array([
        [0, 2], [0.5, 2.5], [-0.5, 2.5], 
        [0, 1.5], [0.5, 2], [-0.5, 2],
        [0, 1], [0.5, 1.5], [-0.5, 1.5],
        [0, 0], [0.5, 1], [-0.5, 1],
        [0, -1], [0.5, 0], [-0.5, 0]
    ])
    
    # Apply downward motion for sitting down
    downward_motion = -0.05 * t
    
    # Update position based on time
    positions[:, 0] = base_positions[:, 0]
    positions[:, 1] = base_positions[:, 1] + downward_motion
    
    return positions

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', markersize=10, color='white')

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to animate the frame
def animate(t):
    pos = create_positions(t)
    points.set_data(pos[:, 0], pos[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 100, 0.1), init_func=init, blit=True, interval=20)

# Show the animation
plt.show()
