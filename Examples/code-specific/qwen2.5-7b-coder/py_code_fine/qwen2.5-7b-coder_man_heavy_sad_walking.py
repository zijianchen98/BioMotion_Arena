
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and frames
num_points = 15
num_frames = 60

# Create a figure and axis for the plot
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the points
points, = ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

def update(frame):
    # Clear the previous frame
    points.set_data([], [])
    
    # Calculate new positions based on walking motion
    t = frame / num_frames * 2 * np.pi
    x = 4 * np.sin(t) - 2 * np.cos(2 * t)
    y = 2 * np.sin(2 * t)
    
    # Distribute points along the path
    angles = np.linspace(0, 2 * np.pi, num_points + 1)[:-1]
    px = x + 1 * np.cos(angles)
    py = y + 1 * np.sin(angles)
    
    # Update the points' positions
    points.set_data(px, py)
    
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True)

plt.show()
