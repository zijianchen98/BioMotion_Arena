
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points
num_points = 15

# Define positions of the points (wrist, elbow, shoulder, etc.)
# This will vary per frame to simulate waving.
initial_positions = np.array([
    [0, 4],  # Head
    [-1, 3], [1, 3],  # Shoulders
    [-1.5, 2], [1.5, 2],  # Elbows
    [-2, 1], [2, 1],  # Hands
    [-1, 0], [1, 0],  # Hips
    [0, -1],  # Torso
    [-1.5, -2], [1.5, -2],  # Knees
    [-1.7, -3], [1.7, -3],  # Feet
])

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

def animate(frame):
    # Update positions for the waving motion
    wave_amplitude = 0.5 * np.sin(frame * 0.2)  # Waving effect
    positions = initial_positions.copy()
    
    # Adjust positions for waving effect
    positions[5, 1] += wave_amplitude  # Adjust hand position
    positions[8, 1] += wave_amplitude  # Adjust hand position (other hand if you want)
    
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=100, blit=True)

# Display the animation
plt.show()
