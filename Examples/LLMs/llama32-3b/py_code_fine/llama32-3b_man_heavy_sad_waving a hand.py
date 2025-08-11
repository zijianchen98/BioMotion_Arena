
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of lights and their initial positions
num_lights = 15
initial_positions = np.array([
    [0.1, 0.1],  # head
    [0.2, 0.2],  # left shoulder
    [0.3, 0.3],  # left elbow
    [0.1, 0.5],  # left wrist
    [0.2, 0.4],  # left hand
    [0.3, 0.3],  # right shoulder
    [0.2, 0.2],  # right elbow
    [0.1, 0.1],  # right wrist
    [0.2, 0.5],  # right hand
    [0.3, 0.4],  # left hip
    [0.1, 0.6],  # left knee
    [0.2, 0.5],  # left ankle
    [0.3, 0.4],  # right hip
    [0.1, 0.6],  # right knee
    [0.2, 0.5],  # right ankle
])

# Define the motion parameters
motion_duration = 10
motion_speed = 0.5

# Create a figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Create a list to store the light objects
lights = []

# Create the light objects
for i in range(num_lights):
    x = initial_positions[i, 0]
    y = initial_positions[i, 1]
    lights.append(plt.Circle((x, y), 0.01, color='white', alpha=0.5))

# Add the lights to the axis
for light in lights:
    ax.add_artist(light)

# Set the limits of the axis
ax.set_xlim(-1, 4)
ax.set_ylim(-1, 7)

# Function to update the lights' positions
def update(frame):
    global initial_positions
    t = frame / motion_duration
    initial_positions = np.array([
        [0.1 + (0.2 - 0.1) * np.sin(2 * np.pi * t)],  # head
        [0.2 + (0.3 - 0.2) * np.sin(2 * np.pi * t)],  # left shoulder
        [0.3 + (0.4 - 0.3) * np.sin(2 * np.pi * t)],  # left elbow
        [0.1 + (0.2 - 0.1) * np.sin(2 * np.pi * t)],  # left wrist
        [0.2 + (0.3 - 0.2) * np.sin(2 * np.pi * t)],  # left hand
        [0.3 + (0.4 - 0.3) * np.sin(2 * np.pi * t)],  # right shoulder
        [0.2 + (0.3 - 0.2) * np.sin(2 * np.pi * t)],  # right elbow
        [0.1 + (0.2 - 0.1) * np.sin(2 * np.pi * t)],  # right wrist
        [0.2 + (0.3 - 0.2) * np.sin(2 * np.pi * t)],  # right hand
        [0.3 + (0.4 - 0.3) * np.sin(2 * np.pi * t)],  # left hip
        [0.1 + (0.6 - 0.1) * np.sin(2 * np.pi * t)],  # left knee
        [0.2 + (0.5 - 0.2) * np.sin(2 * np.pi * t)],  # left ankle
        [0.3 + (0.4 - 0.3) * np.sin(2 * np.pi * t)],  # right hip
        [0.1 + (0.6 - 0.1) * np.sin(2 * np.pi * t)],  # right knee
        [0.2 + (0.5 - 0.2) * np.sin(2 * np.pi * t)],  # right ankle
    ])

    # Clear the axis
    ax.clear()

    # Set the background color to black
    ax.set_facecolor('black')

    # Create a list to store the light objects
    lights = []

    # Create the light objects
    for i in range(num_lights):
        x = initial_positions[i, 0]
        y = initial_positions[i, 1]
        lights.append(plt.Circle((x, y), 0.01, color='white', alpha=0.5))

    # Add the lights to the axis
    for light in lights:
        ax.add_artist(light)

    # Set the limits of the axis
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 7)

# Animate the lights
ani = animation.FuncAnimation(fig, update, frames=range(1000), interval=50)

plt.show()
