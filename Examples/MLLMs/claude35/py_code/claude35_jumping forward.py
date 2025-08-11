
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
frames = 60
jump_height = 2
jump_distance = 5

# Initialize figure
fig, ax = plt.subplots()
ax.set_xlim(-jump_distance, jump_distance)
ax.set_ylim(-1, jump_height + 1)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Define the initial positions of the point lights
# A simple representation of a human model using 15 points
initial_positions = np.array([
    [0, 0],           # Center of the body
    [0.5, 1.5],      # Right shoulder
    [-0.5, 1.5],     # Left shoulder
    [0.75, 1],       # Right elbow
    [-0.75, 1],      # Left elbow
    [0.5, 0.5],      # Right hand
    [-0.5, 0.5],     # Left hand
    [0, 1],          # Head
    [0, -0.5],       # Center of the body (bottom)
    [0.5, -1],       # Right hip
    [-0.5, -1],      # Left hip
    [0.5, -2],       # Right knee
    [-0.5, -2],      # Left knee
    [0.5, -3],       # Right foot
    [-0.5, -3],      # Left foot
])

# Create point-line collection
points, = ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

def animate(i):
    # Calculate the vertical and horizontal displacement
    t = i / frames
    height = -4 * (t - 0.5) ** 2 + jump_height  # Parabolic motion for jumping
    distance = jump_distance * t
    
    # Update point positions
    y_positions = initial_positions[:, 1] + height
    x_positions = initial_positions[:, 0] + distance
    
    points.set_data(x_positions, y_positions)
    return points,

# Create animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, interval=50, blit=True)

# Display the animation
plt.show()
