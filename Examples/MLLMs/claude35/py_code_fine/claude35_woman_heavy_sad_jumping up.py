
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the number of points (joints)
num_points = 15

# Generate initial positions for 15 points
positions = np.zeros((num_points, 2))

# Possible positions for a sad woman representation
# (mocked joint positions for demonstration)
positions[0] = [0, 5]    # Head
positions[1:6] = [[-1, 4], [1, 4], [-1, 3], [1, 3], [0, 2]]  # Arms and torso
positions[6:15] = [[-1, 1], [1, 1], [-1, 0], [1, 0], [-0.5, -1], [0.5, -1], [-1, -2], [1, -2], [-0.5, -3], [0.5, -3]]  # Legs

# Create jump motion data (simple sinusoidal for demo)
def generate_jump_motion():
    t = np.linspace(0, 2 * np.pi, 100)
    y_motion = 5 + 2 * np.sin(t)  # Jump height
    return y_motion

# Generate jump data
jump_height = generate_jump_motion()

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-4, 6)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Animation function
def animate(frame):
    y_offset = jump_height[frame % len(jump_height)]
    
    # Update position with y_offset; keeping x positions static
    new_positions = positions.copy()
    new_positions[:, 1] += y_offset
    
    # Update the points on the plot
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(jump_height), init_func=init, blit=True, interval=1000/30)

# Show the animation
plt.show()
