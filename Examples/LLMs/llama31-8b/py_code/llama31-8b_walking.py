
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Define the figure and axis
fig, ax = plt.subplots()

# Define the background color
ax.set_facecolor('black')

# Define the point-light properties
num_lights = 15
light_radius = 2
light_color = 'white'

# Define the initial positions of the point-lights
lights = []
for i in range(num_lights):
    light_x = np.sin(i * np.pi / num_lights) * 50 + 100
    light_y = np.cos(i * np.pi / num_lights) * 50 + 100
    lights.append([light_x, light_y])

# Define the movement parameters
num_frames = 100
fps = 30
duration = num_frames / fps

# Define the movement function
def movement(frame):
    # Update the positions of the point-lights
    for i in range(num_lights):
        light_x = np.sin((i * np.pi / num_lights) + frame / 10) * 50 + 100
        light_y = np.cos((i * np.pi / num_lights) + frame / 10) * 50 + 100
        lights[i] = [light_x, light_y]
    
    # Clear the previous frame
    ax.clear()
    ax.set_facecolor('black')
    
    # Plot the point-lights
    for light in lights:
        ax.add_patch(patches.Circle(light, light_radius, facecolor=light_color, edgecolor='black'))
    
    # Set the axis limits
    ax.set_xlim(0, 200)
    ax.set_ylim(0, 200)
    
    # Remove the axis ticks and frames
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)

# Create the animation
ani = animation.FuncAnimation(fig, movement, frames=num_frames, interval=1000 / fps, repeat=False)

# Show the animation
plt.show()
