
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
num_lights = 15
x = np.random.rand(num_lights) * 20 - 10
y = np.random.rand(num_lights) * 20 - 10
points, = ax.plot(x, y, 'wo', markersize=8)


# Animation function
def animate(i):
    global x, y
    #Simulate turning around motion. Adjust parameters for different speeds and styles.
    x += np.random.normal(0, 0.1, num_lights)  # Add some noise for realism
    y += np.random.normal(0, 0.1, num_lights)
    #Circular Motion for the turning
    angle = i * 0.02
    radius = 5

    for j in range(num_lights):
        if j < 3:
            x[j] = radius * np.cos(angle + j * 0.2 )
            y[j] = radius * np.sin(angle + j * 0.2)
        elif j < 6:
             x[j] = radius * np.cos(angle + j * 0.1) + 2
             y[j] = radius * np.sin(angle + j * 0.1) - 2
        elif j < 9:
            x[j] = radius * np.cos(angle + j * 0.05) -2
            y[j] = radius * np.sin(angle + j * 0.05) + 2
        elif j < 12:
             x[j] = radius * np.cos(angle + j * 0.02) + 4
             y[j] = radius * np.sin(angle + j * 0.02) - 4
        else:
             x[j] = radius * np.cos(angle + j * 0.01) - 4
             y[j] = radius * np.sin(angle + j * 0.01) + 4
    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=360, interval=20, blit=True)


plt.show()
