
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the point lights
initial_positions = np.array([
    [0, 0],
    [-10, 10],
    [0, 10],
    [10,10],
    [-15, 15],
    [-5, 15],
    [5, 15],
    [15, 15],
    [-10, 20],
    [0, 20],
    [10, 20],
    [-5, 25],
    [5, 25],
    [-2.5, 30],
    [2.5, 30]

])

# Define the animation function
def animate(i):
    # Update the positions of the point lights based on time
    updated_positions = initial_positions.copy()

    #jumping animation
    updated_positions[:, 1] += 2*np.sin(i/10) 
    updated_positions[:, 0] +=  np.cos(i/10)
    

    # Plot the updated positions
    ln.set_offsets(updated_positions)
    return ln,

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-30, 30])
ax.set_ylim([-10, 50])
ax.set_aspect('equal')
ax.set_facecolor('black')  # Set background color to black

# Create the point lights
ln, = plt.plot([], [], 'wo', markersize=8)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Show the animation
plt.show()
