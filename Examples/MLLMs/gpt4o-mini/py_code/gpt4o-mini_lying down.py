
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set parameters
num_points = 15
frames = 100
x_limits = (-1, 1)
y_limits = (0, 2)

# Define the initial positions of the point-lights for lying down pose
initial_positions = np.array([
    (-0.3, 1.8), (0.3, 1.8),  # Head
    (-0.6, 1.5), (0.6, 1.5),  # Shoulders
    (-0.5, 1.2), (0.5, 1.2),  # Chest
    (-0.4, 0.9), (0.4, 0.9),  # Waist
    (-0.3, 0.6), (0.3, 0.6),  # Knees
    (-0.2, 0.3), (0.2, 0.3),  # Folds
    (-0.1, 0.0), (0.1, 0.0),  # Feet
    (0.0, 0.7)                # Center
])

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(x_limits)
ax.set_ylim(y_limits)
ax.set_facecolor('black')

# Create the point-lights
points, = ax.plot([], [], 'o', color='white')

# Define initialization function
def init():
    points.set_data([], [])
    return points,

# Define animation function
def animate(i):
    # Update positions to simulate realistic movement of lying down
    # This can be more complicated to model biomechanics,
    # here we maintain a simple linear motion across frames
    motion_offsets = np.array([
        0.1 * np.sin(np.pi * i / frames + j) for j in range(num_points)
    ])
    
    # Modify y-coordinates to simulate slight movement
    updated_positions = initial_positions[:, 1] + motion_offsets
    updated_positions = np.column_stack((initial_positions[:, 0], updated_positions))
    
    points.set_data(updated_positions[:, 0], updated_positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, interval=50, blit=True)

# Display the animation
plt.show()
