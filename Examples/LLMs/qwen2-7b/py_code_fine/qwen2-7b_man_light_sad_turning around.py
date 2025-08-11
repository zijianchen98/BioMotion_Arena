
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the subject and action
subject = "sadman"
action = "turning around"

# Define the number of point-lights
num_point_lights = 15

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.axis('off')

# Define the initial positions of the point-lights
point_light_positions = np.random.rand(num_point_light, 2) * 100

# Define the radius of the point-lights
radius = 5

# Define the speed and direction of the point-lights
speed = 0.1
directions = np.random.rand(num_point_light, 2)

# Define the function to update the animation
def update(frame):
    # Update the positions of the point-lights
    for i in range(num_point_light):
        point_light_positions[is] += direction[is] * speed
        if point_light_positions[is][0] > 100 or point_light_positions[is][0] < 0:
            direction[is][0] *= -1
        if point_light_positions[is][1] > 100 or point_light_positions[is][1] < 0:
            direction[is][1] *= -1
        
        # Draw the point-lights
        circle = plt.Circle(point_light_positions[is], radius, color='white', fill=False)
        ax.add_patch(circle)
    
    return []

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), blit=True, interval=50)

# Show the animation
plt.show()
