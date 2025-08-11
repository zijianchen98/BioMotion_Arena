
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()

# Set the axis limits and background color
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_axis_off()
ax.set_facecolor('black')

# Define the number of point-lights
num_lights = 15

# Define the point-light positions and colors
light_positions = np.random.uniform(-1, 1, size=(num_lights, 2))
light_colors = np.ones((num_lights, 4))

# Define the jumping action parameters
jump_height = 1.5
jump_duration = 2
num_frames = 50

# Define the animation function
def animate(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_axis_off()
    ax.set_facecolor('black')
    
    # Update the point-light positions based on the jumping action
    time = frame / num_frames * jump_duration
    y_positions = np.sin(time * 2 * np.pi / jump_duration) * jump_height + 0.5
    x_positions = np.cos(time * 2 * np.pi / jump_duration) * jump_height + 0.5
    
    # Update the point-light positions and colors
    for i in range(num_lights):
        ax.plot(light_positions[i, 0], y_positions[i], 'o', color=light_colors[i])
        ax.plot(x_positions[i], y_positions[i], 'o', color=light_colors[i])
    
    # Add the sadwoman's body
    ax.plot([0, 0], [0, 0.5], 'o-', color='white')
    ax.plot([0.5, 0.5], [0.5, 0.7], 'o-', color='white')
    ax.plot([0.5, 1], [0.7, 0.7], 'o-', color='white')
    ax.plot([1, 1], [0.7, 0.5], 'o-', color='white')
    
# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50)

# Show the animation
plt.show()
