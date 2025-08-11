
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(0, 3)
ax.set_facecolor('black')
ax.axis('off')  # Turn off the axes

# Create initial positions for the point-lights
num_points = 15
points = np.zeros((num_points, 2))

# Define jump parameters
jump_height = 0.5
jump_distance = 1.5
frames = 60

# Generate the animation data
def generate_jump_data():
    jump_data = []
    for t in np.linspace(0, 1, frames):
        # Calculate vertical position based on a simple sine wave for jumping motion
        vertical_position = np.sin(t * np.pi) * jump_height
        horizontal_position = t * jump_distance

        # Update positions for point-lights (representing the body)
        # Example structure for point-lights (3 vertical rows of 5 points)
        jump_data.append([
            (0, 2 + vertical_position),  # Head
            (-0.1, 1 + vertical_position), (-0.05, 1 + vertical_position), (0, 1 + vertical_position),
            (0.05, 1 + vertical_position), (0.1, 1 + vertical_position),
            (-0.1, 0 + vertical_position), (-0.05, 0 + vertical_position), (0, 0 + vertical_position),
            (0.05, 0 + vertical_position), (0.1, 0 + vertical_position),
            (-0.15, -1 + vertical_position), (0.15, -1 + vertical_position), 
            (-0.1, -2 + vertical_position), (0.1, -2 + vertical_position), (0, -1 + vertical_position)
        ])
    return jump_data

# Initial points setup based on the jump data
jump_data = generate_jump_data()

# Initialize points on the plot
point_lights, = ax.plot([], [], 'o', color='white')

def init():
    point_lights.set_data([], [])
    return point_lights,

def update(frame):
    # Update point-lights position based on generated data
    x_data = [point[0] for point in jump_data[frame]]
    y_data = [point[1] for point in jump_data[frame]]
    
    point_lights.set_data(x_data, y_data)
    return point_lights,

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=50)

# Show the animation
plt.show()
