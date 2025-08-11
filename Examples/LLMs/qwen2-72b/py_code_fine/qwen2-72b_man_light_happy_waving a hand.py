
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the number of point-lights
num_lights = 15

# Define the size of the figure
fig, ax = plt.subplots(figsize=(6, 6))

# Set the background color to black
ax.set_facecolor('black')

# Remove the axis labels and ticks
ax.axis('off')

# Initialize the point-lights
lights = [plt.Circle((np.random.rand(), np.random.rand()), 0.02, color='white') for _ in range(num_lights)]

# Add the point-lights to the plot
for light in lights:
    ax.add_patch(light)

# Define the initial positions of the point-lights
positions = np.random.rand(num_lights, 2)

# Define the velocities of the point-lights
velocities = np.zeros((num_lights, 2))

# Define the acceleration of the point-lights
acceleration = np.zeros((num_lights, 2))

# Define the update function for the animation
def update(frame):
    global positions, velocities, acceleration
    
    # Update the positions of the point-lights
    positions += velocities
    velocities += acceleration
    
    # Keep the point-lights within the bounds of the figure
    positions = np.clip(positions, 0, 1)
    
    # Update the positions of the point-lights on the plot
    for i, light in enumerate(lights):
        light.center = positions[i]
        
    # Return the updated point-lights
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
