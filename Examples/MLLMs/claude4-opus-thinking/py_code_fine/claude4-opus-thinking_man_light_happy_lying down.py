
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point lights
num_points = 15

# Positions for the points approximating a man lying down
# Here, we use a simple approximation for a "happy man" lying down
initial_positions = np.array([
    [0, 3], [1, 4], [-1, 4],  # Head
    [0, 2], [1, 2], [-1, 2],  # Shoulders
    [0, 1], [0.5, 1], [-0.5, 1],  # Torso
    [0, 0], [0.5, 0], [-0.5, 0],  # Hips
    [0.2, -0.5], [-0.2, -0.5],  # Legs
])

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 4)
ax.set_facecolor('black')

# Create point light objects
points = [ax.plot([], [], 'o', color='white')[0] for _ in range(num_points)]

# Initialization function
def init():
    for point in points:
        point.set_data([], [])
    return points

# Animation function
def animate(i):
    # Update point positions to simulate motion
    offsets = np.array([
        np.sin(i / 10 + angle) * 0.1 for angle in np.linspace(0, np.pi, num_points)
    ])
    for j, point in enumerate(points):
        point.set_data(initial_positions[j, 0] + offsets[j], initial_positions[j, 1])
    return points

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
