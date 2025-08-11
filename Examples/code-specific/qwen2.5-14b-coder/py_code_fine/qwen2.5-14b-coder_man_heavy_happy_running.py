
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
# These positions are placeholders and should be replaced with actual biomechanical data
initial_positions = np.random.rand(num_lights, 2)

# Define the target positions for each point light
# These positions should represent the running motion of the happy man
target_positions = np.zeros((num_lights, 2))
for i in range(num_lights):
    target_positions[i] = [np.sin(i * 0.5), np.cos(i * 0.5)]

# Define the update function for the animation
def update(frame):
    # Interpolate between the initial and target positions
    current_positions = initial_positions + (target_positions - initial_positions) * frame / 100
    scatter.set_offsets(current_positions)
    return scatter,

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the scatter plot for the point lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=10)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
