
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point lights
# Adjust these coordinates to match the desired pose and proportions
initial_positions = np.array([
    [0, 50],  # Head top
    [-5, 45],  # Left shoulder
    [5, 45],  # Right shoulder
    [-10, 35], # Left elbow
    [10, 35], # Right elbow
    [-15, 25], # Left wrist
    [15, 25], # Right wrist
    [-5, 30],  # Left hip
    [5, 30],  # Right hip
    [-10, 15], # Left knee
    [10, 15], # Right knee
    [-10, 0], # Left ankle
    [10, 0], # Right ankle
    [-5,-8], # Left toe
    [5,-8]  # Right toe 
])


# Number of frames in the animation
num_frames = 60

# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-25, 25)  # Adjust limits as needed
ax.set_ylim(-15, 60) # Adjust limits as needed
ax.set_aspect('equal')
ax.set_facecolor('black')  # Set background color to black
points, = ax.plot([], [], 'wo', markersize=4) # White dots


# Initialize the animation
def init():
    points.set_data([], [])
    return points,

# Update function for the animation
def animate(i):
    # Example: Simple vertical downward motion for sitting
    # Modify this to implement more complex and realistic movements
    y_offset = -i * 0.2 * (1+np.sin(i/20)) # downwards bend
    new_positions = initial_positions.copy()

    # Apply motion to specific joints
    # Head and shoulders
    new_positions[:3,1] += y_offset # move down as a rigid body
    #elbows
    new_positions[3:5, 1] += 1.5 * y_offset # bigger bend
    #wrists
    new_positions[5:7, 1] += 1.7*y_offset
    # hips
    new_positions[7:9, 1] += 2.0* y_offset
    # knees
    new_positions[9:11, 1] += 1.2*y_offset
    # ankles
    new_positions[11:13,1] += 0.5*y_offset

    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, init_func=init, blit=True)

# Save the animation (optional)
# ani.save('biological_motion.gif', writer='pillow', fps=30) 
# or show
plt.show()

