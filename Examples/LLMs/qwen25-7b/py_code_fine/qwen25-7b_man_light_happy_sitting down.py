
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the point-lights
initial_positions = np.array([
    [50, 10), (65, 10), (75, 10), (85, 15), (95, 15),
    (45, 25), (55, 25), (65, 25), (75, 25), (85, 25),
    (55, 35), (65, 35), (75, 35), (65, 45), (75, 45)
])

# Define the function to update the positions of the point-lights
def update_positions(positions):
    # Simulate smooth and natural motion
    velocities = np.random.normal(0, 1, positions.shape)
    new_positions = positions + velocities
    new_positions[new_positions < 0] =  t
    new_positions[new_positions > 100] = 100
    return new_positions

# Initialize the figure and axis
fig, ax = plt.subplots()
axg = ax.imshow(np.zeros((100, 100)), cmap='gray')
points = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='w')

# Animation function
def animate(frame):
    global initial_positions
    initial_positions = update_positions(initial_positions)
    points.set_offsets(initial_positions)
    return points,

# Set up the animation
ani = FuncAnimation(fig, animate, frames=200, interval=20, blit=True)

# Show the plot
plt.axis('off
plt.show()
