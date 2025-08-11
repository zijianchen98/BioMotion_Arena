
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
duration = 100  # Frames
fps = 30
x_range = (-1, 1)
y_range = (-1, 1)
z_range = (-0.5, 0.5)  # Adjust for realistic depth
speed = 0.2

# Initialize the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(x_range)
ax.set_ylim(y_range)
ax.set_zlim(z_range)
ax.axis('off')

# Create the point lights
lights = []
for _ in range(num_lights):
    light = plt.scatter([], [], s=50, color='white')
    lights.append(light)

# Define the running motion
def running_motion(frame):
    for i in range(num_lights):
        # Generate random starting positions
        x = np.random.uniform(x_range[0], x_range[1])
        y = np.random.uniform(y_range[0], y_range[1])
        z = np.random.uniform(z_range[0], z_range[1])

        # Calculate the movement
        x += speed * np.cos(frame * 0.1)
        y += speed * np.sin(frame * 0.1)
        z += speed * 0.1 * frame #add some z movement for realism

        # Keep lights within the bounds
        x = np.clip(x, x_range[0], x_range[1])
        y = np.clip(y, y_range[0], y_range[1])
        z = np.clip(z, z_range[0], z_range[1])
        
        # Update the light positions
        lights[i].set_offsets([x, y, z])

# Create the animation
ani = animation.FuncAnimation(fig, running_motion, frames=duration, blit=True, repeat=True)

# Save the animation (optional)
# ani.save("sadman_running.gif", writer='pillow', fps=fps)

plt.show()
