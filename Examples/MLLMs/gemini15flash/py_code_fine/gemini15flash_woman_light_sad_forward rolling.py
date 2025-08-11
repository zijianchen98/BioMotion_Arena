
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-5, 5])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the points
num_points = 15
points, = ax.plot([], [], 'wo', markersize=10)

# Define the initial positions of the points.  These are arbitrary and will need to be adjusted for a realistic rolling motion.
initial_positions = np.array([
    [0, 5],
    [-1, 4], [0, 4], [1, 4],
    [-1.5, 3], [-0.5, 3], [0.5, 3], [1.5, 3],
    [-1, 2], [0, 2], [1, 2],
    [-0.5, 1], [0.5, 1],
    [0, 0]
])

# Animation function
def animate(i):
    #Simulate rolling motion.  This is a VERY simplified example and will need significant refinement for a realistic animation.
    dt = 0.1
    angular_velocity = 0.2
    
    rotated_positions = np.copy(initial_positions)
    rotated_positions[:,0] = initial_positions[:,0] * np.cos(angular_velocity*i*dt) - initial_positions[:,1] * np.sin(angular_velocity*i*dt)
    rotated_positions[:,1] = initial_positions[:,0] * np.sin(angular_velocity*i*dt) + initial_positions[:,1] * np.cos(angular_velocity*i*dt)
    
    # Add linear velocity (rolling forward)
    linear_velocity = 0.5
    rotated_positions[:,1] -= linear_velocity * i * dt

    points.set_data(rotated_positions[:,0], rotated_positions[:,1])
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Save the animation (optional)
ani.save('biological_motion.gif', writer='pillow', fps=20)


plt.show()
