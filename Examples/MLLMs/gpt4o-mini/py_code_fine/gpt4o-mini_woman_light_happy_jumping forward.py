
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point lights
num_points = 15

# Initial positions (y-values) of the point lights
y_initial_positions = np.array([
    1.5, 1.0, 1.5,  # Head 
    0.5, 0.5, 0.5, 0.5,  # Shoulders
    0.0, 0.0, 0.0, 0.0,  # Hips
    -0.5, -0.5, -0.5,  # Knees
    -1.0, -1.0,  # Feet
])

# x positions: These will change to animate the jumping
x_positions = np.zeros(num_points)

# Define the limits for the plot
x_lim = (-2, 2)
y_lim = (-2, 2)

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(x_lim)
ax.set_ylim(y_lim)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)  # White points

def init():
    points.set_data([], [])
    return points,

def animate(i):
    # Define a smooth forward jump motion
    if i < 30:
        # Jump up
        y_positions = y_initial_positions + (i / 30.0) * 1.5
    elif i < 60:
        # Coming down
        y_positions = y_initial_positions + 1.5 - ((i - 30) / 30.0) * 1.5
    else:
        # Rest position
        y_positions = y_initial_positions

    # Update x positions to simulate forward motion
    x_positions += 0.05  # Move forward gradually
    points.set_data(x_positions, y_positions)
    return points,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=90, init_func=init, blit=True, interval=50)

plt.show()
