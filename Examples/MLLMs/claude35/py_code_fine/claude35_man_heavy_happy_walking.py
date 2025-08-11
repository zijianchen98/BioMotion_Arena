
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15  # Number of point lights
duration = 10  # Duration of the animation in seconds
frames_per_second = 30  # FPS
total_frames = duration * frames_per_second

# Initialize figure
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')

# Create 15 white points
points, = ax.plot([], [], 'o', color='white')

# Define walking motion parameters
def walking_motion(frame):
    # Generate walking path with a sinusoidal function for smooth motion
    x_positions = np.linspace(-0.5, 0.5, num_points)
    y_positions = np.sin(np.linspace(0, 10 * np.pi, num_points) + frame * 0.2) / 2 - 0.5

    # Update the y positions to simulate walking
    y_positions += (frame // (total_frames // 10)) * 0.1  # Simulate walking progress
    return x_positions, y_positions

# Animation function
def update(frame):
    x, y = walking_motion(frame)
    points.set_data(x, y)
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=total_frames, blit=True, interval=1000/frames_per_second)

# Show the animation
plt.show()
