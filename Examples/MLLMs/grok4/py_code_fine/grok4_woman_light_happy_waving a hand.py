
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define number of points (joints)
n_points = 15

# Create the initial position for the points (joint positions)
# Example coordinates for a humanoid figure
initial_positions = np.array([
    [0, 4],   # head
    [-1, 3],  # left shoulder
    [1, 3],   # right shoulder
    [-1, 2],  # left elbow
    [1, 2],   # right elbow
    [-1, 1],  # left wrist
    [1, 1],   # right wrist
    [0, 2],   # torso 
    [-0.5, 0],  # left hip
    [0.5, 0],   # right hip
    [-0.5, -2], # left knee
    [0.5, -2],  # right knee
    [-0.5, -4], # left ankle
    [0.5, -4],  # right ankle
    [0, 0],     # torso center
])

# Generate waving motion for the right hand
def wave_motion(frame):
    # Define a simple waving motion for the right arm
    waving_amplitude = 0.5  # The distance to wave
    angle = np.sin(frame * 0.2) * waving_amplitude  # Frame based sine wave
    positions = initial_positions.copy()

    # Update the right wrist position for waving
    positions[5, 1] += angle  # Update y-coordinate of right wrist (index 5)

    return positions

# Setting up the figure
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')

# Create scatter plot for point lights
points, = ax.plot([], [], 'o', color='white')

# Animation function that will be called at each frame
def animate(frame):
    positions = wave_motion(frame)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Creating the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
