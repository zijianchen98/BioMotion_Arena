
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Create a new figure
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Define the number of point lights
num_lights = 15

# Define the position of each point light
light_positions = np.zeros((num_lights, 2))
light_positions[:, 0] = np.linspace(-1, 1, num_lights)
light_positions[:, 1] = np.linspace(-1, 1, num_lights)

# Define the initial position of the happyman
happyman_position = np.array([0, 0])

# Define the velocity of each point light
light_velocities = np.zeros((num_lights, 2))
light_velocities[:, 0] = np.random.uniform(-0.1, 0.1, num_lights)
light_velocities[:, 1] = np.random.uniform(-0.1, 0.1, num_lights)

# Define the radius of each point light
light_radius = 0.05

# Function to update the positions of the point lights
def update(i):
    global light_positions, happyman_position
    
    # Update the position of the happyman
    happyman_position[0] = np.sin(i / 10)
    happyman_position[1] = np.cos(i / 10)
    
    # Update the position of each point light
    light_positions[:, 0] += light_velocities[:, 0]
    light_positions[:, 1] += light_velocities[:, 1]
    
    # Keep the point lights within the boundaries
    light_positions = np.clip(light_positions, -1, 1)
    
    # Clear the previous frames
    ax.clear()
    ax.set_facecolor('black')
    
    # Draw the happyman
    happyman = patches.Circle(happyman_position, 0.2, edgecolor='white', facecolor='white', alpha=0.5)
    ax.add_patch(happyman)
    
    # Draw the point lights
    for position in light_positions:
        ax.plot(position[0], position[1], 'o', markersize=light_radius*20, markerfacecolor='white', markeredgecolor='white')
        
    # Set the limits of the axes
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect('equal')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(200), blit=False, interval=20)

# Show the animation
plt.show()
