
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Define the initial positions of the point lights
x = np.array([0, 1, 1, 1, 2, 2, 2, 2, 0, -1, -1, -1, -2, -2, -2])
y = np.array([5, 4, 3, 2, 4, 3, 2, 1, 0, -1, -2, -3, -1, -2, -3])


# Define the animation function
def animate(i):
    # Update the positions of the point lights
    global x,y
    
    # waving hand animation (example)
    x[2] += np.sin(i/10) *0.5
    y[2] += np.cos(i/10)*0.5
    x[3] += np.sin(i/10) *0.5
    y[3] += np.cos(i/10)*0.5
    x[10] += np.sin(i/10) *0.5
    y[10] -= np.cos(i/10)*0.5
    x[11] += np.sin(i/10) *0.5
    y[11] -= np.cos(i/10)*0.5


    # Clear the previous frame
    ax.clear()
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Plot the point lights
    ax.plot(x, y, 'wo', markersize=8)


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50)

# Show the animation
plt.show()

