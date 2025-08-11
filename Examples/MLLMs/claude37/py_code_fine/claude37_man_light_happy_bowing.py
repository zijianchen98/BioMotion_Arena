
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create the initial positions of the point lights
def get_point_light_positions(frame):
    # Assuming a smooth bowing motion
    # 15 points arranged vertically (head to feet)
    
    # Base positions of points
    positions = np.zeros((15, 2))
    
    # Bowing by modifying y-coordinates
    # Lowering the head and bending the torso
    bow_amount = 0.1 * np.sin(frame * 0.2)  # Smooth oscillation for bowing effect
    
    # Assign positions (x, y)
    positions[:, 0] = 0  # x is constant; all points are in the center
    positions[0:5, 1] = np.array([1, 0.8, 0.6, 0.4, 0.2]) + bow_amount  # Head to upper body
    positions[5:10, 1] = np.array([0, -0.2, -0.4, -0.6, -0.8]) + bow_amount  # Lower body
    positions[10:15, 1] = np.array([-1, -1.2, -1.4, -1.6, -1.8]) + bow_amount  # Feet
    
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 1)
ax.axis('off')  # No axis

# Create a scatter plot for point lights
points = ax.scatter([], [], c='white')

# Initialization function for the animation
def init():
    points.set_offsets([])
    return points,

# Animation function
def animate(frame):
    positions = get_point_light_positions(frame)
    points.set_offsets(positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, init_func=init, blit=True, repeat=True)

# Set background color
fig.patch.set_facecolor('black')

# Show the animation
plt.show()
