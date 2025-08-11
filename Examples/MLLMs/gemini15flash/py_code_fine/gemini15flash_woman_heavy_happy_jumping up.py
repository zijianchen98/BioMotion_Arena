
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Define the initial positions of the point lights
x = np.array([0, 1, 1, 1, 0, -1, -1, -1, 0, 0, 0.5, -0.5, 0.5, -0.5, 0])
y = np.array([0, 1, 0, -1, -2, -1, 0, 1, 2, 3, 2.5, 2.5, 3.5, 3.5, 4])


# Define the animation function
def animate(i):
    ax.clear()
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Update the positions of the point lights based on time
    global x, y
    t = i / 100
    x_new = x + np.sin(t + x) * 0.5
    y_new = y + (np.sin(t*2 + y) + 2) * 0.7  # added upward motion
    x = x_new
    y = y_new


    # Plot the point lights
    ax.plot(x, y, 'wo', markersize=5)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=300, interval=20)

plt.show()

