
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Define the figure and axis
fig, ax = plt.subplots()

# Define the background color
ax.set_facecolor('black')

# Define the point lights
lights = []
for i in range(15):
    x = np.linspace(-0.2, 0.2, 100)
    y = np.linspace(-0.2, 0.2, 100)
    x, y = np.meshgrid(x, y)
    z = np.zeros_like(x)
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    x_light = 0.3 * np.cos(theta + i * np.pi / 15)
    y_light = 0.3 * np.sin(theta + i * np.pi / 15)
    light, = ax.plot(x + x_light, y + y_light, color='white', lw=2)
    lights.append(light)

# Define the happy woman's body
body = patches.Rectangle((-0.4, -0.4), 0.8, 0.8, color='white', alpha=0.5)
ax.add_patch(body)

# Set the axis limits
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 0.5)
ax.set_aspect('equal')

# Initialize the animation
def animate(i):
    # Update the point lights' positions
    for j, light in enumerate(lights):
        x_light = 0.3 * np.cos(i * np.pi / 60 + j * np.pi / 15)
        y_light = 0.3 * np.sin(i * np.pi / 60 + j * np.pi / 15)
        light.set_data(x + x_light, y + y_light)

    # Update the happy woman's body position
    body.set_xy((-0.4 + 0.2 * np.sin(i * np.pi / 60), -0.4 + 0.2 * np.cos(i * np.pi / 60)))

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=120, blit=False, interval=20)

# Show the animation
plt.show()
