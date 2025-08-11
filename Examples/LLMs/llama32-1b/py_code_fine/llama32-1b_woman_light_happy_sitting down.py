
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters
width, height = 800, 600
fps = 60
frame_rate = 1 / fps
num_points = 1000
num_strikes = 5
num_angles = 4
num_motions = 3

# Define the point-light model
class PointLight:
    def __init__(self, x, y, z, intensity):
        self.x = x
        self.y = y
        self.z = z
        self.intensity = intensity

    def update(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# Define the subject model
class Subject:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def update(self, x, y, z):
        self.x += 0.01
        self.y += 0.01
        self.z += 0.01

# Define the action model
class Action:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def update(self, x, y, z):
        self.x += 0.01
        self.y += 0.01
        self.z += 0.01

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize the points
points = np.zeros((num_points, 2))

# Initialize the strikes
strikes = np.zeros((num_strikes, 2))

# Initialize the angles
angles = np.zeros((num_angles, 2))

# Initialize the motions
motions = np.zeros((num_motions, 2))

# Define the initial positions and angles
initial_positions = np.array([width / 2, height / 2])
initial_angles = np.array([np.pi / 2, np.pi, np.pi / 2, np.pi / 2])

# Function to update the points
def update_points(positions, strikes, angles, motions):
    for i in range(num_points):
        points[i, 0] = positions[i]
        points[i, 1] = positions[i] + strikes[i] * np.sin(angles[i])
    return points

# Function to update the strikes
def update_strikes(strikes, angles, motions):
    for i in range(num_strikes):
        strikes[i] = np.sin(angles[i]) * motions[i]
    return strikes

# Function to update the angles
def update_angles(angles, motions):
    for i in range(num_angles):
        angles[i] = np.sin(angles[i]) * motions[i]
    return angles

# Function to update the motions
def update_motions(motions):
    for i in range(num_motions):
        motions[i] += 0.01
    return motions

# Initialize the points, strikes, angles, and motions
points = np.zeros((num_points, 2))
strikes = np.zeros((num_strikes, 2))
angles = np.zeros((num_angles, 2))
motions = np.zeros((num_motions, 2))

# Update the points
for i in range(num_points):
    points[i, 0] = initial_positions[i]
    points[i, 1] = initial_positions[i] + strikes[i] * np.sin(angles[i])
    angles[i] = initial_angles[i]

# Update the strikes
for i in range(num_strikes):
    strikes[i] = np.sin(angles[i]) * motions[i]

# Update the angles
for i in range(num_angles):
    angles[i] = np.sin(angles[i]) * motions[i]

# Update the motions
for i in range(num_motions):
    motions[i] += 0.01

# Animate the points
def animate(i):
    ax.clear()
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    ax.set_axis_off()
    ax.scatter(points[:, 0], points[:, 1], c=points[:, 0], s=10, alpha=0.5)
    ax.scatter(strikes[:, 0], strikes[:, 1], c=strikes[:, 0], s=10, alpha=0.5)
    ax.scatter(angles[:, 0], angles[:, 1], c=angles[:, 0], s=10, alpha=0.5)
    ax.scatter(motions[:, 0], motions[:, 1], c=motions[:, 0], s=10, alpha=0.5)
    ax.set_title(f'Frame {i+1} / {frame_rate}')

ani = animation.FuncAnimation(fig, animate, frames=num_points, interval=16, repeat=True, blit=True, save_count=True)

plt.show()
