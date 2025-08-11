
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1, 2)
ax.set_facecolor('black')

# Initialize point lights positions for a running man
# Points will be represented as y-coordinates for the arms, legs, head, etc.
n_points = 15
points = np.array([
    [0, 1],   # Head
    [-0.2, 0.8], [0.2, 0.8], # Shoulders
    [-0.3, 0.6], [0.3, 0.6], # Elbows
    [-0.4, 0.4], [0.4, 0.4], # Hands
    [-0.3, 0], [0.3, 0], # Hips
    [-0.4, -0.6], [0.4, -0.6], # Knees
    [-0.5, -1], [0.5, -1] # Feet
]).astype(float)

scatter = ax.scatter(points[:, 0], points[:, 1], color='white')

# Define the run motion path
def run_motion(frame):
    # Update the y-coordinates of the points to simulate running
    time_factor = frame / 10.0  # Adjust for speed
    motion_offset = 0.2 * np.sin(time_factor * np.pi * 2)  # Sine wave for smooth motion
    
    # Update positions of the points to simulate the running action
    points[0, 1] = 1 + motion_offset  # Head oscillates
    points[1:3, 1] = 0.8 + motion_offset  # Shoulders
    points[3:5, 1] = 0.6 - motion_offset * 0.5  # Elbows
    points[5:7, 1] = 0.4 + motion_offset * 0.3  # Hands
    points[7:9, 1] = motion_offset * 0.3  # Hips
    points[9:11, 1] = -0.6 + motion_offset  # Knees
    points[11:13, 1] = -1 + motion_offset * 0.7  # Feet

    scatter.set_offsets(points)  # Update scatter plot
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, run_motion, frames=200, interval=50, blit=True)

# Show the animation
plt.show()
