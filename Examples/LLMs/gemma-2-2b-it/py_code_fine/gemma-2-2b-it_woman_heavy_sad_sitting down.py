
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

# Define the position of the point lights
light_positions = np.array([
    [width/2, height/2],
    [width/2 - 100, height/2],
    [width/2 + 100, height/2],
    [width/2, height/2 - 100],
    [width/2, height/2 + 100],
    [width/2 - 50, height/2 - 50],
    [width/2 + 50, height/2 - 50],
    [width/2 - 50, height/2 + 50],
    [width/2 + 50, height/2 + 50],
    [width/2 - 100, height/2 - 100],
    [width/2 + 100, height/2 - 100],
    [width/2 - 100, height/2 + 100],
    [width/2 + 100, height/2 + 100],
    [width/2 - 50, height/2 - 50],
    [width/2 + 50, height/2 - 50],
    [width/2 - 50, height/2 + 50],
    [width/2 + 50, height/2 + 50]
])

# Define the animation function
def animate(i):
    # Update the positions of the point lights
    for j in range(num_lights):
        light_positions[j] = np.array([
            light_positions[j][0] - 10 * np.sin(i * 0.01),
            light_positions[j][1] - 10 * np.cos(i * 0.01)
        ])
    
    # Update the plot
    ax.clear()
    ax.imshow(np.zeros((height, width, 3)))
    for j in range(num_lights):
        ax.plot(light_positions[j][0], light_positions[j][1], 'w', marker='o', markersize=5)
    
    return ax,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=10, blit=True)

# Show the animation
plt.show()
