
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters for the point lights
light1 = {'x': 0, 'y': 0, 'z': 0, 'color': (1, 1, 1), 'radius': 5, 'intensity': 1}
light2 = {'x': 0, 'y': 0, 'z': 0, 'color': (1, 1, 1), 'radius': 5, 'intensity': 1}
light3 = {'x': 0, 'y': 0, 'z': 0, 'color': (1, 1, 1), 'radius': 5, 'intensity': 1}
light4 = {'x': 0, 'y': 0, 'z': 0, 'color': (1, 1, 1), 'radius': 5, 'intensity': 1}
light5 = {'x': 0, 'y': 0, 'z': 0, 'color': (1, 1, 1), 'radius': 5, 'intensity': 1}
light6 = {'x': 0, 'y': 0, 'z': 0, 'color': (1, 1, 1), 'radius': 5, 'intensity': 1}
light7 = {'x': 0, 'y': 0, 'z': 0, 'color': (1, 1, 1), 'radius': 5, 'intensity': 1}
light8 = {'x': 0, 'y': 0, 'z': 0, 'color': (1, 1, 1), 'radius': 5, 'intensity': 1}
light9 = {'x': 0, 'y': 0, 'z': 0, 'color': (1, 1, 1), 'radius': 5, 'intensity': 1}
light10 = {'x': 0, 'y': 0, 'z': 0, 'color': (1, 1, 1), 'radius': 5, 'intensity': 1}
light11 = {'x': 0, 'y': 0, 'z': 0, 'color': (1, 1, 1), 'radius': 5, 'intensity': 1}
light12 = {'x': 0, 'y': 0, 'z': 0, 'color': (1, 1, 1), 'radius': 5, 'intensity': 1}
light13 = {'x': 0, 'y': 0, 'z': 0, 'color': (1, 1, 1), 'radius': 5, 'intensity': 1}
light14 = {'x': 0, 'y': 0, 'z': 0, 'color': (1, 1, 1), 'radius': 5, 'intensity': 1}
light15 = {'x': 0, 'y': 0, 'z': 0, 'color': (1, 1, 1), 'radius': 5, 'intensity': 1}

# Define the parameters for the subject
subject = {'x': 0, 'y': 0, 'z': 0, 'color': (1, 1, 1), 'radius': 0, 'intensity': 1}

# Define the parameters for the action
action = {'x': 0, 'y': 0, 'z': 0, 'color': (1, 1, 1), 'radius': 0, 'intensity': 1}

# Define the parameters for the movement
movement = {'x': 0, 'y': 0, 'z': 0, 'color': (1, 1, 1), 'radius': 0, 'intensity': 1}

# Define the parameters for the background
background = {'x': 0, 'y': 0, 'z': 0, 'color': (0, 0, 0), 'radius': 100, 'intensity': 1}

# Define the parameters for the camera
camera = {'x': 0, 'y': 0, 'z': 0, 'color': (1, 1, 1), 'radius': 100, 'intensity': 1}

# Create a figure and a 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the points for the subject
subject_points = np.array([
    [0, 0, 0],
    [0, 0, 10],
    [0, 10, 10],
    [0, 10, 0],
    [10, 0, 10],
    [10, 0, 0],
    [10, 10, 10],
    [10, 10, 0],
])

# Define the points for the action
action_points = np.array([
    [0, 0, 0],
    [0, 0, 10],
    [0, 10, 10],
    [0, 10, 0],
    [10, 0, 10],
    [10, 0, 0],
    [10, 10, 10],
    [10, 10, 0],
])

# Define the points for the movement
movement_points = np.array([
    [0, 0, 0],
    [0, 0, 10],
    [0, 10, 10],
    [0, 10, 0],
    [10, 0, 10],
    [10, 0, 0],
    [10, 10, 10],
    [10, 10, 0],
])

# Define the points for the background
background_points = np.array([
    [0, 0, 0],
    [0, 0, 100],
    [0, 100, 100],
    [100, 100, 100],
    [100, 0, 100],
    [0, 0, 0],
    [0, 0, 100],
    [0, 100, 100],
    [0, 100, 0],
])

# Define the points for the camera
camera_points = np.array([
    [0, 0, 0],
    [0, 0, 100],
    [0, 100, 100],
    [100, 100, 100],
    [100, 0, 100],
    [0, 0, 0],
    [0, 0, 100],
    [0, 100, 100],
    [0, 100, 0],
])

# Define the points for the lights
light_points = [light1, light2, light3, light4, light5, light6, light7, light8, light9, light10, light11, light12, light13, light14, light15]

# Define the colors for the lights and the subject
light_colors = [(1, 1, 1) for _ in light_points]
subject_color = (1, 1, 1)
action_color = (1, 1, 1)
movement_color = (1, 1, 1)
background_color = (0, 0, 0)
camera_color = (1, 1, 1)

# Define the movement parameters
movement_speed = 0.01

# Define the camera parameters
camera_fov = 90

# Define the animation parameters
animation_speed = 0.1

# Initialize the animation
animation = 0

# Define the animation loop
while True:
    # Clear the axes
    ax.clear()

    # Set the axis limits
    ax.set_xlim(-200, 200)
    ax.set_ylim(-200, 200)
    ax.set_zlim(-200, 200)

    # Set the camera position and orientation
    ax.set_xlim(-200, 200)
    ax.set_ylim(-200, 200)
    ax.set_zlim(-200, 200)
    ax.set_aspect('equal')
    ax.view_init(elev=45, azim=90)

    # Set the background color
    ax.set_facecolor(background_color)

    # Set the camera position
    ax.set_position([0, 0, 0])

    # Draw the subject
    for point in subject_points:
        ax.plot3D(*zip(point, subject_color), c=subject_color, linewidth=1, label='Subject')

    # Draw the action
    for point in action_points:
        ax.plot3D(*zip(point, action_color), c=action_color, linewidth=1, label='Action')

    # Draw the movement
    for point in movement_points:
        ax.plot3D(*zip(point, movement_color), c=movement_color, linewidth=1, label='Movement')

    # Draw the lights
    for point in light_points:
        ax.plot3D(*zip(point.x, point.y, point.z, light_colors[point.id]), c=light_colors[point.id], linewidth=1, label='Light')

    # Draw the camera
    ax.plot3D(*zip(camera_points[0].x, camera_points[0].y, camera_points[0].z, camera_color), c=camera_color, linewidth=1, label='Camera')

    # Update the camera position
    camera.x += movement_speed
    camera.y += movement_speed
    camera.z += movement_speed

    # Set the limits of the camera position
    camera.x = max(-200, min(200, camera.x))
    camera.y = max(-200, min(200, camera.y))
    camera.z = max(-200, min(200, camera.z))

    # Set the labels and title
    ax.set_title('Sadman Jumping Up')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set.legend()

    # Update the plot
    plt.pause(animation_speed)
    animation += animation_speed

    # If the animation is over, stop it
    if animation >= 10:
        break
