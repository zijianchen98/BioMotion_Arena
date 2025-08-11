
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
points, = ax.plot([], [], 'wo', markersize=10)

# Define the initial positions of the points
initial_positions = np.array([
    [0, 5],
    [-1, 4],
    [1, 4],
    [-2, 3],
    [0, 3],
    [2, 3],
    [-2.5, 2],
    [-1.5, 2],
    [0, 2],
    [1.5, 2],
    [2.5, 2],
    [-1, 1],
    [1, 1],
    [-0.5, 0],
    [0.5, 0]
])


# Function to update the points' positions for each frame
def animate(i):
    # Simulate jumping motion (example - replace with more realistic motion)
    dt = 0.1
    gravity = -0.5
    jump_height = 5
    jump_duration = 2

    t = i * dt
    if t < jump_duration:
        y = jump_height * np.sin(np.pi * t / jump_duration) + 0.5 * gravity * t**2
        # Apply the jump to the y-coordinate of the body points
        updated_positions = initial_positions.copy()
        updated_positions[:,1] += y
    else:
        updated_positions = initial_positions

        
    points.set_data(updated_positions[:, 0], updated_positions[:, 1])
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50, blit=True)

# Show the animation
plt.show()

