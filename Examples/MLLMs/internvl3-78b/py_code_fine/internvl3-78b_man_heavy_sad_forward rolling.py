
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Total number of frames
total_frames = 120
# Total number of point-lights
points = 15
# Duration of the animation (in seconds)
duration = 4
# Time between each frame
interval = duration * 1000 / total_frames

# Points' coordinates
# x, y coordinates of the points at the start and end of the animation
start_coords = np.array([
    [3, 8], [4, 8], [5, 8], [6, 8], [7, 8],
    [4, 7], [5, 7], [6, 7], [7, 7],
    [5, 6], [6, 6],
    [4, 5], [5, 5], [6, 5],
    [5, 4]
])
end_coords = np.array([
    [8, 8], [9, 8], [10, 8], [11, 8], [12, 8],
    [9, 7], [10, 7], [11, 7], [12, 7],
    [10, 6], [11, 6],
    [9, 5], [10, 5], [11, 5],
    [10, 4]
])

# The function to update the animation
def update(num, points_scatter):
    t = num / total_frames  # Progress through the animation
    coords = (1 - t) * start_coords + t * end_coords
    points_scatter.set_offsets(coords)
    return points_scatter,

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim([-2, 15])
ax.set_ylim([-2, 15])
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

# Create scatter plot
points_scatter = ax.scatter(start_coords[:, 0], start_coords[:, 1], color='white', s=50)

# Start the animation
ani = animation.FuncAnimation(fig, update, fargs=(points_scatter,), frames=total_frames, interval=interval, blit=True)

# Display the animation
plt.show()
