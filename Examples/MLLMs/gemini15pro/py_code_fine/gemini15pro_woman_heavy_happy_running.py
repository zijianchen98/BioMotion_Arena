
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the coordinates of the 15 point lights
# These are placeholder coordinates and should be replaced with actual motion capture data
# for a realistic running animation
num_points = 15
x = np.random.rand(num_points) * 2 - 1  # Initial x-coordinates between -1 and 1
y = np.random.rand(num_points) * 2 - 1  # Initial y-coordinates between -1 and 1

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_aspect('equal')
ax.set_facecolor('black')  # Set background color to black
points, = ax.plot(x, y, 'wo') # 'wo' creates white circles


# Define the animation function
def animate(i):
    global x, y
    # Update the coordinates of the point lights for each frame
    # Example: Simple oscillation for demonstration
    x += 0.01 * np.sin(i * 0.1) 
    y += 0.01 * np.cos(i * 0.1)


    # Update the plot with the new coordinates, ensuring smooth transitions.
    points.set_data(x, y)

    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Display the animation or save it to a file. To save it, uncomment the below two lines
# writer = animation.PillowWriter(fps=20)
# ani.save('running_animation.gif', writer=writer)

plt.show()
