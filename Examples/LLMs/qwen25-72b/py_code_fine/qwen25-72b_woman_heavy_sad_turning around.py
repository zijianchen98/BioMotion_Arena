
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
num_points = 15

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
plt.axis('off')

# Initialize the point-lights
points = [plt.plot([], [], 'o', color='white')[0] for _ in range(num_points)]

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0, 0],  # Center of mass
    [1, 1],  [1, -1],  [-1, 1],  [-1, -1],  # Limbs
    [2, 2],  [2, -2],  [-2, 2],  [-2, -2],  # Extremities
    [1.5, 0.5],  [1.5, -0.5],  [-1.5, 0.5],  [-1.5, -0.5],  # Shoulders and hips
    [0.5, 1.5],  [0.5, -1.5],  [-0.5, 1.5],  [-0.5, -1.5]  # Elbows and knees
])

# Define the turning motion
def turn_around(t):
    angle = t * np.pi / 4  # Slow turning
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    return np.dot(initial_positions, rotation_matrix)

# Update function for the animation
def update(frame):
    positions = turn_around(frame)
    for i, point in enumerate(points):
        point.set_data(positions[i][0], positions[i][1])
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 8, 200), interval=50, blit=True)

# Display the animation
plt.show()
