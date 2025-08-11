
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')  # Black background
ax.axis('off')  # Turn off the axis

# Number of points to represent the limbs and joints
num_points = 15
point_lights, = ax.plot([], [], 'o', color='white', markersize=10)  # Static points

# Initialize the position of points representing a sad man
def init():
    point_lights.set_data([], [])
    return point_lights,

# Update function to animate the point positions
def update(frame):
    # Define positions for points (could be adjusted based on desired motion)
    x_positions = np.array([
        5,  # Head
        4, 5, 6,  # Shoulders
        3.8, 4, 5.2, 6.2,  # Elbows
        2, 8, 5,  # Hips
        2.5, 4.5, 7,  # Knees
        2, 8, 7  # Feet
    ])
    
    # Each row represents Y position for various frames
    y_positions = [
        [8, 0, 0, 0],  # Head, 4 limbs relaxed
        [7, 0, 0, 0],  # Like waving with right hand
        [5, 0, 0, 0],  # Like waving with right hand up
        [7, 0, 0, 0],  # Return to resting position
    ]
    
    # Get respective y position based on the frame
    if frame < len(y_positions):
        y = y_positions[frame] + [5, 4, 3, 2]  # Adjust the vertical positions
    else:
        y = y_positions[-1] + [5, 4, 3, 2]
    
    point_lights.set_data(x_positions, y)
    return point_lights,

# Set up the animation
ani = animation.FuncAnimation(fig, update, frames=4, init_func=init, blit=True, repeat=True, interval=300)

# Show the animation
plt.show()
