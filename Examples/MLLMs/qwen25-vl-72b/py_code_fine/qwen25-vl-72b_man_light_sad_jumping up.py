
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')

# Create the points
points = []
for i in range(15):
    point, = ax.plot([], [], 'wo', markersize=5)
    points.append(point)

# Define the initial positions of the points
positions = np.array([
    [0, 5],
    [-1, 4], [1, 4],
    [-2, 3], [0, 3], [2, 3],
    [-3, 2], [-1, 2], [1, 2], [3, 2],
    [-2, 1], [0, 1], [2, 1],
    [-1, 0], [1, 0]
])

# Define the velocities of the points
velocities = np.zeros((15, 2))

# Define the gravity
gravity = np.array([0, -0.1])

# Define the spring constants
spring_constants = np.ones((15, 15)) * 0.1
np.fill_diagonal(spring_constants, 0)

# Define the rest lengths
rest_lengths = np.zeros((15, 15))
for i in range(15):
    for j in range(i+1, 15):
        rest_lengths[i, j] = np.linalg.norm(positions[i] - positions[j])
        rest_lengths[j, i] = rest_lengths[i, j]

def update(frame):
    global positions, velocities
    
    # Apply gravity
    velocities += gravity
    
    # Apply spring forces
    for i in range(15):
        force = np.zeros(2)
        for j in range(15):
            if i != j:
                vector = positions[j] - positions[i]
                distance = np.linalg.norm(vector)
                if distance > 0:
                    force += spring_constants[i, j] * (distance - rest_lengths[i, j]) * vector / distance
        velocities[i] += force
    
    # Update positions
    positions += velocities
    
    # Update the points
    for i in range(15):
        points[i].set_data(positions[i][0], positions[i][1])
    
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

plt.show()
