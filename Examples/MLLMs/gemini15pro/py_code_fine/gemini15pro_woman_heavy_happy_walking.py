
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be replaced with actual motion capture data or similar
# to achieve realistic biomechanical motion.
# The structure is: [frame, point, coordinate (x,y)]
motion_data = np.zeros((60, 15, 2))

# Example: simple oscillatory motion for each point
for frame in range(60):
    for point in range(15):
        motion_data[frame, point, 0] = point * 10 + 5 * np.sin(frame/10 + point)
        motion_data[frame, point, 1] = (point % 3) * 20 + 10 * np.cos(frame/5 + point)


# Create the animation
fig, ax = plt.subplots()

# Initialize the point-light scatter plot
scatter = ax.scatter([], [], s=50, c='white')

# Set the axis limits based on the data (add some padding)
x_min = motion_data[:, :, 0].min() - 10
x_max = motion_data[:, :, 0].max() + 10
y_min = motion_data[:, :, 1].min() - 10
y_max = motion_data[:, :, 1].max() + 10
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_facecolor('black')


def animate(i):
    """Update the scatter plot for frame i."""
    x = motion_data[i, :, 0]
    y = motion_data[i, :, 1]
    scatter.set_offsets(np.c_[x, y])  # Update point positions
    return scatter,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(60), blit=True, interval=30)

# To save the animation as a GIF or MP4, uncomment the appropriate line below
# ani.save('walking_animation.gif', writer='imagemagick') # Requires imagemagick
# ani.save('walking_animation.mp4', writer='ffmpeg') # Requires ffmpeg

plt.show()

