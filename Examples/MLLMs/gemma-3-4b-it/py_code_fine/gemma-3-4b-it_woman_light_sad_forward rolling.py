
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the action and subject
action = "forward rolling"
subject = "sadwoman"  # Placeholder - visualization doesn't require a specific subject

# Define the number of lights
num_lights = 15

# Define the animation parameters
duration = 100  # Frames
fps = 30
fig_size = (8, 8)

# Create the figure and axes
fig, ax = plt.subplots(figsize=fig_size)
ax.set_facecolor("black")
ax.set_xticks([])
ax.set_yticks([])
ax.axis("off")

# Initialize the lights
lights = []
for _ in range(num_lights):
    light = plt.Point2D(np.random.rand() - 0.5, np.random.rand() - 0.5)
    lights.append(light)

# Define the motion function
def motion_function(frame):
    for light in lights:
        # Simulate forward rolling motion
        light.x += 0.01 * np.sin(frame / 10)
        light.y -= 0.01 * np.cos(frame / 10)
        light.y += 0.005 * frame
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, motion_function, frames=duration, blit=True, repeat=True)

# Save the animation
ani.save("sadwoman_forward_roll.gif", writer='pillow', fps=fps)

plt.close(fig)
