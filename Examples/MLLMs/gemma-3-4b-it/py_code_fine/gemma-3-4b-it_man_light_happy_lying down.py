
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
duration = 100  # Frames
fps = 30
fig_size = (8, 8)

# Define the movement patterns for each light
# These patterns will be applied to the coordinates of the lights
# Each row represents a light, and each column represents a coordinate (x, y)
# The values represent the displacement in each coordinate over time
light_patterns = np.array([
    [0, 0],  # Light 1: No movement
    [10, 0],  # Light 2: Moves to the right
    [-10, 0], # Light 3: Moves to the left
    [0, 10],  # Light 4: Moves up
    [0, -10], # Light 5: Moves down
    [5, 5],  # Light 6: Moves diagonally up-right
    [-5, -5], # Light 7: Moves diagonally down-left
    [5, -5],  # Light 8: Moves diagonally down-right
    [-5, 5],  # Light 9: Moves diagonally up-left
    [2, 8],  # Light 10: Moves right and up
    [-2, 8], # Light 11: Moves left and up
    [2, -8], # Light 12: Moves right and down
    [-2, -8],# Light 13: Moves left and down
    [1, 7],  # Light 14: Moves right and up (small)
    [-1, 7], # Light 15: Moves left and up (small)
])

# Initialize the figure and axes
fig, ax = plt.subplots(figsize=fig_size)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Create the lights
lights = []
for i in range(num_lights):
    light, = ax.plot([], [], 'w', markersize=5)
    lights.append(light)

# Animation function
def animate(frame):
    for i in range(num_lights):
        x = light_patterns[i, 0]
        y = light_patterns[i, 1]
        lights[i].set_data(x, y)
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=duration, blit=True, repeat=True)

# Save the animation (optional)
# ani.save("happyman_motion.gif", writer='pillow', fps=fps)

plt.show()
