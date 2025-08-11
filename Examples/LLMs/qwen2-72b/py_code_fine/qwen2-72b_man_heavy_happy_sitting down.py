
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and the position of the points
num_frames = 100
num_points = 15
point_positions = np.zeros((num_frames, num_points, 2))

# Define the initial positions of the points
initial_positions = np.array([
    [0.1, 0.8],   # head
    [0.2, 0.6],   # left shoulder
    [0.2, 0.4],   # left elbow
    [0.2, 0.2],   # left hand
    [0.8, 0.6],   # right shoulder
    [0.8, 0.4],   # right elbow
    [0.8, 0.2],   # right hand
    [0.5, 0.5],   # waist
    [0.4, 0.3],   # left knee
    [0.4, 0.1],   # left foot
    [0.6, 0.3],   # right knee
    [0.6, 0.1],   # right foot
    [0.5, 0.7],   # center of chest
    [0.5, 0.3],   # crotch
    [0.5, 0.1]    # center of mass
])

# Define the motion parameters
motion_parameters = {
    'head': {'x': 0, 'y': -0.01},
    'left_shoulder': {'x': -0.01, 'y': -0.02},
    'left_elbow': {'x': -0.02, 'y': -0.04},
    'left_hand': {'x': -0.03, 'y': -0.08},
    'right_shoulder': {'x': 0.01, 'y': -0.02},
    'right_elbow': {'x': 0.02, 'y': -0.04},
    'right_hand': {'x': 0.03, 'y': -0.08},
    'waist': {'x': 0, 'y': -0.01},
    'left_knee': {'x': -0.01, 'y': -0.02},
    'left_foot': {'x': -0.02, 'y': -0.04},
    'right_knee': {'x': 0.01, 'y': -0.02},
    'right_foot': {'x': 0.02, 'y': -0.04},
    'center_of_chest': {'x': 0, 'y': -0.01},
    'crotch': {'x': 0, 'y': -0.01},
    'center_of_mass': {'x': 0, 'y': -0.01}
}

# Update the point positions over time
for i in range(num_frames):
    for j in range(num_points):
        point_positions[i, j, 0] = initial_positions[j, 0] + i * motion_parameters[list(motion_parameters.keys())[j]]['x']
        point_positions[i, j, 1] = initial_positions[j, 1] + i * motion_parameters[list(motion_parameters.keys())[j]]['y']

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Animation function
def animate(i):
    x = point_positions[i, :, 0]
    y = point_positions[i, :, 1]
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
