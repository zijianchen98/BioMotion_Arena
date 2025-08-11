
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuration Constants
num_points = 15  # Number of point-lights
walking_cycle_steps = 60  # Number of frames in one walking cycle
frame_rate = 30  # Frames per second

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Define the initial positions of point-lights
def init():
    points.set_data([], [])
    return points,

# Walking pattern (Simple representation for a happy man walking)
def update(frame):
    # Calculate the vertical position of the "legs" during walking
    leg_offset = 0.2 * np.sin(2 * np.pi * frame / walking_cycle_steps)
    
    # Coordinates for point-lights (skelton-like for a happy man holding weight)
    head = (0, 1)
    shoulders = [(-0.3, 0.7), (0.3, 0.7)]
    elbows = [(-0.5, 0.5), (0.5, 0.5)]
    wrists = [(-0.6, 0.3), (0.6, 0.3)]
    hips = [(-0.2, 0.2 + leg_offset), (0.2, 0.2 - leg_offset)]
    knees = [(-0.2, 0), (0.2, 0)]
    feet = [(-0.2, -0.2), (0.2, -0.2)]
    
    # Combine all points
    x = [head[0]] + [p[0] for p in shoulders + elbows + wrists + hips + knees + feet]
    y = [head[1]] + [p[1] for p in shoulders + elbows + wrists + hips + knees + feet]
    
    # Update point-light positions
    points.set_data(x, y)
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=walking_cycle_steps, 
                              init_func=init, blit=True, interval=1000/frame_rate)

# Show the animation
plt.show()
