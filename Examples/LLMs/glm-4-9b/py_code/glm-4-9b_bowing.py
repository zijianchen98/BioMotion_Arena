
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15  # Number of point-lights
duration = 300   # Duration of the animation in frames
jump_height = 0.2  # Maximum jump height
jump_width = 0.1  # Maximum jump width
frequency = 0.05  # Frequency of the jump

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-0.1, 1.1)
ax.axis('off')

# Initialize the scatter plot for the point-lights
scatter = ax.scatter([], [], color='white', s=50)

def init():
    scatter.set_offsets(np.zeros((num_points, 2)))
    return scatter,

def update(frame):
    angle = 2 * np.pi * frequency * frame
    t = frame / duration  # Normalized time (0 to 1)
    
    # Jump trajectory (sine wave)
    y = jump_height * np.sin(angle)
    x = jump_width * (1 - np.cos(angle)) * 0.5
    
    # Randomly distribute the points around the jump trajectory
    offsets = np.random.rand(num_points, 2)
    offsets[:, 0] *= x
    offsets[:, 1] *= y
    
    # Concatenate the offsets with the base trajectory
    positions = np.vstack([np.ones((num_points, 1)) * frame * 0.01, offsets]).T
    
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=duration, init_func=init, blit=True)

# Show the animation
plt.show()
