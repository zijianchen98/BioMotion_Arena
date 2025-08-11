
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')
ax.axis('off')

# Define initial coordinates of points (15 points)
initial_points = np.array([
    [4, 8], [5, 8], [6, 8],  # Head
    [3, 7], [4, 7], [5, 7], [6, 7], [7, 7],  # Upper body
    [4, 6], [6, 6],  # Shoulders
    [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5],  # Lower body
    [5, 4], [6, 4]  # Feet
])

# Function to update the positions of points
def update(frame):
    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_facecolor('black')
    ax.axis('off')

    # Calculate displacement for jumping motion
    amplitude = 0.5
    offset = 0.2
    height = 1 - np.cos(2 * np.pi * frame / 30) * amplitude + offset

    # Move forward
    shift = frame / 30 * 0.2

    # Update positions
    new_points = initial_points + np.array([shift, -height])

    # Draw the new points
    for point in new_points:
        circle = plt.Circle(point, 0.1, color='white')
        ax.add_artist(circle)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=60, repeat=True)

# Display the animation
plt.show()
