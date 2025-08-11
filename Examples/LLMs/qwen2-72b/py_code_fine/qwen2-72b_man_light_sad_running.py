
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and the size of the figure
num_points = 15
fig, ax = plt.subplots(figsize=(6, 6))

# Set the background color to black
ax.set_facecolor('black')

# Remove the axis labels and ticks
ax.axis('off')

# Initialize the point lights as empty lines
point_lights = [plt.Line2D([], [], lw=0, marker='o', markersize=8, color='white') for _ in range(num_points)]
for line in point_lights:
    ax.add_line(line)

# Define the initial positions of the point lights
positions = np.zeros((num_points, 2))
velocities = np.random.normal(0, 0.1, (num_points, 2))

# Function to update the positions of the point lights
def update(frame):
    global positions, velocities
    
    # Update the positions based on the velocities
    positions += velocities
    
    # Keep the point lights within the boundaries of the figure
    positions = np.clip(positions, 0, 1)
    
    # Update the data of each point light
    for i, line in enumerate(point_lights):
        line.set_data(positions[i, 0], positions[i, 1])
    
    return point_lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=20, blit=True)

# Show the animation
plt.show()
