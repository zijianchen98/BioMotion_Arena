
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Define the parameters
num_lights = 15
action = 'lying down'
subject ='sadman'
weight = 'heavy'
background_color = 'black'

# Define the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the point lights
lights = []
for i in range(num_lights):
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    z = np.random.uniform(-1, 1)
    lights.append([x, y, z])

# Define the motion
motion = np.zeros((num_lights, 3))

# Define the initial position
initial_position = np.array([0, 0, 0])

# Define the movement
movement = np.array([0, 0, 0])

# Define the animation function
def animate(i):
    global motion, movement
    
    # Update the movement
    movement += 0.01 * np.array([np.cos(i/10), np.sin(i/10), np.cos(i/10)])
    
    # Update the position of the lights
    for j in range(num_lights):
        lights[j][0] = initial_position[0] + movement[0]
        lights[j][1] = initial_position[1] + movement[1]
        lights[j][2] = initial_position[2] + movement[2]
        motion[j] = lights[j]
        
    # Clear the axis
    ax.clear()
    
    # Plot the background
    ax.set_facecolor(background_color)
    
    # Plot the lights
    for light in lights:
        ax.scatter(light[0], light[1], light[2], color='white', s=10)

# Define the initial position of the lights
initial_position = np.array([0, 0, 0])

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50)

# Show the animation
plt.show()
