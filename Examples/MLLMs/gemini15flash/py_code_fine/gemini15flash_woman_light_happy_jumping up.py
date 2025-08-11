
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
num_points = 15
x = np.random.uniform(-5, 5, num_points)
y = np.random.uniform(-5, 5, num_points)

# Create the point light scatter plot
points, = ax.plot(x, y, 'wo', markersize=10)

# Define the animation function
def animate(i):
    # Generate random displacements for each point
    dx = np.random.normal(0, 0.5, num_points)
    dy = np.random.normal(0, 0.5, num_points)


    # Apply displacement to the x and y coordinates

    x += dx
    y += dy

    #Keep points within the range
    x = np.clip(x,-8,8)
    y = np.clip(y,-8,8)

    # Update the plot data
    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Save the animation as a GIF
ani.save('biological_motion.gif', writer='imagemagick')

# Show the plot (optional)
plt.show()

