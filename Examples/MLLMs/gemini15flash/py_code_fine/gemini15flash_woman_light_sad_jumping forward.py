
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the points
num_points = 15
x = np.random.rand(num_points) * 10 - 5
y = np.random.rand(num_points) * 10 - 5
points, = ax.plot(x, y, 'wo', markersize=8)


# Animation function
def animate(i):
    global x, y
    #Simulate jumping forward motion. Adjust parameters for different motions.
    dx = np.random.normal(0.1,0.05, num_points) #add some randomness
    dy = np.random.normal(0,0.05, num_points)
    x += dx
    y += dy
    
    #Keep points within bounds
    x = np.clip(x,-5,5)
    y = np.clip(y,-5,5)
    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Show the animation
plt.show()

