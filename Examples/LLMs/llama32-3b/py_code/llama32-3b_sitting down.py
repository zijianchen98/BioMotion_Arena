
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure size and background color
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_facecolor('black')

# Define the number of lights, their initial positions, and the target positions
num_lights = 15
light_positions = np.random.rand(num_lights, 2) * 2 - 1  # Random initial positions between -1 and 1
target_positions = np.array([
    [-0.5, 0.5],  # Head
    [-0.4, -0.5],  # Left shoulder
    [0.4, -0.5],  # Right shoulder
    [0.5, 0.5],  # Right elbow
    [-0.5, 0.5],  # Left elbow
    [-0.4, 0.2],  # Left hand
    [0.4, 0.2],  # Right hand
    [-0.5, -0.2],  # Left hip
    [0.5, -0.2],  # Right hip
    [0.2, -0.8],  # Left knee
    [-0.2, -0.8],  # Right knee
    [0.2, -0.6],  # Left ankle
    [-0.2, -0.6],  # Right ankle
    [0.2, -0.4],  # Left foot
    [-0.2, -0.4],  # Right foot
    [0.2, 0.2],  # Left hip (for sitting down)
    [-0.2, 0.2]  # Right hip (for sitting down)
])

# Create a function to update the light positions
def update(frame):
    # Calculate the movement of each light
    for i in range(num_lights):
        light_x = light_positions[i, 0]
        light_y = light_positions[i, 1]
        target_x = target_positions[i, 0]
        target_y = target_positions[i, 1]

        # Move the light towards the target position
        if frame < 100:
            light_x = light_x + (target_x - light_x) / 10
            light_y = light_y + (target_y - light_y) / 10
        elif frame < 200:
            light_x = light_x + (target_x - light_x) / 5
            light_y = light_y + (target_y - light_y) / 5
        elif frame < 300:
            light_x = light_x + (target_x - light_x) / 2
            light_y = light_y + (target_y - light_y) / 2

        # Ensure the light stays within the figure boundaries
        light_x = np.clip(light_x, -1, 1)
        light_y = np.clip(light_y, -1, 1)

        # Update the light position
        light_positions[i, 0] = light_x
        light_positions[i, 1] = light_y

    # Clear the axes and plot the lights
    ax.clear()
    ax.set_facecolor('black')
    for i in range(num_lights):
        ax.scatter(light_positions[i, 0], light_positions[i, 1], s=10, c='white', alpha=0.5)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=300, interval=50)

# Show the animation
plt.show()
