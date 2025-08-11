
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters for the animation
num_points = 15
frames = 100
duration = 10  # Duration of the animation in seconds

# Setting up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(0, 20)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)  # White points

# Initial positions of points (simple standing form)
initial_positions = np.array([
    [-1, 1], [1, 1],
    [-2, 0], [0, 0], [2, 0],
    [-1, -1], [1, -1], [-3, -2], [3, -2],
    [-1, -3], [1, -3],
    [0, -5]  # Heavy weight position
])

# Animate function to update the points
def animate(frame):
    t = frame / frames
    walking_amplitude = 0.5 * np.sin(2 * np.pi * t)  # Swaying motion

    # Update positions for walking motion 
    updated_positions = initial_positions.copy()
    updated_positions[:, 1] += walking_amplitude  # Simulate walking by changing y

    # Update data in scatter plot
    points.set_data(updated_positions[:, 0], updated_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=1000/frames, blit=True)

# Show the animation
plt.title('Point-Light Animation of Sad Woman Walking with Heavy Weight')
plt.show()
