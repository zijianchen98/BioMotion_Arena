
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Point positions for the "happyman" walking with heavy weight
# Positioning for 15 point lights
def get_happy_man_positions(frame):
    # Define walking patterns (x, y) for each point-light
    base_y = np.array([-1, -0.5, 0, 0.5, 1])  # vertical base positions
    leg_movement = np.sin(2 * np.pi * (frame / 20))  # cyclic movement for legs
    arm_movement = np.sin(2 * np.pi * (frame / 20 + 0.5))  # cyclic movement for arms
    
    # Adjusted positions for left and right legs and arms
    positions = np.array([
        [0, base_y[0] + arm_movement],   # Left arm
        [-0.5, base_y[1] + leg_movement], # Left leg
        [0.5, base_y[1] + leg_movement],  # Right leg
        [0, base_y[3] + arm_movement],    # Right arm
        [0, base_y[2]],                    # Center of body
        [-0.25, base_y[4]],                # Left shoulder
        [0.25, base_y[4]],                 # Right shoulder
        [-0.25, base_y[3]],                # Left knee
        [0.25, base_y[3]],                 # Right knee
        [0, base_y[4]],                    # Additional 
        [-0.5, base_y[2]],                 # Extra left
        [0.5, base_y[2]],                  # Extra right
        [-0.5, base_y[1]],                 # Extra left lower
        [0.5, base_y[1]],                  # Extra right lower
        [0, base_y[2] - 0.5],              # Slightly lower
        [0, base_y[2] + 0.5],              # Slightly higher
    ])
    return positions

# Setup the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=8)  # Points will be white

# Animation update function
def update(frame):
    positions = get_happy_man_positions(frame)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
