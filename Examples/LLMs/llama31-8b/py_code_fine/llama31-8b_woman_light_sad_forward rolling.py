
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters of the animation
num_lights = 15
num_frames = 100
light_radius = 2
light_color = 'white'
background_color = 'black'

# Define the motion parameters
sadwoman_x = np.linspace(-3, 3, num_frames)
sadwoman_y = np.sin(np.linspace(0, 2*np.pi, num_frames))

# Define the light positions and velocities
light_positions = np.random.rand(num_lights, 2) * 6 - 3
light_velocities = np.random.rand(num_lights, 2) * 2 - 1

# Create a new figure
fig, ax = plt.subplots()

# Initialize the plot
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')
ax.set_facecolor(background_color)

# Initialize the lights
lights = []
for i in range(num_lights):
    light = ax.scatter(light_positions[i, 0], light_positions[i, 1], s=light_radius*2, color=light_color, alpha=0.5)
    lights.append(light)

# Function to update the plot
def update(frame):
    global light_positions
    global light_velocities
    
    # Update the light positions
    light_positions += light_velocities
    
    # Keep the lights within the plot boundaries
    for i in range(num_lights):
        if light_positions[i, 0] < -3:
            light_positions[i, 0] = -3
            light_velocities[i, 0] *= -1
        elif light_positions[i, 0] > 3:
            light_positions[i, 0] = 3
            light_velocities[i, 0] *= -1
        
        if light_positions[i, 1] < -3:
            light_positions[i, 1] = -3
            light_velocities[i, 1] *= -1
        elif light_positions[i, 1] > 3:
            light_positions[i, 1] = 3
            light_velocities[i, 1] *= -1
    
    # Update the light positions in the plot
    for i in range(num_lights):
        lights[i].set_offsets([light_positions[i, 0], light_positions[i, 1]])

    # Update the sadwoman position
    ax.clear()
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_aspect('equal')
    ax.set_facecolor(background_color)
    ax.scatter(sadwoman_x[frame], sadwoman_y[frame], s=light_radius*2, color='blue', alpha=0.5)
    
    # Update the light positions in the plot
    for i in range(num_lights):
        lights[i].set_offsets([light_positions[i, 0], light_positions[i, 1]])

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

# Show the animation
plt.show()
