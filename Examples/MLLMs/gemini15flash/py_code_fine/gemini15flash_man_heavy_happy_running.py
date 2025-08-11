
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


# Animation function
def animate(i):
    # Define the movement of the point-lights (replace with your desired motion)
    dt = 0.1  # Adjust for animation speed
    x = initial_positions[:, 0] + np.sin(i * dt) * 2 + np.random.normal(0,0.1,15) #Adding some noise
    y = initial_positions[:, 1] + i * dt - np.cos(i * dt) * 2 + np.random.normal(0,0.1,15) #Adding some noise


    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=20, blit=True)

# Save the animation as a GIF (optional)
# ani.save('biological_motion.gif', writer='imagemagick')

# Show the animation
plt.show()

