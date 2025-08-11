
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
points, = ax.plot([], [], 'wo', markersize=8)

# Define the initial positions of the point-lights
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


# Define the animation function
def animate(i):
    # Generate new positions based on a simple sine wave for each point
    new_positions = np.copy(initial_positions)
    
    # Simulate sitting down
    new_positions[:,1] -= 0.1*np.sin(i/10) 
    new_positions[:,0] += 0.05*np.sin(i/5)
    # Introduce some random noise for more natural movement
    new_positions += np.random.normal(scale=0.1, size=new_positions.shape)

    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Save the animation as an MP4 file
ani.save('biological_motion.mp4', writer='ffmpeg', fps=20)

# Show the plot (optional - you might want to comment this out if only saving the animation)
plt.show()

