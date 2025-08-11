
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point lights
num_points = 15

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 800)
ax.set_ylim(0, 800)
ax.set_axis_off()

# Define the initial position of each point light
points = np.array([np.random.randint(0, 800, num_points),
                   np.random.randint(0, 800, num_points)]).T

# Animation initialization
def init():
    ax.set_xlim(0, 800)
    ax.set_ylim(0, 800)

# Animation update function
def update(frame_count):
    global points

    # Define the motion parameters for the lying down animation
    speed = 0.05
    x_offset = 0.5 * speed * frame_count
    y_shift = 0.3 * speed * frame_count

    for i in range(num_points):
        dx = 0
        if frame_count < 240:
            dx = 0.15 * speed * frame_count
        else:
            dx = -0.15 * speed * (frame_count - 240)

        points[0, i] += dx + x_offset
        points[1, i] = int(400 - y_shift * (i + 1))

    return [plt.Circle(points[i], 3, color='white', alpha=0.5) for i in range(num_points)]

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=300, init_func=init, blit=True)

# Display the animation
plt.show()
