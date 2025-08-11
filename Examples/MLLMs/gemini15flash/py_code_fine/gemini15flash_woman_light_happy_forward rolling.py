
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5],  [1, 4], [2, 4], [3, 4],
    [0.5, 3], [1.5, 3], [2.5, 3],[3.5,3],
    [1, 2], [2, 2],
    [1.5, 1], [2.5, 1],
    [1.5, 0], [2.5, 0]
])


# Define the animation function
def animate(i):
    # Update the positions of the point-lights based on a rolling motion
    updated_positions = np.copy(initial_positions)
    angle = i * np.pi / 180 # Adjust speed by changing divisor (e.g., 180, 360 etc.)
    for j in range(len(updated_positions)):
        x_shift = 0.1 * np.sin(angle + j * 0.1) # Simulate a rolling motion with slight variations for each point
        y_shift = 0.2 + 0.1 * np.cos(angle + j * 0.2)
        updated_positions[j,0] += x_shift  
        updated_positions[j,1] += y_shift  

    # Plot the updated positions
    ax.clear()
    ax.scatter(updated_positions[:, 0], updated_positions[:, 1], s=50, color='white')
    ax.set_xlim([-2, 6])  # Adjust limits as necessary
    ax.set_ylim([-1, 7])   # Adjust limits as necessary
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_facecolor('black')

# Set up the figure and axes
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=360, interval=20, blit=False)  #frames = number of frames, interval= delay between frames in ms

# Show the animation (uncomment if you want to save the animation to a file)
#ani.save('rolling_motion.gif', writer='imagemagick', fps=30)


plt.show()

