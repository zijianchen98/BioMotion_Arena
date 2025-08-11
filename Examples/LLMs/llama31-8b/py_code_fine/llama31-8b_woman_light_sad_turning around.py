
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters
num_lights = 15
num_frames = 100
light_radius = 2
background_color = 'black'
light_color = 'white'

# Define the positions of the lights
light_positions = np.random.rand(num_lights, 2) * 2 - 1  # Random positions between -1 and 1

# Define the angles for rotation
angles = np.linspace(0, 2 * np.pi, num_frames)

# Create a new figure
fig, ax = plt.subplots()

# Set the background color
ax.set_facecolor(background_color)

# Initialize the plot
def init():
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    return ax.scatter([], [])

# Animate the plot
def animate(i):
    ax.clear()
    ax.set_facecolor(background_color)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    
    # Rotate the lights
    for j in range(num_lights):
        x = light_positions[j, 0] * np.cos(angles[i]) - light_positions[j, 1] * np.sin(angles[i])
        y = light_positions[j, 0] * np.sin(angles[i]) + light_positions[j, 1] * np.cos(angles[i])
        ax.scatter(x, y, color=light_color, s=light_radius*light_radius)
    
    return ax.scatter([], [])

ani = animation.FuncAnimation(fig, animate, frames=num_frames, init_func=init, blit=False, interval=50)

plt.show()
