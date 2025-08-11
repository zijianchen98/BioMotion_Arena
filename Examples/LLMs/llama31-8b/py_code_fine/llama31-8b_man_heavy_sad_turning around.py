
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters
num_lights = 15
light_radius = 5
background_color = 'black'
light_color = 'white'
frame_rate = 30
duration = 2  # seconds

# Create a figure and axis
fig, ax = plt.subplots()

# Define the initial positions of the lights
light_positions = np.zeros((num_lights, 2))
light_positions[:, 0] = np.random.uniform(-100, 100, num_lights)
light_positions[:, 1] = np.random.uniform(-100, 100, num_lights)

# Define the movement of the lights
def move_lights(frame):
    global light_positions
    angle = np.radians(360 * frame / (frame_rate * duration))
    center_x = 0
    center_y = 0
    radius = 100
    for i in range(num_lights):
        light_x = center_x + radius * np.cos(angle + i * np.pi * 2 / num_lights)
        light_y = center_y + radius * np.sin(angle + i * np.pi * 2 / num_lights)
        light_positions[i, 0] = light_x
        light_positions[i, 1] = light_y
    ax.clear()
    ax.set_facecolor(background_color)
    ax.scatter(light_positions[:, 0], light_positions[:, 1], s=light_radius * 2, c=light_color)

# Create the animation
ani = animation.FuncAnimation(fig, move_lights, frames=int(frame_rate * duration), interval=1000 // frame_rate)

plt.show()
