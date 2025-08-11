
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points to represent a human figure
# Approximate positions for a human-like figure
initial_positions = np.array([
    [0, 2],    # Head
    [-0.5, 1],  # Neck
    [-1, 0],    # Left shoulder
    [0.5, 1],   # Right shoulder
    [1, 0],     # Right shoulder
    [-1.5, -0.5],  # Left elbow
    [1.5, -0.5],   # Right elbow
    [-1.5, -1.5],  # Left hand
    [1.5, -1.5],   # Right hand
    [0, 0],     # Spine
    [0, -1],    # Hips
    [-0.5, -2],  # Left knee
    [0.5, -2],   # Right knee
    [-0.5, -3],  # Left foot
    [0.5, -3]    # Right foot
])

def update_positions(positions, frame):
    # Simplified motion: jumping upward and then returning
    amplitude = 0.5
    frequency = 0.1
    y_displacement = amplitude * np.sin(2 * np.pi * frequency * frame)
    
    # Update y positions of all points
    positions[:, 1] += y_displacement

    # Return to original height on the way down
    if frame % (1 / frequency) > 0.5 / frequency:
        positions[:, 1] -= y_displacement

    return positions

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 3)
ax.set_facecolor('black')

points, = ax.plot([], [], 'wo')

def init():
    points.set_data([], [])
    return points,

def animate(frame):
    positions = update_positions(initial_positions.copy(), frame)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

ani = animation.FuncAnimation(fig, animate, frames=range(100), init_func=init, blit=True)
plt.show()
