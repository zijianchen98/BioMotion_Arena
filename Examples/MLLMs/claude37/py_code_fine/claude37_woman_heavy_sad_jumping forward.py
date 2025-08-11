
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuration
num_points = 15  # Number of point lights
duration = 500  # Duration of animation in milliseconds
frames = 100  # Number of frames in the animation
jump_height = 0.4  # Height of the jump
jump_distance = 1.0  # Horizontal distance covered
fall_speed = 0.05  # Speed of descent

# Initialize figure
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_facecolor('black')

# Create empty points
points, = ax.plot([], [], 'o', color='white')

# Generate positions for the points (static positions)
positions = np.zeros((num_points, 2))
y_offsets = np.linspace(0.1, 0.2, num_points)
x_offsets = np.linspace(-0.1, 0.1, num_points)
positions[:, 0] = x_offsets
positions[:, 1] = y_offsets

# Animation function
def animate(frame):
    # Calculate the jump trajectory
    jump_progress = frame / (frames // 2)
    if frame < frames // 2:  # Ascending
        y_new = jump_height * (-4 * (jump_progress - 0.5)**2 + 1)  # Parabola
    else:  # Descending
        y_new = jump_height * (-4 * ((1 - jump_progress) - 0.5)**2 + 1)

    # Update positions
    positions[:, 1] += y_new - fall_speed if frame > frames // 2 else y_new
    positions[:, 0] += jump_distance / (frames // 2) if frame < frames // 2 else -jump_distance / (frames // 2)

    # Update point positions on plot
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=duration/frames, blit=True)

# Show animation
plt.show()
