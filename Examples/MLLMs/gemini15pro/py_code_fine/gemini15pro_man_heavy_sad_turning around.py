
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be fleshed out for a realistic animation
# Each point is represented by a list of its x, y coordinates over time.

num_frames = 60  # Example: 60 frames for the animation

# Example coordinates for the point-lights, adjust these for the desired motion
point_lights = []
for i in range(15):
    x = np.linspace(i * 10, (i * 10) + (i % 2 * 50), num_frames)
    y = np.linspace(i * 5, (i * 5) + (i % 2 * 30), num_frames)
    point_lights.append([x,y])


# Create the figure and axes for the animation
fig, ax = plt.subplots()
ax.set_xlim([0, 200])  # Set the x-axis limits
ax.set_ylim([0, 200])  # Set the y-axis limits
ax.set_aspect('equal')  # Ensure equal aspect ratio
ax.set_facecolor('black')  # Set background color to black

# Create the scatter plot for the point-lights
scatter = ax.scatter([], [], s=30, c='white')  # s is marker size


# Animation update function
def update(frame):
    x_coords = [point_lights[i][0][frame] for i in range(15)]
    y_coords = [point_lights[i][1][frame] for i in range(15)]

    scatter.set_offsets(np.c_[x_coords, y_coords])

    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(num_frames), blit=True, interval=30)


plt.show()
