
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters of the subject
subject_x = 0
subject_y = 0
subject_z = 0

# Define the parameters of the action
action_x = 1
action_y = 1
action_z = 1

# Define the parameters of the point lights
point_light_x = 1
point_light_y = 1
point_light_z = 1
point_light_radius = 0.1

# Define the parameters of the camera
camera_x = 0
camera_y = 0
camera_z = 10

# Define the parameters of the animation
animation_frame = 0
animation_speed = 0.01
animation_duration = 30  # seconds

# Create a figure and a 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the points of the subject
subject_points = np.array([
    [subject_x, subject_y, subject_z],
    [subject_x + 0.2, subject_y + 0.2, subject_z],
    [subject_x + 0.4, subject_y + 0.2, subject_z],
    [subject_x + 0.6, subject_y + 0.2, subject_z],
    [subject_x + 0.8, subject_y + 0.2, subject_z],
    [subject_x + 1.0, subject_y + 0.2, subject_z],
    [subject_x + 1.2, subject_y + 0.2, subject_z],
    [subject_x + 1.4, subject_y + 0.2, subject_z],
    [subject_x + 1.6, subject_y + 0.2, subject_z],
    [subject_x + 1.8, subject_y + 0.2, subject_z],
    [subject_x + 2.0, subject_y + 0.2, subject_z]
])

# Define the points of the action
action_points = np.array([
    [action_x, action_y, action_z],
    [action_x + 0.2, action_y + 0.2, action_z],
    [action_x + 0.4, action_y + 0.2, action_z],
    [action_x + 0.6, action_y + 0.2, action_z],
    [action_x + 0.8, action_y + 0.2, action_z],
    [action_x + 1.0, action_y + 0.2, action_z],
    [action_x + 1.2, action_y + 0.2, action_z],
    [action_x + 1.4, action_y + 0.2, action_z],
    [action_x + 1.6, action_y + 0.2, action_z],
    [action_x + 1.8, action_y + 0.2, action_z],
    [action_x + 2.0, action_y + 0.2, action_z]
])

# Define the points of the point lights
point_light_points = np.array([
    [point_light_x, point_light_y, point_light_z],
    [point_light_x + point_light_radius, point_light_y, point_light_z],
    [point_light_x + 2*point_light_radius, point_light_y, point_light_z],
    [point_light_x + 3*point_light_radius, point_light_y, point_light_z],
    [point_light_x + 4*point_light_radius, point_light_y, point_light_z],
    [point_light_x + 5*point_light_radius, point_light_y, point_light_z],
    [point_light_x + 6*point_light_radius, point_light_y, point_light_z],
    [point_light_x + 7*point_light_radius, point_light_y, point_light_z],
    [point_light_x + 8*point_light_radius, point_light_y, point_light_z],
    [point_light_x + 9*point_light_radius, point_light_y, point_light_z],
    [point_light_x + 10*point_light_radius, point_light_y, point_light_z]
])

# Create the line segments between the points of the subject and action
for i in range(len(subject_points)):
    ax.plot3D(subject_points[i], subject_points[(i+1)%len(subject_points)], subject_points[(i+2)%len(subject_points)], 'b-')

for i in range(len(action_points)):
    ax.plot3D(action_points[i], action_points[(i+1)%len(action_points)], action_points[(i+2)%len(action_points)], 'b-')

# Create the line segments between the points of the point lights
for i in range(len(point_light_points)):
    ax.plot3D(point_light_points[i], point_light_points[(i+1)%len(point_light_points)], point_light_points[(i+2)%len(point_light_points)], 'r-')

# Set the limits of the axes
ax.set_xlim(-1.0, 2.0)
ax.set_ylim(-1.0, 2.0)
ax.set_zlim(-1.0, 2.0)

# Set the axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the title of the animation
ax.set_title('Happyman with Forward Rolling')

# Animate the points of the subject and action
for i in range(100):
    ax.clear()
    ax.set_xlim(-1.0, 2.0)
    ax.set_ylim(-1.0, 2.0)
    ax.set_zlim(-1.0, 2.0)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.plot3D(subject_points[i], subject_points[(i+1)%len(subject_points)], subject_points[(i+2)%len(subject_points)], 'b-')
    ax.plot3D(action_points[i], action_points[(i+1)%len(action_points)], action_points[(i+2)%len(action_points)], 'b-')
    ax.plot3D(point_light_points[i], point_light_points[(i+1)%len(point_light_points)], point_light_points[(i+2)%len(point_light_points)], 'r-')
    ax.set_title(f'Frame {i+1}')
    plt.pause(animation_speed)

# Show the animation
plt.show()
