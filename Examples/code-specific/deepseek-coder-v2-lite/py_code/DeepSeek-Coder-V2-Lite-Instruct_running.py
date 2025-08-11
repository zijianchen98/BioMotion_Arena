
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100
light_radius = 0.2
black_background = np.zeros((60, 60))

# Initial positions of the lights
positions = np.random.rand(num_lights, 2) * 50 + 5

# Function to update the positions of the lights
def update(frame):
    global positions
    positions[:, 1] += 0.1  # Move down
    if positions[:, 1] > 60:
        positions[:, 1] = 0
    positions[:, 0] += 0.1  # Move right
    if positions[:, 0] > 60:
        positions[:, 0] = 0

    # Clear the background
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(0, 60)
    ax.set_ylim(0, 60)

    # Draw the lights
    for pos in positions:
        circle = plt.Circle(pos, light_radius, color='white')
        ax.add_artist(circle)

# Create the animation
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, frames=num_frames, repeat=True)

# Show the animation
plt.show()
