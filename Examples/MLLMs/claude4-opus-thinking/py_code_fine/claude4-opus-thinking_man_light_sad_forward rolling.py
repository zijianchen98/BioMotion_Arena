
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')

# Number of point-lights
num_lights = 15
points = np.zeros((num_lights, 2))

# Initialize positions of the point-lights
# Fixed skeleton positions for "sadman" representation
skeleton_positions = np.array([
    [0, 2],   # head
    [0, 1.5], # shoulders
    [-0.5, 1], [0.5, 1], # arms
    [0, 0],   # torso
    [-0.5, -1], [0.5, -1], # hips
    [-1, -2], [1, -2], # legs
    [-0.75, -1.5], [0.75, -1.5], # knees
    [-0.5, -2.5], [0.5, -2.5], # feet
    [0, -3] # bottom point for roll
])

# Initialize scatter plot
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Update function for animation
def update(frame):
    # Simulate a forward roll by updating positions
    roll_angle = np.pi / 30 * frame  # angle increment
    forward_roll = np.array([[np.cos(roll_angle), -np.sin(roll_angle)],
                              [np.sin(roll_angle), np.cos(roll_angle)]])
    
    # Update positions with rolling effect
    if frame < 60:  # Rolling up
        points[:] = skeleton_positions @ forward_roll
    elif frame < 120:  # Rolling down
        points[:] = skeleton_positions @ forward_roll
        points[:, 1] -= 1  # Just to show downward motion
        
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=240, interval=50, blit=True)

# Show the animation
plt.show()
