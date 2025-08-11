
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_lights = 15

# Define the size of the animation
width, height = 800, 600

# Create a black background
fig, ax = plt.subplots(figsize=(width/100, height/100))
ax.set_xlim(-width/2, width/2)
ax.set_ylim(-height/2, height/2)
ax.set_facecolor('black')

# Create the point lights
point_lights = []
for i in range(num_lights):
    x = np.random.uniform(-width/2, width/2)
    y = np.random.uniform(-height/2, height/2)
    point_lights.append([x, y])

# Define the animation function
def animate(i):
    # Update the position of the point lights
    for light in point_lights:
        light[0] += np.random.uniform(-0.1, 0.1)
        light[1] += np.random.uniform(-0.1, 0.1)

    # Update the plot
    ax.clear()
    ax.scatter(*point_lights, s=10, c='white')
    return ax,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=10, blit=True)

# Show the animation
plt.show()
