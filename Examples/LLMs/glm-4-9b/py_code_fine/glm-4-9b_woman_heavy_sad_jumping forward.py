
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
num_points = 15
num_frames = 200
background_color = 'black'
point_color = 'white'
point_size = 5

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 6), facecolor=background_color)
ax.set_facecolor(background_color)
ax.axis('off')

# Initialize positions of the point-lights
# Assuming the initial positions are in a spherical shape around the waist
initial_radius = 1.0
theta = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
initial_x = initial_radius * np.cos(theta)
initial_y = initial_radius * np.sin(theta)
positions = np.column_stack((initial_x, initial_y))

# Function to update positions
def update(frame):
    ax.clear()
    ax.set_facecolor(background_color)
    ax.axis('off')
    
    # Time variable for the jumping motion
    t = frame / num_frames * np.pi
    
    # Simulate jumping forward
    jump_height = 0.5 * np.sin(t)  # Amplitude of the jump
    jump_horizontal = 1.0 * t  # Horizontal movement over time
    
    # Update positions for jumping forward
    new_x = positions[:, 0] + jump_horizontal
    new_y = positions[:, 1] + jump_height
    new_positions = np.column_stack((new_x, new_y))
    
    # Plot the point-lights
    ax.scatter(new_positions[:, 0], new_positions[:, 1], s=point_size, color=point_color)
    
    return ax,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, blit=True, interval=50)

plt.show()
