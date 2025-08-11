
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of lights and frames
num_lights = 15
num_frames = 100

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Create the scatter plot for the lights
lights = ax.scatter([], [], c='white', s=50)

# Generate random initial positions for the lights
positions = np.random.rand(num_lights, 2) * 2 - 1

# Define the function to update the position of each light for the turning motion
def update_positions(frame):
    theta = np.radians(frame * 3.6)  # 3.6 degrees per frame for a full turn in 100 frames
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                [np.sin(theta), np.cos(theta)]])
    positions_rotated = np.dot(positions, rotation_matrix.T)
    return positions_rotated

# Animation update function
def animate(frame):
    new_positions = update_positions(frame)
    lights.set_offsets(new_positions)
    return lights,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=40, blit=True)

# Show the plot
plt.show()
