
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be adjusted for realistic motion
def animate(frame):
    ax.clear()
    x = [2, 3, 4, 2.5, 3.5, 2, 3, 4, 2.2, 2.8, 3.2, 3.8, 1, 5, 3]
    y = [7, 7, 7, 6, 6, 5, 5, 5, 4, 4, 4, 4, 2, 2, 1]

    # Example subtle movement
    y[0] += np.sin(frame * 0.1) * 0.1
    y[1] += np.cos(frame * 0.1) * 0.1

    ax.scatter(x, y, c='white', s=50)  # s controls the size of the dots
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 8)
    ax.set_facecolor('black')  # set background to black
    ax.set_aspect('equal')  # Maintain aspect ratio
    ax.set_xticks([])  # Remove x ticks
    ax.set_yticks([])  # Remove y ticks


fig, ax = plt.subplots()

ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

# For displaying in a Jupyter Notebook
# from IPython.display import HTML
# HTML(ani.to_jshtml())

# Save the animation, adjust fps for desired speed
ani.save('lying_down.gif', writer='pillow', fps=20)  # or 'imagemagick' if installed
plt.show()

