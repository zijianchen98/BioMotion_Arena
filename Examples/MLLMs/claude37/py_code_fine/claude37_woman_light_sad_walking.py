
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point lights
num_points = 15

# Define the point lights for the figure of a walking woman
def get_points(frame):
    # This generates a simple walking motion
    # The y-coordinates represent both the legs and body's movement over time
    y_positions = np.array([-1, -1, -0.5, -0.5, 0, 0, 0.5, 0.5, 1, 1, 1.5, 1.5, 2, 2, 2.5])
    x_offset = 0.1 * np.sin(frame / 10)  # Simulate a slight side-to-side motion

    return x_offset * np.ones(num_points), y_positions + frame * 0.02  # Upward motion

# Create the figure
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')
ax.axis('off')  # Hide axes

# Create a scatter plot for the point lights
points, = ax.plot([], [], 'o', color='white')

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Animation function
def animate(frame):
    x_data, y_data = get_points(frame)
    points.set_data(x_data, y_data)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, init_func=init,
                              interval=50, blit=True)

# Display the animation
plt.show()
