
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
num_lights = 15

# Define the initial positions of the point-lights
initial_positions = np.random.rand(num_lights, 2)

# Define the movement parameters
speed = 0.02
angle = np.linspace(0, 2*np.pi, num_lights)

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create the point-lights
lights = [ax.plot([], [], 'o', color='white')[0] for _ in range(num_lights)]

def update(frame):
    # Update the positions of the point-lights
    for i in range(num_lights):
        x = initial_positions[i, 0] + speed * frame * np.cos(angle[i])
        y = initial_positions[i, 1] + speed * frame * np.sin(angle[i])
        
        # Wrap around the edges
        if x > 1:
            x -= 1
        elif x < 0:
            x += 1
        
        if y > 1:
            y -= 1
        elif y < 0:
            y += 1
        
        lights[i].set_data([x], [y])
    
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Show the animation
plt.show()
