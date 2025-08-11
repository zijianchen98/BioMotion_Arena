
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize the axis with a black background
ax.set_facecolor(BLACK)

# Define the subject and action
subject = {'x': 200, 'y': 100, 'z': 50}
action = {'x': 50, 'y': 50, 'z': 0}

# Define the point-light sources
sources = []
for i in range(15):
    source = {'x': np.random.uniform(0, WIDTH), 'y': np.random.uniform(0, HEIGHT), 'z': np.random.uniform(-100, 100)}
    sources.append(source)

# Define the light source parameters
light_source = {'x': 0, 'y': 0, 'z': 1}

# Function to update the plot
def update(frame):
    global ax, sources, light_source

    # Clear the axis
    ax.clear()

    # Set the axis limits
    ax.set_xlim(-200, 200)
    ax.set_ylim(-100, 100)
    ax.set_zlim(-50, 50)

    # Draw the background
    ax.set_facecolor(BLACK)

    # Draw the point-lights
    for source in sources:
        # Calculate the position of the light source relative to the subject
        relative_x = source['x'] - subject['x']
        relative_y = source['y'] - subject['y']
        relative_z = source['z'] - subject['z']

        # Calculate the direction of the light source
        direction_x = relative_x / np.linalg.norm(relative_x)
        direction_y = relative_y / np.linalg.norm(relative_y)
        direction_z = relative_z / np.linalg.norm(relative_z)

        # Draw the light source
        ax.scatter(source['x'], source['y'], source['z'], c='w', s=1, marker='o')
        ax.scatter(source['x'] + direction_x * 10, source['y'] + direction_y * 10, source['z'] + direction_z * 10, c='w', s=1, marker='o')

    # Draw the light source
    ax.scatter(light_source['x'], light_source['y'], light_source['z'], c='w', s=1, marker='o')
    ax.scatter(light_source['x'] + light_source['x'] / 2, light_source['y'] + light_source['y'] / 2, light_source['z'] + light_source['z'] / 2, c='w', s=1, marker='o')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=20)

plt.show()
