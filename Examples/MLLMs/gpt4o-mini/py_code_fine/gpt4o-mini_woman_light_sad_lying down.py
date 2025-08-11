
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters for the figure
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
point_lights, = plt.plot([], [], 'o', color='white')

# Define the initial positions of the point-lights to mimic a lying down woman
num_points = 15
# Define "lying down" pose with y-coordinates reflecting that position
x_positions = np.array([-0.5, -0.3, -0.1, 0.1, 0.3, 0.5] * 2 + [0])  # Centers on the Y-axis
y_positions = np.array([-1, -0.9, -1.1, -1.0, -0.9, -1])  # Variation to give a "lying down" look
y_positions = np.tile(y_positions, 2)
y_positions[-1] = -1.5  # Center point at bottom for balance

# Initialize positions for animation
points = np.array([[x, y] for x, y in zip(x_positions, y_positions)])

def init():
    point_lights.set_data([], [])
    return point_lights,

def animate(frame):
    # Create a slight oscillation effect to simulate breathing
    oscillation = 0.05 * np.sin(0.1 * frame)
    new_y = points[:, 1] + oscillation
    point_lights.set_data(points[:, 0], new_y)
    return point_lights,

# Create animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=50, blit=True)

# Show the animation
plt.show()
