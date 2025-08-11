
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters of the animation
num_lights = 15
light_radius = 5
background_color = 'black'
light_color = 'white'

# Define the positions of the lights for a walking motion
def get_positions(t):
    # Define the joints of the walking motion
    joints = np.array([
        [-0.2, 0.0],  # left foot
        [0.2, 0.0],   # right foot
        [-0.2, 0.1],  # left ankle
        [0.2, 0.1],   # right ankle
        [-0.2, 0.2],  # left knee
        [0.2, 0.2],   # right knee
        [-0.2, 0.3],  # left hip
        [0.2, 0.3],   # right hip
        [-0.2, 0.4],  # left shoulder
        [0.2, 0.4],   # right shoulder
        [-0.2, 0.5],  # left elbow
        [0.2, 0.5],   # right elbow
        [-0.2, 0.6],  # left hand
        [0.2, 0.6],   # right hand
        [0.0, 0.0],   # head
    ])

    # Define the movement of the joints
    movement = np.sin(t)

    # Calculate the positions of the lights
    positions = joints + movement[:, np.newaxis] * np.array([
        [0.1, 0.0],  # left foot
        [0.1, 0.0],   # right foot
        [0.0, 0.1],  # left ankle
        [0.0, 0.1],   # right ankle
        [-0.1, 0.2],  # left knee
        [-0.1, 0.2],  # right knee
        [0.0, 0.3],  # left hip
        [0.0, 0.3],  # right hip
        [0.1, 0.4],  # left shoulder
        [0.1, 0.4],  # right shoulder
        [-0.1, 0.5],  # left elbow
        [-0.1, 0.5],  # right elbow
        [-0.1, 0.6],  # left hand
        [-0.1, 0.6],  # right hand
        [0.0, 0.0],   # head
    ])

    return positions

# Create a new figure
fig, ax = plt.subplots()

# Set the background color
ax.set_facecolor(background_color)

# Initialize the plot
lights = []
for i in range(num_lights):
    light, = ax.plot([], [], 'o', markersize=light_radius, color=light_color)
    lights.append(light)

# Initialize the plot limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Define the animation function
def animate(t):
    for i, light in enumerate(lights):
        light.set_data(get_positions(t)[i, 0], get_positions(t)[i, 1])
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 10*np.pi, 100), interval=50)

# Show the animation
plt.show()
