
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the joint positions over time (replace with actual motion capture data or simulated data)
# This is a simplified example and would need to be refined for realistic motion
num_frames = 60
joint_positions = np.zeros((15, 2, num_frames))

# Example: Simulate jumping motion (replace with actual data)
t = np.linspace(0, 2 * np.pi, num_frames)
y_offset = 3 * np.sin(t) # Simulate vertical jump

# Define initial positions (adjust as needed)
initial_positions = np.array([
    [0, 10], [-2, 8], [2, 8],  # Head
    [-3, 5], [3, 5],  # Shoulders
    [-2, 3], [2, 3],  # Elbows
    [-4, 0], [4, 0], # Hands
    [0, 3], # Torso
    [-1, -3], [1, -3],  # Knees
    [-1, -7], [1, -7] # Feet
])


for i in range(num_frames):
    joint_positions[:, :, i] = initial_positions + np.array([0, y_offset[i]])


# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 20) # Adjusted y-limit
ax.set_aspect('equal')
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=8)


# Animation update function
def update(frame):
    x = joint_positions[:, 0, frame]
    y = joint_positions[:, 1, frame]
    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)


# Optional: Save the animation as a GIF
#ani.save('jumping_man.gif', writer='pillow') 

plt.show()
