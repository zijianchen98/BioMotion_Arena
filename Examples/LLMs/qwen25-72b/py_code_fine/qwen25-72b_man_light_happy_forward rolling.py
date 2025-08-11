
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points
initial_positions = np.array([
    [0, 0],  # Center of mass
    [1, 1],  [1, -1],  [-1, 1],  [-1, -1],  # Limbs
    [0.5, 0.5],  [0.5, -0.5],  [-0.5, 0.5],  [-0.5, -0.5],  # Joints
    [1.5, 1.5],  [1.5, -1.5],  [-1.5, 1.5],  [-1.5, -1.5],  # Extremities
    [2, 2],  [2, -2],  [-2, 2],  [-2, -2]  # Additional points for detail
])

# Function to update the positions of the points
def update_positions(i):
    angle = i * np.pi / 180  # Convert frame number to angle in radians
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    new_positions = np.dot(initial_positions, rotation_matrix.T)
    for j, point in enumerate(points):
        point.set_data(new_positions[j])
    return points

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.set_facecolor('black')
plt.axis('off')

# Create the points
points = [ax.plot([], [], 'wo', markersize=10)[0] for _ in range(15)]

# Create the animation
ani = animation.FuncAnimation(fig, update_positions, frames=360, interval=20, blit=True)

# Show the animation
plt.show()
