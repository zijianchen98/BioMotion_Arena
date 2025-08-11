
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
light_positions = np.zeros((num_lights, 2))

# Define the target positions of the point lights for each frame
target_positions = np.zeros((num_lights, 2))

# Define the movement parameters
jump_height = 1.5  # meters
jump_distance = 2.0  # meters
num_frames = 100
frame_rate = 30

# Define the animation function
def animate(i):
    global light_positions
    global target_positions
    
    # Update the target positions based on the current frame
    if i < num_frames // 4:
        target_positions[:, 0] = np.linspace(-jump_distance, jump_distance, num_lights)
        target_positions[:, 1] = np.zeros(num_lights)
    elif i < num_frames // 2:
        target_positions[:, 0] = jump_distance
        target_positions[:, 1] = np.linspace(0, jump_height, num_lights)
    elif i < 3 * num_frames // 4:
        target_positions[:, 0] = np.linspace(jump_distance, -jump_distance, num_lights)
        target_positions[:, 1] = np.linspace(jump_height, 0, num_lights)
    else:
        target_positions[:, 0] = np.zeros(num_lights)
        target_positions[:, 1] = np.linspace(0, -jump_height, num_lights)
    
    # Update the light positions
    light_positions = target_positions
    
    # Clear the current axes
    ax.clear()
    
    # Set the limits of the axes
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    
    # Set the aspect ratio of the axes to be equal
    ax.set_aspect('equal')
    
    # Plot the point lights
    ax.scatter(light_positions[:, 0], light_positions[:, 1], s=50, c='white')

# Create a new figure
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=1000 // frame_rate, repeat=False)

# Show the animation
plt.show()
