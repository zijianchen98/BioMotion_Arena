
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the 15 point-lights
light_positions = [
    (0,  0 ), ( 4,  6), ( 7,  9), (10,  8), (13,  5),
    ( 3,  2), ( 5,  4), ( 8,  7), (11,  3), (14,  1),
    ( 1,  0), ( 6,  3), ( 9,  5), (12,  7)
]

# Function to update the positions of the lights
def update_light_positions(frame):
    # Define the movement pattern for each-down
    movement_pattern = [
        (0,   t), ( 4,  6), ( 7,  9), (10,  8), (13,  5),
        ( 3,  2), ( 5,  4), ( 8,  7), (11,  3), (14,  1),
        ( 1,   t), ( 6,  3), ( 9,  5), (12,  7)
    ]
    
    # Update the positions based on the frame number
    for i in range(len(light_positions)):
        x, y = light_positions[i]
        new_x = int((movement_pattern[i][0] + frame) % 15)
        new_y = int((movement_pattern[i][1] + frame) % 15)
        light_positions[i] = (new_x, new_y)
    
    # Clear the previous frame
    ax.clear()
    
    # Plot the updated positions of the lights
    for x, y in light_positions:
        ax.plot(x, y, 'wo', markersize=10)
    
    # Set the limits for the plot
    ax.set_xlim(0, 15)
    ax.set_ylim(1, 15)
    ax.set_aspect('equal')
    ax.axis('off')

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 10))
axight_positions(light_positions)

# Create the animation
animation = FuncAnimation(fig, update_light_positions, frames=100, interval=50)

# Show the animation
plt.show()
