
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Number of point lights
num_points = 15

# Initial positions of the points (representing the body joints)
points = np.array([
    [0, 1],   # head
    [-0.5, 0.5],  # left shoulder
    [0.5, 0.5],   # right shoulder
    [-0.5, 0],     # left elbow
    [0.5, 0],      # right elbow
    [-0.5, -0.5],  # left hand
    [0.5, -0.5],   # right hand
    [-0.75, 0],    # left hip
    [0.75, 0],     # right hip
    [-0.75, -1],   # left knee
    [0.75, -1],    # right knee
    [-0.5, -1.5],  # left foot
    [0.5, -1.5],   # right foot
    [0, 0.5],      # torso
    [0, 0],        # center
])

# Function to compute the positions of points for the turning action
def update_points(frame):
    global points
    angle = np.radians(frame * 2)  # rotation angle for each frame
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    rotated_points = np.dot(points, rotation_matrix)
    return rotated_points

# Animation function
def animate(frame):
    plt.clf()  # Clear the previous frame
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.gca().set_facecolor('black')  # Set background color to black
    rotated_points = update_points(frame)
    plt.scatter(rotated_points[:, 0], rotated_points[:, 1], color='white')
    plt.axis('off')  # Turn off the axes

# Create animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 180), interval=50, blit=False)

# Show the animation
plt.show()
