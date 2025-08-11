
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the subject's initial position and velocity
initial_position = np.array([0, 0])
velocity = np.array([-0.1, -0.05])

# Create a figure and axis for the plot
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create 15 white point lights
point_lights = [plt.Circle((0, 0), 0.1, color='white') for _ in range(15)]
for light in point_lights:
    ax.add_artist(light)

def update(frame):
    global initial_position, velocity
    
    # Update the positions of the point lights
    for i, light in enumerate(point_lights):
        if i == 0:
            # Head of the happyman
            new_position = initial_position + velocity * frame
            light.center = new_position
        else:
            # Legs and body of the happyman
            angle = 2 * np.pi * i / len(point_lights)
            radius = 2 + 0.5 * np.sin(angle * 4)
            x = new_position[0] + radius * np.cos(angle)
            y = new_position[1] + radius * np.sin(angle)
            light.center = (x, y)
    
    # Update the initial position for the next frame
    initial_position += velocity
    
    return point_lights

ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()
