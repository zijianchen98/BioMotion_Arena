
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the animation function
def animate(i):
    # Clear the previous frame
    ax.clear()

    # Set the background color to black
    ax.set_facecolor('black')

    # Set the axis limits
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])

    # Remove axis ticks and labels
    ax.set_xticks([])
    ax.set_yticks([])

    # Define the coordinates of the points for a bowing motion
    # These coordinates are based on a simplified skeleton of a person bowing
    if i < 50:  # Bowing down
        x = np.array([0, -2, 2, -4, 4, -2, 2, -1, 1, 0, -1, 1, -0.5, 0.5, 0])
        y = np.array([9, 7, 7, 5, 5, 3, 3, 1, 1, -1, -3, -3, -5, -5, -7]) - (i * 0.1)  # Lower the body
        x[5:7] = x[5:7] - (i * 0.02)  # Move arms slightly forward
        x[11:13] = x[11:13] - (i * 0.02)
    elif i < 100:  # Holding the bow
        x = np.array([0, -2, 2, -4, 4, -2, 2, -1, 1, 0, -1, 1, -0.5, 0.5, 0])
        y = np.array([9, 7, 7, 5, 5, 3, 3, 1, 1, -1, -3, -3, -5, -5, -7]) - 5  # Hold the lowered position
        x[5:7] = x[5:7] - 1  # Hold the arms forward
        x[11:13] = x[11:13] - 1
    else:  # Raising back up
        x = np.array([0, -2, 2, -4, 4, -2, 2, -1, 1, 0, -1, 1, -0.5, 0.5, 0])
        y = np.array([9, 7, 7, 5, 5, 3, 3, 1, 1, -1, -3, -3, -5, -5, -7]) - (5 - ((i-100) * 0.1)) # Raise the body back
        x[5:7] = x[5:7] - (1 - ((i-100) * 0.02)) # Move arms back
        x[11:13] = x[11:13] - (1 - ((i-100) * 0.02))
        if i >= 150: # Reset the animation after raising up
            i = 0

    # Plot the points as white dots
    ax.plot(x, y, 'wo', markersize=8)

    return

# Create the figure and axes
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50)

# Show the animation
plt.show()
