
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
frames = 200
fps = 30
dt = 1 / fps
g = 9.81  # gravity

# Initial positions and velocities
np.random.seed(42)
positions = np.zeros((num_lights, 2))
velocities = np.zeros((num_lights, 2))

# Define the joints and their connections for a simplified model of a person rolling forward
joints = [
    (0, 1), (1, 2), (2, 3), (3, 4),  # head, neck, torso, hip
    (4, 5), (5, 6), (4, 7), (7, 8),  # right leg, left leg
    (4, 9), (9, 10), (4, 11), (11, 12),  # right arm, left arm
    (10, 13), (12, 14)  # hands
]

# Initial setup
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

points, = ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

def update(frame):
    global positions, velocities
    
    # Simple physics simulation for forward rolling
    for i in range(num_lights):
        if i == 4:  # Hip joint
            velocities[i, 0] += 0.5 * dt  # Forward motion
            velocities[i, 1] -= g * dt  # Gravity
        else:
            velocities[i, 1] -= g * dt  # Gravity
        
        positions[i] += velocities[i] * dt
    
    # Constrain positions to simulate rolling
    for i in range(num_lights):
        if positions[i, 1] < -1:
            positions[i, 1] = -1
            velocities[i, 1] *= -0.8  # Bounce effect
    
    # Update points
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Animation
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=1000/fps)

plt.show()
