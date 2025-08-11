
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the points
num_points = 15
points, = ax.plot([], [], 'wo', markersize=8)

# Define the initial positions of the points
initial_positions = np.array([
    [0, 5],
    [-1, 4],
    [0, 4],
    [1, 4],
    [-2, 3],
    [-1, 3],
    [0, 3],
    [1, 3],
    [2, 3],
    [-1, 2],
    [0, 2],
    [1, 2],
    [0, 1],
    [-0.5, 0],
    [0.5, 0]
])


# Animation function
def animate(i):
    # Define the positions of the points at time i
    t = i / 10.0  # Adjust the speed here
    positions = initial_positions.copy()


    #Jumping motion simulation (example)
    positions[:,1] += np.sin(t)*2 #Vertical jump
    positions[:,0] += np.cos(t) #Horizontal movement


    # Add some noise for a more natural look.  Comment out for less noisy animation.
    positions += np.random.normal(scale=0.1, size=positions.shape)

    # Update the plot data
    points.set_data(positions[:, 0], positions[:, 1])
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)


# Save the animation as a GIF (optional)

ani.save('biological_motion.gif', writer='pillow', fps=20)

# Show the animation
plt.show()

