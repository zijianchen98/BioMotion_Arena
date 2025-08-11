
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light positions for the sad man with heavy weight
# The points are defined as (x, y) coordinates
point_lights = {
    'head': (0, 10),
    'left_shoulder': (-2, 8),
    'right_shoulder': (2, 8),
    'left_elbow': (-3, 5),
    'right_elbow': (3, 5),
    'left_hand': (-4, 2),
    'right_hand': (4, 2),
    'left_hip': (-2, 0),
    'right_hip': (2, 0),
    'left_knee': (-2, -2),
    'right_knee': (2, -2),
    'left_ankle': (-2, -4),
    'right_ankle': (2, -4),
    'left_foot': (-2, -6),
    'right_foot': (2, -6)
}

# Define the movement parameters for the walking action
# The movement is defined as a sinusoidal function
def move_point_light(point, t, amplitude, frequency, phase):
    x, y = point
    return x + amplitude * np.sin(2 * np.pi * frequency * t + phase), y

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_facecolor('black')
    ax.set_aspect('equal')
    
    # Move the point-lights
    t = i / 10.0  # time
    points = {
        'head': move_point_light(point_lights['head'], t, 0.5, 0.5, 0),
        'left_shoulder': move_point_light(point_lights['left_shoulder'], t, 1.0, 0.5, np.pi / 2),
        'right_shoulder': move_point_light(point_lights['right_shoulder'], t, 1.0, 0.5, -np.pi / 2),
        'left_elbow': move_point_light(point_lights['left_elbow'], t, 1.5, 1.0, np.pi / 2),
        'right_elbow': move_point_light(point_lights['right_elbow'], t, 1.5, 1.0, -np.pi / 2),
        'left_hand': move_point_light(point_lights['left_hand'], t, 2.0, 1.5, np.pi / 2),
        'right_hand': move_point_light(point_lights['right_hand'], t, 2.0, 1.5, -np.pi / 2),
        'left_hip': move_point_light(point_lights['left_hip'], t, 1.0, 0.5, np.pi / 2),
        'right_hip': move_point_light(point_lights['right_hip'], t, 1.0, 0.5, -np.pi / 2),
        'left_knee': move_point_light(point_lights['left_knee'], t, 1.5, 1.0, np.pi / 2),
        'right_knee': move_point_light(point_lights['right_knee'], t, 1.5, 1.0, -np.pi / 2),
        'left_ankle': move_point_light(point_lights['left_ankle'], t, 2.0, 1.5, np.pi / 2),
        'right_ankle': move_point_light(point_lights['right_ankle'], t, 2.0, 1.5, -np.pi / 2),
        'left_foot': move_point_light(point_lights['left_foot'], t, 2.5, 2.0, np.pi / 2),
        'right_foot': move_point_light(point_lights['right_foot'], t, 2.5, 2.0, -np.pi / 2)
    }
    
    # Plot the point-lights
    for point in points.values():
        ax.plot(point[0], point[1], 'o', markersize=5, color='white')

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
