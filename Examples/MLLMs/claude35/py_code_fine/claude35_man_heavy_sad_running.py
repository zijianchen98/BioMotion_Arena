
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point lights
num_points = 15

# Initial positions of the point lights
positions = np.array([
    [0, 3],  # Head
    [-1, 2], [1, 2],  # Shoulders
    [-1, 1], [1, 1],  # Elbows
    [-1, 0], [1, 0],  # Hips
    [-1, -1], [1, -1], # Knees
    [-0.5, -2], [0.5, -2], # Feet (without weight)
    [0, -2.5],  # Weight position
])

# Running animation function
def update(frame):
    plt.clf()
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.gca().set_facecolor('black')

    # Create a running motion effect
    weight_move = np.sin(frame / 5) / 10
    x_positions = positions[:, 0] + weight_move
    y_positions = positions[:, 1] + np.sin(frame / 5)

    # Scatter points for point lights
    plt.scatter(x_positions, y_positions, color='white', s=100)

    # Draw connecting lines for the limbs to represent coherent motion
    plt.plot(x_positions[[0, 1, 3, 6]], y_positions[[0, 1, 3, 6]], color='white')  # Head to Shoulder to Hip
    plt.plot(x_positions[[2, 4, 6]], y_positions[[2, 4, 6]], color='white')  # Shoulder to Elbow to Hip
    plt.plot(x_positions[[5, 6, 8]], y_positions[[5, 6, 8]], color='white')  # Hip to Knee to Foot
    plt.plot(x_positions[[7, 6, 9]], y_positions[[7, 6, 9]], color='white')  # Knee to Hip to Weight

# Create the figure
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50)

plt.axis('off')  # Turn off the axis
plt.show()
