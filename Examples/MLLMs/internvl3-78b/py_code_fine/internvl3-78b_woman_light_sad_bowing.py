
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create a list to hold the points
points, = ax.plot([], [], 'bo')

# Coordinates and motion for the point-lights
bowing_motion = np.array([
    [50, 10],  # Head
    [50, 20],  # Neck
    [50, 30],  # Upper Body
    [50, 40],  # Middle Body
    [50, 50],  # Lower Body
    [40, 50],  # Legs (left)
    [60, 50],  # Legs (right)
    [40, 30],  # Left Arm
    [60, 30],  # Right Arm
    [45, 20],  # Left Hand
    [55, 20],  # Right Hand
    [45, 40],  # Left Knee
    [55, 40],  # Right Knee
    [45, 60],  # Left Feet
    [55, 60],  # Right Feet
])

# Interpolate motion over time (simple example of bowing)
def update(num, points, bowing_motion, ax):
    # Calculate displacement for bowing
    displacement = np.sin(num / 10.0) * 5  # Bowing amplitude
    offset = np.array([0, displacement])

    # Update each point's position
    new_coords = bowing_motion + offset

    points.set_data(new_coords[:, 0], new_coords[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, fargs=(points, bowing_motion, ax),
                              interval=20, blit=True, repeat=True)

plt.show()
