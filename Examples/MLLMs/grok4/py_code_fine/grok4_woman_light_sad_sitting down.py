
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up parameters for the animation
num_lights = 15
frames = 100
duration = 4  # seconds
fps = frames / duration
time = np.linspace(0, duration, frames)

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Define initial positions of point lights (body joints)
initial_positions = np.array([
    [0, 1],   # Head
    [-0.5, 0.6],  # Left shoulder
    [0.5, 0.6],   # Right shoulder
    [-0.5, 0.3],  # Left elbow
    [0.5, 0.3],   # Right elbow
    [-0.5, 0],    # Left wrist
    [0.5, 0],     # Right wrist
    [-0.3, -0.6], # Left hip
    [0.3, -0.6],  # Right hip
    [-0.3, -1],   # Left knee
    [0.3, -1],    # Right knee
    [0, -1.2],    # Feet (sitting down)
    [0.15, -1.2],
    [-0.15, -1.2],
    [0, -1.3],
    [0, -1.4]
])

# Simulate downward movement for sitting
def animate(frame):
    # Update positions of each point light
    positions = initial_positions.copy()
    positions[0, 1] -= frame * 0.01  # Move head down
    positions[1:5, 1] -= frame * 0.01  # Shoulders & elbows
    positions[8:11, 1] -= frame * 0.01  # Knees down further
    
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create an animation
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=1000/fps, blit=True)

# Display the animation
plt.show()
