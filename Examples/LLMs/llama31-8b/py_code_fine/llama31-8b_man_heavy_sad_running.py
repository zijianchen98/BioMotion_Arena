
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_lights = 15

# Define the position of each point light
lights_x = np.array([
    0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.9, 0.8, 0.7, 0.6
])
lights_y = np.array([
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.1, -0.2, -0.3, -0.4
])

# Define the radius of each point light
light_radius = 0.05

# Define the animation parameters
num_frames = 100
frame_rate = 30

# Create a new figure
fig, ax = plt.subplots()

# Initialize the plot with a black background
ax.set_facecolor('black')

# Initialize the point lights
light_scatter = ax.scatter(lights_x, lights_y, s=light_radius*200, c='white')

# Initialize the axis limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Initialize the axis ticks
ax.set_xticks([])
ax.set_yticks([])

# Function to update the plot for each frame
def update(frame):
    # Calculate the phase of each point light
    phase = np.linspace(0, 2*np.pi, num_frames, endpoint=False)[frame % num_frames]

    # Calculate the x and y coordinates of each point light
    lights_x_new = lights_x + np.cos(phase)
    lights_y_new = lights_y + np.sin(phase)

    # Update the point lights
    light_scatter.set_offsets(np.column_stack((lights_x_new, lights_y_new)))

    # Return the updated plot
    return light_scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, interval=1000/frame_rate)

# Display the animation
plt.show()
