
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the points
num_points = 15
x = np.zeros(num_points)
y = np.zeros(num_points)
points, = ax.plot(x, y, 'wo', markersize=10)

# Define the animation function
def animate(i):
    # Define the bowing motion using sine and cosine waves
    # Adjust parameters for different speeds and amplitudes
    angle = i * 0.05
    x[0] = 0
    y[0] = 5 + 3 * np.sin(angle)  # Head moves up and down
    x[1] = 1 + np.cos(angle + np.pi / 3)
    y[1] = 3 + 2 * np.sin(angle + np.pi / 3)
    x[2] = -1 + np.cos(angle + 2 * np.pi / 3)
    y[2] = 3 + 2 * np.sin(angle + 2 * np.pi / 3)
    x[3] = 2 + np.cos(angle + np.pi / 2)
    y[3] = 1 + 2 * np.sin(angle + np.pi / 2)
    x[4] = -2 + np.cos(angle + 3 * np.pi / 2)
    y[4] = 1 + 2 * np.sin(angle + 3 * np.pi / 2)
    x[5] = 1 + np.cos(angle)
    y[5] = -1 + 2*np.sin(angle)
    x[6] = -1 + np.cos(angle + np.pi)
    y[6] = -1 + 2 * np.sin(angle + np.pi)
    x[7] = 1.5 + np.cos(angle + np.pi/4)
    y[7] = -3 + 2* np.sin(angle + np.pi/4)
    x[8] = -1.5 + np.cos(angle + 3* np.pi/4)
    y[8] = -3 + 2 * np.sin(angle + 3*np.pi/4)
    x[9] = 2.5 + np.cos(angle + np.pi/6)
    y[9] = -5 + np.sin(angle + np.pi/6)
    x[10] = -2.5 + np.cos(angle + 5*np.pi/6)
    y[10] = -5 + np.sin(angle + 5*np.pi/6)
    x[11] = 0.7
    y[11] = -7
    x[12] = -0.7
    y[12] = -7
    x[13] = 0
    y[13] = -8.5
    x[14] = 0
    y[14] = -9.5


    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=360, interval=20, blit=True)

# Show the animation
plt.show()

