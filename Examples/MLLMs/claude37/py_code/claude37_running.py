
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.axis('off')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Number of point-lights
num_points = 15

# Generate initial positions for the point-lights representing joints
positions = np.array([
    [0, 1],    # Head
    [-0.5, 0.75], [0.5, 0.75],  # Shoulders
    [-0.75, 0.5], [0.75, 0.5],  # Elbows
    [-0.5, 0.25], [0.5, 0.25],  # Hands
    [-0.5, 0], [0.5, 0],      # Hips
    [-0.75, -0.5], [0.75, -0.5],  # Knees
    [-0.5, -1], [0.5, -1],  # Feet
    [0, -1.5]  # Center of the body
])

# Create scatter plot for point-lights
points, = ax.plot([], [], 'o', color='white', markersize=10)

def init():
    points.set_data([], [])
    return points,

def update(frame):
    # Simulate running by updating the positions
    # Create a running motion pattern
    offset = 0.1 * np.sin(np.linspace(0, 2 * np.pi * 2, num_points) + frame * 0.1)
    positions[:, 0] += 0.1  # Move right across the screen
    # Update vertical positions to simulate smooth running
    positions[:, 1] += offset * np.array([1, 0.5] + [0.25]*6 + [0.5]*6) 

    # Wrap around if off-screen
    if positions[0, 0] > 2:
        positions[:, 0] -= 4  

    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=200, init_func=init,
                              blit=True, interval=20)

plt.show()
