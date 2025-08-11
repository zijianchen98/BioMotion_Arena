
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of lights and their initial positions
num_lights = 15
initial_positions = [(np.cos(i * 2 * np.pi / num_light), np.sin(i * 2 * np.pi / num_light)) for i in range(num_light)]

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
circle = plt.Circle((0, 0), 0.1, color='white', fill=True)
ax.add_artist(circle)

# Function to update the position of each light
def update(frame):
    global initial_positions
    # Calculate new positions based on the turn around action
    new_positions = [(x * np.cos(frame / 10) - y * np.sin(frame / 10), x * np.sin(frame / 10) + y * np.cos(frame / 10)) for x, y in initial_positions]
    for i, (position in enumerate(new_positions):
        circle = plt.Circle(position, 0.1, color='white', fill=True)
        ax.add_artist(circle)
    # Remove the old circles
    for artist in ax.patches:
        artist.remove()
    return [circle]

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange((-100, 100), blit=True, repeat=True)

plt.show()

