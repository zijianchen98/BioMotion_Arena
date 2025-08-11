
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the subject and action
subject = 'sadman'
action = 'jumping forward'

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim((-10, 10)
ax.set_ylim((-10, 10))
ax.set_aspect('equal')
ax.axis('off')

# Create the initial positions for the point-lights
initial_positions = [(np.random.uniform(-8, 8), np.random.uniform(-8, 8)) for _ in range(15]

# Function to update the positions of the point-lights
def update(frame):
    global initial_positions
    # Simulate the movement based on the action
    if action == 'jumping forward':
        new_positions = [(x + np.sin(frame / 10) * 1.5, y + np.cos(frame / 10) * 1.5) for x, y in initial_positions]
    # Add other actions here...
    # Update the positions of the point-lights
    for i, (new_position in enumerate(new_positions):
        initial_positions[if] = new_position
        ax.scatter(*new_position, color='white', s=50)

    return [ax.scatter(*pos, color='white', s=50) for pos in initial_positions]

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 400, interval=20)

# Show the animation
plt.show()
