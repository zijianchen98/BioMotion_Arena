
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()

# Define the number of lights and their initial positions
num_lights = 15
light_positions = np.random.uniform(-1, 1, num_lights)

# Define the animation function
def animate(i):
    global light_positions
    
    # Update the light positions to create the rolling motion
    light_positions = np.roll(light_positions, 1)
    
    # If the first light has moved past the edge, reset it to the end
    if light_positions[0] > 1:
        light_positions[0] = -1
    
    # Update the light positions on the plot
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.scatter(light_positions, np.zeros(num_lights), s=10, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=20)

# Show the animation
plt.show()
