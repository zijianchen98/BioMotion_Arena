
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Frame rate and duration
fps = 30
duration = 5 # seconds
frames = fps * duration

# Set up the figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the points
points, = ax.plot([], [], 'ko', ms=6)

# Define the positions of the points for a bowing motion
# Let's assume a simplified model where the points form a basic stick figure
def init():
    points.set_data([], [])
    return points,

def update(frame):
    angle = np.pi / duration * frame # Bowing angle in radians
    
    # Define initial positions (for standing pose)
    x, y = np.array([
        [-0.05, -0.15, -0.05, -0.25,  0.05,  0.15,  0.05,  0.25,  0,  0, -0.03, -0.15,  0.05,  0.15,  0.05], 
        [ 0,     0,  0.1,  0.2, -0.05, -0.1, -0.15, -0.2, -0.4, -0.6,  0,   0,  0.1,  0.2,  0.3]
    ])

    # Apply the bowing transformation
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle),  np.cos(angle)]
    ])
    
    # Rotate all points around the pivot (the center of the bow)
    xy = np.dot(rotation_matrix, np.array([x, y]))
    points.set_data(xy[0], xy[1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, init_func=init, frames=frames, interval=1000/fps, blit=True)

# Save the animation as a gif
# ani.save('bowing_animation.gif', writer='pillow')

# Show the plot
plt.show()
