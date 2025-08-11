
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def init():
    for point in point_lights:
        point.set_visible(False)
    return point_lights

def animate(i):
    for idx, point in enumerate(point_lights):
        x, y = positions[:, idx, i]
        point.set_data(x, y)
        point.set_visible(True)
    return point_lights

# Parameters
frames = 100
interval = 40  # ms, controls the speed of animation

# Generate synthetic data for point lights
np.random.seed(42)
num_lights = 15
positions = np.random.randn(2, num_lights, frames)  # [x, y] coordinates for each point light over frames

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')

# Initialize the point lights
point_lights = [ax.plot([], [], 'w.')[0] for _ in range(num_lights)]

# Create the animation
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, interval=interval, blit=True)

# Display the animation
plt.close(fig)  # Prevent the initial figure from showing
plt.show()
