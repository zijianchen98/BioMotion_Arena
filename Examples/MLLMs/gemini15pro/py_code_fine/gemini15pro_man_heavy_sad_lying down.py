
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be refined 
# for realistic biomechanical motion
def animate(i):
    x = np.array([5, 7, 9, 6, 8, 5, 9, 4, 6, 8, 10, 2, 3, 1, 4]) + np.sin(i * 0.1) * 0.5  # Subtle sway
    y = np.array([15, 15, 15, 12, 12, 9, 9, 6, 6, 6, 6, 3, 3, 1, 1]) + np.cos(i * 0.1) * 0.2 # Subtle bobbing
    scat.set_offsets(np.c_[x, y])
    return scat,

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black') # Set black background
ax.set_aspect('equal')  # Ensure same scaling of x and y axis
ax.set_xlim([0, 12])
ax.set_ylim([0, 16])
ax.set_xticks([]) #hide ticks
ax.set_yticks([])

# Initialize the point-lights
x = np.array([5, 7, 9, 6, 8, 5, 9, 4, 6, 8, 10, 2, 3, 1, 4])
y = np.array([15, 15, 15, 12, 12, 9, 9, 6, 6, 6, 6, 3, 3, 1, 1])
scat = ax.scatter(x, y, s=30, c='white') # s is size of points

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50, blit=True)

# For displaying in a Jupyter notebook
# from IPython.display import HTML
# HTML(ani.to_jshtml())

# Save the animation, if you want to keep it or upload as a response
# ani.save('lying_down_sadman.gif', writer='pillow', fps = 10) # fps = frames per second
# Set writer to 'imagemagick' if on Mac

plt.show()

