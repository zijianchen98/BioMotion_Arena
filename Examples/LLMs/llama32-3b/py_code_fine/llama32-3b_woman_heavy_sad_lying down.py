
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()

# Set the aspect ratio to be equal so the animation is not distorted
ax.set_aspect('equal')

# Set the background color to black
ax.set_facecolor('black')

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
light_positions = np.random.rand(num_lights, 2)

# Define the initial sizes of the point lights
light_sizes = np.random.rand(num_lights) * 0.1

# Define the initial orientations of the point lights
light_orientations = np.random.rand(num_lights, 2) * np.pi * 2 - np.pi

# Define the initial velocities of the point lights
light_velocities = np.random.rand(num_lights, 2) * 0.1

# Define the initial weights of the point lights
light_weights = np.random.rand(num_lights) * 0.1

# Define the function to update the point lights
def update(frame):
    global light_positions, light_sizes, light_orientations, light_velocities
    
    # Update the positions of the point lights
    light_positions += light_velocities
    
    # Ensure the point lights stay within the figure
    light_positions = np.clip(light_positions, 0, 1)
    
    # Update the sizes of the point lights
    light_sizes = np.random.rand(num_lights) * 0.1
    
    # Update the orientations of the point lights
    light_orientations += 0.01
    
    # Update the weights of the point lights
    light_weights = np.random.rand(num_lights) * 0.1
    
    # Clear the current axis
    ax.clear()
    
    # Set the background color to black
    ax.set_facecolor('black')
    
    # Plot the point lights
    for i in range(num_lights):
        # Calculate the x and y coordinates of the point light
        x = light_positions[i, 0] * light_weights[i]
        y = light_positions[i, 1] * light_weights[i]
        
        # Plot the point light
        ax.plot(x, y, 'w', markersize=light_sizes[i], marker='o', alpha=0.5)
        
        # Plot the line connecting the point light to the origin
        ax.plot([0, x], [0, y], 'w', alpha=0.5)
        
        # Plot the line connecting the point light to the previous position
        prev_x = light_positions[i-1, 0] * light_weights[i-1]
        prev_y = light_positions[i-1, 1] * light_weights[i-1]
        ax.plot([prev_x, x], [prev_y, y], 'w', alpha=0.5)
        
        # Plot the line connecting the point light to the next position
        next_x = light_positions[(i+1)%num_lights, 0] * light_weights[(i+1)%num_lights]
        next_y = light_positions[(i+1)%num_lights, 1] * light_weights[(i+1)%num_lights]
        ax.plot([next_x, x], [next_y, y], 'w', alpha=0.5)
        
        # Plot the line connecting the point light to the previous action position
        prev_action_x = light_positions[(i-1)%num_lights, 0] * light_weights[(i-1)%num_lights]
        prev_action_y = light_positions[(i-1)%num_lights, 1] * light_weights[(i-1)%num_lights]
        ax.plot([prev_action_x, x], [prev_action_y, y], 'w', alpha=0.5)
        
        # Plot the line connecting the point light to the next action position
        next_action_x = light_positions[(i+1)%num_lights, 0] * light_weights[(i+1)%num_lights]
        next_action_y = light_positions[(i+1)%num_lights, 1] * light_weights[(i+1)%num_lights]
        ax.plot([next_action_x, x], [next_action_y, y], 'w', alpha=0.5)
        
        # Plot the line connecting the point light to the origin, but only for the first and last point lights
        if i == 0:
            ax.plot([0, x], [0, y], 'w', alpha=0.5)
        elif i == num_lights-1:
            ax.plot([next_x, x], [next_y, y], 'w', alpha=0.5)

# Define the function to return the animation
def animate():
    return update

# Create the animation
ani = animation.FuncAnimation(fig, animate, interval=50)

# Show the animation
plt.show()
