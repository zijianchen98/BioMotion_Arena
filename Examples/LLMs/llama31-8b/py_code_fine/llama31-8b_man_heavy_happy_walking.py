
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Define the figure and axis
fig, ax = plt.subplots()

# Set the axis limits and aspect ratio
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')

# Define the point-light positions
num_lights = 15
light_positions = np.zeros((num_lights, 2))
light_positions[:, 0] = np.random.uniform(-0.5, 0.5, num_lights)
light_positions[:, 1] = np.random.uniform(-0.5, 0.5, num_lights)

# Define the action parameters
action_name = 'walking'
action_duration = 10  # seconds
fps = 30
num_frames = int(action_duration * fps)

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Update the point-light positions
    if i % 2 == 0:
        light_positions[:, 0] += 0.01
    else:
        light_positions[:, 0] -= 0.01

    # Ensure point-lights stay within the body
    light_positions[:, 0] = np.clip(light_positions[:, 0], -0.5, 0.5)
    light_positions[:, 1] = np.clip(light_positions[:, 1], -0.5, 0.5)

    # Plot the point-lights
    for position in light_positions:
        ax.scatter(position[0], position[1], color='white', s=100)

    # Plot the body
    body = patches.Rectangle((-0.5, -0.5), 1, 1, edgecolor='white', facecolor='none', lw=2)
    ax.add_patch(body)

    # Plot the head
    head = patches.Circle((0, 0.5), 0.1, edgecolor='white', facecolor='none', lw=2)
    ax.add_patch(head)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=1000 // fps)

# Display the animation
plt.show()
