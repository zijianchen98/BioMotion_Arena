
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)  # Set x-axis limits
ax.set_ylim(-1, 1)  # Set y-axis limits
ax.set_facecolor('black')  # Set background color
points, = ax.plot([], [], 'o', color='white')  # Points for the lights

# Initialize positions of the point lights
num_points = 15
# Initialize points for a lying down position
x_init = np.linspace(-2.5, 2.5, num_points)
y_init = np.zeros(num_points)

# Update function for the animation
def update(frame):
    # Define basic motion (smooth side-to-side wavy motion for realism)
    y_offset = np.sin(frame / 10) * 0.1  # Adjust the amplitude if needed
    y_positions = y_init + y_offset  # New y positions

    # Update points
    points.set_data(x_init, y_positions)
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), blit=True, interval=50)

# Show the animation
plt.show()
