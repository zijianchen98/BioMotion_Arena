
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
frames = 60
fps = 24

# Initial positions of the points (simplified model)
initial_positions = np.array([
    [0.0, 0.8],  # Head
    [-0.1, 0.7], [-0.1, 0.6],  # Left eye, left eyebrow
    [0.1, 0.7], [0.1, 0.6],   # Right eye, right eyebrow
    [0.0, 0.5],               # Nose
    [0.0, 0.4],               # Mouth
    [-0.2, 0.3], [0.2, 0.3],   # Shoulders
    [-0.3, 0.2], [0.3, 0.2],   # Elbows
    [-0.3, 0.0], [0.3, 0.0],   # Hands
    [0.0, 0.2],               # Waist
    [-0.2, -0.1], [0.2, -0.1], # Hips
    [-0.2, -0.3], [0.2, -0.3]  # Feet
])

# Function to create a rotation matrix
def rotation_matrix(angle):
    return np.array([[np.cos(angle), -np.sin(angle)],
                     [np.sin(angle), np.cos(angle)]])

# Generate frames
positions = []
angle_increment = 2 * np.pi / frames
for frame in range(frames):
    angle = angle_increment * frame
    rot_mat = rotation_matrix(angle)
    rotated_positions = initial_positions @ rot_mat.T
    positions.append(rotated_positions)

# Plotting
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

points, = ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

def animate(i):
    x, y = positions[i].T
    points.set_data(x, y)
    return points,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, interval=1000/fps, blit=True)

plt.show()
