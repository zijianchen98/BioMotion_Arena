
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need more frames for a smooth animation
# and more realistic jump motion.  You'd likely want to use motion capture data
# or a physics engine for more accurate movement.

frames = [
    # Frame 1 (Start of jump)
    [(1, 5), (2, 4), (3, 4), (1, 3), (3, 3), (0.5, 2), (1.5, 2), (2.5, 2), (3.5, 2), (1, 1), (3, 1), (1, 0), (2, 0), (1, -1), (3, -1)],
    # Frame 2 (Mid-air)
    [(1.5, 5.5), (2.5, 4.5), (3.5, 4.5), (1.5, 3.5), (3.5, 3.5), (1, 2.5), (2, 2.5), (3, 2.5), (4, 2.5), (1.5, 1.5), (3.5, 1.5), (1.5, 0.5), (2.5, 0.5), (1.5, -0.5), (3.5, -0.5)],
    # Frame 3 (Landing)
    [(2, 5), (3, 4), (4, 4), (2, 3), (4, 3), (1.5, 2), (2.5, 2), (3.5, 2), (4.5, 2), (2, 1), (4, 1), (2, 0), (3, 0), (2, -1), (4, -1)],



]

# Create figure and axes
fig, ax = plt.subplots()
ax.set_aspect('equal')  # Ensure points are circular
ax.set_xlim(0, 5)
ax.set_ylim(-2, 6)
ax.set_facecolor('black') # Set background color to black
scatter = ax.scatter([], [], s=30, c='white') # Set point color to white


# Animation update function
def update(frame):
    x = [point[0] for point in frames[frame]]
    y = [point[1] for point in frames[frame]]
    scatter.set_offsets(np.c_[x, y])
    return scatter,


# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(frames), interval=100, blit=True)


# For saving the animation as a gif or mp4 use the following lines. Uncomment to use.
# writer = animation.PillowWriter(fps=10)  # For GIF
# writer = animation.FFMpegWriter(fps=10) # For MP4
# ani.save("jumping_man.gif", writer=writer) # Replace with desired filename and extension


plt.show()
