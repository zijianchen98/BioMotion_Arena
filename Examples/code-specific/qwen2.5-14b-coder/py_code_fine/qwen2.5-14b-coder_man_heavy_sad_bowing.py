
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
num_lights = 15

# Define the initial positions of the point-lights
initial_positions = np.random.rand(num_lights, 2)

# Define the target positions for each frame of the animation
target_positions = []
for i in range(100):  # 100 frames
    # Generate a new set of target positions
    targets = np.random.rand(num_lights, 2)
    # Interpolate between the current and target positions
    target_positions.append(np.linspace(initial_positions, targets, num=20))

# Flatten the target positions list
target_positions = np.concatenate(target_positions)

# Create a figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Create a scatter plot for the point-lights
scatter = ax.scatter([], [], color='white')

# Define the update function for the animation
def update(frame):
    # Get the current positions of the point-lights
    current_positions = target_positions[frame * num_lights:(frame + 1) * num_lights]
    # Update the scatter plot
    scatter.set_offsets(current_positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(target_positions) // num_lights, blit=True, interval=50)

# Show the animation
plt.show()
