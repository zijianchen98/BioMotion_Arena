
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
light_positions = np.zeros((num_lights, 2))

# Define the movement of each point light
light_movements = np.zeros((num_lights, 2))
light_movements[:, 0] = np.linspace(-0.5, 0.5, num_lights)
light_movements[:, 1] = np.sin(np.linspace(0, 2*np.pi, num_lights))

# Define the time step and total duration of the animation
dt = 0.01
total_time = 5

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_facecolor('black')
    
    # Update the positions of the point lights
    light_positions[:, 0] = light_movements[:, 0] * np.sin(i*dt)
    light_positions[:, 1] = light_movements[:, 1] * np.sin(i*dt)
    
    # Plot the point lights
    for light in light_positions:
        ax.plot(light[0], light[1], 'o', color='white', markersize=5)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=int(total_time/dt), interval=dt*1000, blit=False)

# Show the animation
plt.show()
