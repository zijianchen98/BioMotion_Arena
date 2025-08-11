
import matplotlib.pyplot as plt
import numpy as np

# Define the radius of the circle and the number of points
radius = 400
num_points = 15

# Define the number of frames
frames = 100

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim([0, radius])
ax.set_ylim([0, radius])

# Remove axes
ax.axis('off')

# Initialize the positions of the points
positions = np.random.uniform(-radius/2, radius/2, (frames, num_points, 2))

# Animation function
def animate(i):
    # Update the positions based on simple acceleration and deceleration
    acceleration = 0.03 * np.sin(positions[:, i % 50, 0] / radius) - 0.03 * np.sin(positions[:, i % 50, 1] / radius)
    deceleration = 0.005 * np.sin(positions[:, i % 50, 0] / radius) + 0.005 * np.sin(positions[:, i % 50, 1] / radius)
    positions[:, i % 50, :] += 0.001 * (acceleration + positions[:, i % 50, :]) * (i % 50 < frames // 30) - 0.001 * (deceleration + positions[:, i % 50, :]) * (i % 50 >= frames // 30)

    # Clear the previous plot
    ax.clear()

    # Create a circle for the background
    circle = plt.Circle((0, 0), radius, color='black')
    ax.add_artist(circle)

    # Plot the points
    ax.plot(positions[:, i % 50, 0], positions[:, i % 50, 1], 'wo', markersize=2)

# Animate the points-light stimulus
ani = plt animations.FuncAnimation(fig, animate, frames=frames, interval=10)
plt.show()
