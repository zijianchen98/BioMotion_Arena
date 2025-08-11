
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
duration = 2000  # duration of animation in milliseconds
frames = 60  # total frames in the animation

# Function to initialize point-light positions
def init_positions():
    # Initial position of points in a sad jumping stance
    # Y-coordinates for a sad woman (approximate)
    y_positions = np.linspace(-1, -5, num_lights)
    x_positions = np.zeros(num_lights)
    
    # Adjust x positions for a more dynamic layout
    x_offsets = np.random.uniform(-0.1, 0.1, num_lights)
    return x_positions + x_offsets, y_positions

# Update function for animation
def update(frame):
    plt.cla()  # Clear previous frame
    
    # Update positions
    jump_height = 3 * np.sin(np.pi * frame / frames)  # Height of jump
    x_positions = np.zeros(num_lights) 
    y_positions = init_y + jump_height + np.linspace(0, -5, num_lights)

    # Draw point lights
    plt.scatter(x_positions, y_positions, color='white', s=100)
    plt.xlim(-1, 1)   # Set x-axis limits
    plt.ylim(-6, 1)   # Set y-axis limits
    plt.axis('off')    # Turn off the axis
    plt.gca().set_facecolor('black')  # Set background color

# Initialize positions
init_x, init_y = init_positions()

# Setup plot
fig, ax = plt.subplots()
ax.set_facecolor('black')
plt.xlim(-1, 1)
plt.ylim(-6, 1)
plt.axis('off')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=duration/frames)

# Show the animation
plt.show()
