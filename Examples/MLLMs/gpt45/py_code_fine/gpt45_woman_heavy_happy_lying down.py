
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Number of points
num_points = 15

# Initialize positions of 15 point lights
# Example positions for a jumping motion
initial_positions = np.array([
    [4.5, 0],  # Center Point (Body)
    [4, 1], [5, 1],  # Shoulders
    [3.5, 2], [4.5, 2], [5.5, 2],  # Elbows
    [3, 3], [4.5, 3], [6, 3],  # Hands
    [4.5, -1], [3.5, -2], [5.5, -2],  # Hips
    [3, -3], [4.5, -3], [6, -3]  # Knees and Feet
])

# Movement patterns to simulate jumping
def jump_motion(frame):
    # Clear previous points
    moving_positions = np.copy(initial_positions)

    # Simulated jumping motion
    vertical_offset = np.abs(np.sin(frame / 10)) * 2  # Simulate upward motion
    forward_offset = frame / 10  # Simulate forward motion

    # Update positions
    moving_positions[:, 0] += forward_offset  # Move forward
    moving_positions[:, 1] += vertical_offset  # Move up and down

    points.set_data(moving_positions[:, 0], moving_positions[:, 1])

    return points,

# Create an animation
ani = animation.FuncAnimation(fig, jump_motion, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
