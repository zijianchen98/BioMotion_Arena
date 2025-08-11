
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point lights
num_points = 15
x = np.zeros(num_points)
y = np.zeros(num_points)
points, = ax.plot(x, y, 'wo', markersize=10)


# Define the animation function
def animate(i):
    # Define the positions of the points
    global x,y
    # Sadman waving a hand animation.  Adjust parameters for different motions
    x[0] = np.sin(i/10)
    y[0] = 5
    x[1] = np.sin(i/10) + 1
    y[1] = 4
    x[2] = np.sin(i/10) +2
    y[2] = 4
    x[3] = np.sin(i/10) +1
    y[3] = 3
    x[4] = np.sin(i/10) +2
    y[4] = 3
    x[5] = np.sin(i/10)
    y[5] = 2
    x[6] = np.sin(i/10) +1
    y[6] = 2
    x[7] = np.sin(i/10) + 2
    y[7] = 2
    x[8] = np.sin(i/10) + 1
    y[8] = 1
    x[9] = np.sin(i/10) +2
    y[9] = 1
    x[10] = np.sin(i/10)
    y[10] = 0
    x[11] = np.sin(i/10) +1
    y[11] = 0
    x[12] = np.sin(i/10)
    y[12] = -1
    x[13] = np.sin(i/10) + 1
    y[13] = -1
    x[14] = np.sin(i/10) + 2
    y[14] = -2


    # Update the point positions
    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(1000), interval=20, blit=True)

# Save the animation as a GIF (optional)
# ani.save('biological_motion.gif', writer='pillow', fps=30)


# Show the animation
plt.show()

