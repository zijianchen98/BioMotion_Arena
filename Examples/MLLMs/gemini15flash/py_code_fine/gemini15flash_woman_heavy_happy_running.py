
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point-lights
num_points = 15
x = np.random.rand(num_points) * 20 - 10
y = np.random.rand(num_points) * 20 - 10
points, = ax.plot(x, y, 'wo', markersize=8)

# Define the animation update function
def animate(i):
    global x, y
    #Simulate running motion.  This is a simplified example.  
    # For a more realistic animation, you would need a more sophisticated model of human movement.

    dx = np.random.normal(0, 0.5, num_points)  # Add some randomness to the movement
    dy = np.random.normal(0, 0.5, num_points)
    
    #Add cyclic movement pattern to simulate running
    x += dx + np.sin(i/10) * 2  #Simulate legs moving forward and backward
    y += dy + np.cos(i/10) * 0.5 #Simulate body bouncing slightly

    #Keep points within the screen boundaries
    x = np.clip(x, -10, 10)
    y = np.clip(y, -10, 10)

    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=500, interval=20, blit=True)

# Show the animation
plt.show()

