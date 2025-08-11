
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters for the animation
num_frames = 100  # Number of frames in the animation
interval = 40  # Delay between frames in milliseconds
point_lights = 15  # Number of point lights

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim([-100, 100])
ax.set_ylim([-100, 100])
ax.set_facecolor('black')

# Create an empty list to hold the point lights
point_lights_list = []

# Function to initialize the point lights
def init():
    for _ in range(point_lights):
        x = np.random.uniform(-50, 50)
        y = np.random.uniform(-50, 50)
        point_light = plt.Circle((x, y), radius=1, color='white')
        ax.add_artist(point_light)
        point_lights_list.append(point_light)

# Function to update the positions of the point lights
def update(frame):
    for i, point_light in enumerate(point_lights_list):
        # Update the position of each point light to simulate walking motion
        if frame % 2 == 0:
            point_light.center = (point_light.center[0] + 1, point_light.center[1] - 1)
        else:
            point_light.center = (point_light.center[0] + 1, point_light.center[1] + 1)
        
        # Apply additional movement to simulate the carrying of a heavy weight
        if i % 3 == 0:
            point_light.center = (point_light.center[0], point_light.center[1] - 1)
        elif i % 3 == 1:
            point_light.center = (point_light.center[0], point_light.center[1] + 1)
        elif i % 3 == 2:
            pass

# Call the init function once before the animation starts
init()

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=interval)

# Display the animation
plt.show()
