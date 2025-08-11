
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
duration = 100  # Total duration of animation in frames
rolls = 3  # Number of forward rolls in the animation

# Generate point-light positions (initial positions)
# Mimicking a sad woman rolling forward
points_y = np.linspace(2, -7, num_points)  # Vertical position of point lights
points_x = np.zeros(num_points)  # Starting horizontal positions (at center)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-8, 3)
ax.set_facecolor('black')
ax.axis('off')  # Turn off the axis

# Initialize the points as white dots
points, = ax.plot(points_x, points_y, 'o', color='white')

# Animation function
def update(frame):
    # Calculate new positions based on an upwards and forwards translation
    offset = frame * (10 / duration)  # Total distance covered during the animation
    angled_offset = np.sin(np.pi * frame / duration)  # Simulate rolling motion
    points.set_data(points_x + angled_offset, points_y - offset / rolls)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=duration, interval=50, blit=True)

# Display the animation
plt.show()
