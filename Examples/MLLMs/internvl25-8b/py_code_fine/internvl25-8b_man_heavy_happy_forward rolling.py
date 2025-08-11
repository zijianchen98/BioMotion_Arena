
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Create a list to hold point lights
points = []

# Define the initial positions for the point lights representing the human figure
initial_positions = [
    (50, 250), (100, 210), (150, 170), (200, 70), (250, 150), 
    (110, 50), (60, 100), (90, 180), (130, 230), (170, 240), 
    (220, 140), (280, 90), (270, 220), (320, 300)
]

# Add the initial positions to the points list
for position in initial_positions:
    points.append(ax.plot(position, 'o', color='white', markersize=5)[0])
    points.append(ax.plot(position, "", color='white')[0])

# Update function for animation
def update(frame):
    positions = []
    for p in points:
        # Define the motion based on the desired action
        if frame % 15 == 0:  # Start moving downward
            dy = -10
        elif frame % 15 == 5:  # Start moving sideways
            dx = 0
            dy = 0
        elif frame % 15 == 10:  # Transition and move up again
            dy = 10
        else:
            dy = 0
        positions.append((p.get_x(), p.get_y() + dy))
    
    # Update positions
    for i in range(len(points)):
        points[i].set_data(*positions[i])
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=range(120), interval=250, blit=True, repeat=False)

# Show the plot
plt.xlim(0, 350)
plt.ylim(0, 280)
plt.axis('off')
plt.show()
