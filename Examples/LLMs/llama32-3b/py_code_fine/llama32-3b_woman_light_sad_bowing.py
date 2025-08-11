
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# Define the figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Define the number of point lights
num_lights = 15

# Initialize the point lights
lights = np.zeros((num_lights, 3), dtype=np.float32)

# Define the action parameters
action = 'bowing'
action_params = {
    'action': action,
    'duration': 2,  # seconds
    'frame_rate': 30,
    'num_frames': int(action_params['duration'] * action_params['frame_rate']),
    'light_positions': np.random.uniform(-1, 1, size=(num_lights, 3)),  # random initial positions
    'light_sizes': np.random.uniform(0.01, 0.1, size=num_lights),  # random initial sizes
    'light_speeds': np.random.uniform(0.01, 0.1, size=num_lights),  # random initial speeds
}

# Initialize the animation
def init():
    ax.clear()
    ax.set_facecolor('black')
    return lights

# Update the point lights
def update(frame):
    global lights
    lights = np.zeros((num_lights, 3), dtype=np.float32)
    for i in range(num_lights):
        light_pos = lights[i]
        light_size = action_params['light_sizes'][i]
        light_speed = action_params['light_speeds'][i]
        if action == 'bowing':
            # Calculate the movement of the point light
            if frame % 10 == 0:
                light_pos[0] += light_speed
            if frame % 20 == 0:
                light_pos[1] += light_speed
            if frame % 30 == 0:
                light_pos[2] += light_speed
        lights[i] = light_pos

    # Draw the point lights
    ax.clear()
    ax.set_facecolor('black')
    for i in range(num_lights):
        ax.scatter(lights[i, 0], lights[i, 1], s=action_params['light_sizes'][i]*100, color='white')
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=action_params['num_frames'], init_func=init, interval=1000//action_params['frame_rate'])

plt.show()
