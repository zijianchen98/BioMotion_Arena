
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 2.5)

# Initialize the plot objects for each of the 15 point-lights
num_points = 15
point_cloud = ax.scatter([], [], color='white', s=10)

# Define the function that simulates the jumping motion for the point-lights
def generate_jump_position(t, jump_height=1.5, jump_period=2):
    x = 0.2 * np.sin(2 * np.pi * t / jump_period)  # Horizontal sinusoidal motion to simulate stepping forward
    y = np.abs(np.sin(2 * np.pi * t / jump_period)) * jump_height  # Vertical sinusoidal motion to simulate the jump
    return x, y

# Define the update function for the animation
def update(frame):
    t = frame / 100  # Time scaling
    x_positions, y_positions = [], []
    
    # Generate the positions for each point-light based on the jump motion
    for i in range(num_points):
        offset = (i / num_points) * 2 - 1  # Spread the points across a width
        x, y = generate_jump_position(t + i * 0.1, jump_height=1.5, jump_period=2)
        x_positions.append(x + offset)
        y_positions.append(y)
        
    point_cloud.set_offsets(np.column_stack((x_positions, y_positions)))
    return point_cloud,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 20, 600), blit=True, interval=20)

plt.axis('off')  # Hide axes for a clean look
plt.show()
