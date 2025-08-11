
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define parameters
num_points = 15
frames = 60

# Initialize point positions (15 points to represent body joints)
# These are arbitrary positions and will be animated to mimic bowing
initial_positions = np.array([
    [0, 1],
    [-0.5, 0.5], [0.5, 0.5],
    [-0.5, 0], [0.5, 0],
    [-0.5, -0.5], [0.5, -0.5],
    [0, 0],  # Center of mass / hips
    [-0.2, -1], [0.2, -1],  # Legs
    [-0.5, -1.5], [0.5, -1.5],  # Feet
    [0, 2],  # Head
])

# Setup the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')

# Create points
points, = ax.plot([], [], 'o', color='white')

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to animate the bowing motion
def animate(frame):
    # Create a bowing motion by modifying the y-coordinates
    # The bowing motion lowers the body and shifts the head slightly forward
    y_offset = -0.05 * np.sin(np.pi * frame / (frames / 2))  # Bowing effect
    positions = initial_positions.copy()
    
    # Adjust the body position based on the bowing
    positions[:, 1] += y_offset

    # Update point positions
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=frames, init_func=init,
                              blit=True, interval=1000/30)

plt.show()
