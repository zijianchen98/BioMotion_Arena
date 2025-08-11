
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)  # white dots

# Initialize the points' positions
num_points = 15
points_position = np.zeros((num_points, 2))

def init():
    points.set_data([], [])
    return points,

# Update function for animation
def update(frame):
    # Calculate the new positions based on a sine wave motion for rolling
    t = frame / 10.0  # Time parameter for smooth motion
    roll_angle = np.sin(t)  # Use sine for smooth up and down motion
    
    # Forward roll-like positions (simplified for 15 points)
    # Setting positions for 15 joint locations
    points_position[0] = [0, 3 + roll_angle]  # Head
    points_position[1] = [-1, 2 + roll_angle]
    points_position[2] = [1, 2 + roll_angle]
    points_position[3] = [-2, 1 + roll_angle]
    points_position[4] = [2, 1 + roll_angle]
    points_position[5] = [-1.5, 0 + roll_angle]
    points_position[6] = [1.5, 0 + roll_angle]
    points_position[7] = [-2, -1 + roll_angle]
    points_position[8] = [2, -1 + roll_angle]
    points_position[9] = [0, -2 + roll_angle]  # Torso center
    points_position[10] = [-2.5, -2.5 + roll_angle]
    points_position[11] = [2.5, -2.5 + roll_angle]
    points_position[12] = [-2, -3 + roll_angle]
    points_position[13] = [2, -3 + roll_angle]
    points_position[14] = [0, -4 + roll_angle]  # Feet
    
    # Update the data of point lights
    points.set_data(points_position[:, 0], points_position[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=50)

# Show the animation
plt.show()
