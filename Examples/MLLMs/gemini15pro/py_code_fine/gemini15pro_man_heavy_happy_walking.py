
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point lights over time
# This is a simplified example and would need more frames for a smooth animation
# and realistic "heavy weight" walking motion.
# Each frame is a list of (x, y) coordinates for each of the 15 points.

frames = [
    # Frame 1
    [(1, 5), (2, 4), (3, 4), (1, 3), (3, 3), (1, 2), (2, 2), (3, 2), (1.5, 1), (2.5, 1), (2, 0), (1.5, -1), (2.5, -1), (2, -2), (2, -3)],
    # Frame 2 (shifted slightly to simulate movement)
    [(1.2, 5), (2.2, 4), (3.2, 4), (1.2, 3), (3.2, 3), (1.2, 2), (2.2, 2), (3.2, 2), (1.7, 1), (2.7, 1), (2.2, 0), (1.7, -1), (2.7, -1), (2.2,-2.2), (2.2, -2.8)],
    # Frame 3 (shifted further)
    [(1.4, 5), (2.4, 4), (3.4, 4), (1.4, 3), (3.4, 3), (1.4, 2), (2.4, 2), (3.4, 2), (1.9, 1), (2.9, 1), (2.4, 0), (1.9, -1), (2.9, -1), (2.4, -2.4), (2.4,-2.6)],
    # ... More frames would go here ...
]


# Create the figure and axes
fig, ax = plt.subplots()
ax.set_aspect('equal')  # Ensure points are circular
ax.set_xlim(0, 4)
ax.set_ylim(-4, 6)
ax.set_facecolor('black') # set background color to be black


# Initialize the point light scatter plot
scatter = ax.scatter([], [], s=20, c='white')


# Animation update function
def update(frame_num):
    x = [coord[0] for coord in frames[frame_num]]
    y = [coord[1] for coord in frames[frame_num]]
    scatter.set_offsets(np.c_[x, y])
    return scatter,


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(frames), interval=50, blit=True)


# Show the animation (optional, if you want to display it directly)
plt.show()



# Save the animation (optional, if you want to save it as a file)
# ani.save('point_light_walker.gif', writer='imagemagick') # requires imagemagick

