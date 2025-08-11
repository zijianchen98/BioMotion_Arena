
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_points = 15

# Initial positions of the point-lights representing a bowing action
initial_positions = np.array([
    [0, 5],   # head
    [2, 4], [-2, 4],  # shoulders
    [2, 3], [-2, 3],  # elbows
    [1, 2], [-1, 2],  # hands
    [1, 1], [-1, 1],  # hips
    [1, 0], [-1, 0],  # knees
    [1, -1], [-1, -1],  # feet (or lower legs)
])

# Define the bowing action as an animation function
def animate(frame):
    # Clear current points
    xdata.clear()
    ydata.clear()

    # Adjust the y-position to simulate the bowing motion
    movement_factor = np.sin(frame / 10)  # Sine wave for smooth motion
    bowing_positions = initial_positions.copy()
    
    # Making the head lower to simulate bowing
    bowing_positions[0, 1] += movement_factor  # Head moves down
    bowing_positions[1:, 1] += movement_factor  # Other points follow

    # Append new positions to xdata and ydata
    xdata.extend(bowing_positions[:, 0])
    ydata.extend(bowing_positions[:, 1])

    # Update the scatter plot
    scatter.set_offsets(np.column_stack((xdata, ydata)))
    return scatter,

# Create a figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-3, 6)
ax.set_facecolor('black')  # Black background

# Create a scatter plot for the point-lights
xdata, ydata = [], []
scatter = ax.scatter(xdata, ydata, color='white', s=100)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Display the animation
plt.show()
