
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
rotation_speed = 0.1
duration = 400  # milliseconds
frames = 60

# Define point-light positions (simple arrangement)
def get_point_light_positions(t):
    theta = np.linspace(0, 2 * np.pi, num_points//3)
    r = 1.0  # Radius for positioning
    positions = []

    # Upper Body
    for angle in theta:
        x = r * np.cos(angle + t * rotation_speed)
        y = r * np.sin(angle + t * rotation_speed + np.pi/2)
        positions.append((x, y))

    # Lower Body
    for angle in theta:
        x = r * np.cos(angle + t * rotation_speed)
        y = r * np.sin(angle + t * rotation_speed + np.pi)
        positions.append((x, y))

    # Central Point
    positions.append((0, 0))

    return np.array(positions)

# Set up figure
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)  # white points

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Update function for animation
def update(frame):
    positions = get_point_light_positions(frame)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames,
                              init_func=init, blit=True, interval=duration/frames)

# Display the animation
plt.show()
