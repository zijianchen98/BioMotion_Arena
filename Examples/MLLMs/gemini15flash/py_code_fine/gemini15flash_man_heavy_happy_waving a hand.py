
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the point lights
x = np.array([0, -1, 1, -2, 0, 2, -2, -1, 1, 2, 0, -1, 1, 0, 0])
y = np.array([0, 2, 2, 1, 0, 1,-1, -1,-1, -1, -2, -3, -3, -4,-5])


# Define the animation function
def animate(i):
    # Update the positions of the point lights
    global x, y
    x += 0.1*np.random.randn(15)
    y += 0.1*np.random.randn(15)
    
    #Check boundaries
    x = np.clip(x, -5, 5)
    y = np.clip(y, -5,5)

    # Clear the axes
    ax.cla()
    ax.set_xlim([-6,6])
    ax.set_ylim([-6,6])
    ax.set_facecolor('black')
    # Plot the point lights
    ax.scatter(x, y, s=50, c='white')
    # Remove axis ticks and labels
    ax.set_xticks([])
    ax.set_yticks([])


# Create the figure and axes
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50)

# Show the animation
plt.show()

