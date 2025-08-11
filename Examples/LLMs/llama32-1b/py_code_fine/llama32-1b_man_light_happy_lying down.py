
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

# Define the parameters of the point-light stimulus
num_points = 15
light_intensity = 0.5
light_direction = np.array([random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)])

# Define the parameters of the subject
subject_position = np.array([0, 0, 0])
subject_rotation = np.array([random.uniform(0, 2 * np.pi), random.uniform(0, 2 * np.pi), random.uniform(0, 2 * np.pi)])

# Define the parameters of the action
action_position = np.array([random.uniform(-1, 1), random.uniform(-1, 1), 0])
action_rotation = np.array([random.uniform(0, 2 * np.pi), random.uniform(0, 2 * np.pi), random.uniform(0, 2 * np.pi)])

# Function to generate a random point in 3D space
def random_point():
    return np.random.uniform(-1, 1, 3)

# Function to generate a random direction vector
def random_direction():
    return np.random.uniform(-1, 1, 3)

# Function to generate a random rotation angle
def random_rotation():
    return np.random.uniform(0, 2 * np.pi)

# Function to generate a random point-light stimulus
def generate_point_light():
    position = subject_position + action_position
    direction = light_direction + light_intensity * action_rotation
    return position, direction

# Function to generate a random subject
def generate_subject():
    position = subject_position
    rotation = subject_rotation + random_rotation()
    return position, rotation

# Function to generate a random action
def generate_action():
    position = action_position
    rotation = action_rotation
    return position, rotation

# Generate random point-light stimuli
point_light_stimuli = [generate_point_light() for _ in range(num_points)]

# Generate random subjects
subjects = [generate_subject() for _ in range(num_points)]

# Generate random actions
actions = [generate_action() for _ in range(num_points)]

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the point-light stimuli
for i, (position, direction) in enumerate(point_light_stimuli):
    ax.scatter(position[0], position[1], position[2], c='w', s=10)
    ax.scatter(direction[0], direction[1], direction[2], c='w', s=10)

# Plot the subjects
for i, (position, rotation) in enumerate(subjects):
    ax.quiver(position[0], position[1], position[2], rotation[0], rotation[1], rotation[2], color='b')

# Plot the actions
for i, (position, rotation) in enumerate(actions):
    ax.quiver(position[0], position[1], position[2], rotation[0], rotation[1], rotation[2], color='r')

# Set the limits and aspect ratio of the axis
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_aspect('equal')

# Show the plot
plt.show()
