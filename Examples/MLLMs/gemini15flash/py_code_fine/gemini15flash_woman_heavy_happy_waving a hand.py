
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
x = np.zeros(num_lights)
y = np.zeros(num_lights)
points, = ax.plot(x, y, 'wo', markersize=10)

# Define the animation function
def animate(i):
    # Generate random motion for each point light
    dx = np.random.normal(0, 0.1, num_lights)
    dy = np.random.normal(0, 0.1, num_lights)
    
    #add some constraint to make the motion realistic
    x_new = x + dx
    y_new = y + dy
    
    #ensure points stay within the boundaries
    x_new = np.clip(x_new,-8,8)
    y_new = np.clip(y_new,-8,8)

    # Update the point light positions
    global x,y
    x = x_new
    y = y_new

    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()

