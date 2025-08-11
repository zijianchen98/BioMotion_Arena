
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_points = 15

# Define the angles for the points
angles = np.linspace(0, 2*np.pi - np.pi/2, num_points)

# Define the center of the animation
circle_radius = 1.25

# Define the time points for the animation
time = np.linspace(0, 2*np.pi, 60)

# Define positions for the man's joints and head
joint_positions = {
    'head': np.array([circle_radius * np.cos(angles[-1]), circle_radius * np.sin(angles[-1]), 0]),
    'knee': np.array([circle_radius * np.cos(angles[7]), circle_radius * np.sin(angles[7]), 0]),
    'hip': np.array([circle_radius * np.cos(angles[0]), circle_radius * np.sin(angles[0]), 0]),
    'foot': np.array([circle_radius * np.cos(angles[0]), circle_radius * np.sin(angles[0]), 0])
}

# Initialize the figure
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.axis('off')

# Create the points
points = [ax.plot([], [], 'o', color='white')[0] for _ in range(num_points)]

def init():
    for point in points:
        point.set_data([], [])
    return points

def update(frame):
    global joint_positions
    time_angle = time[frame] % (2*np.pi)
    
    for i in range(num_points):
        angle = angles[i] + time_angle
        points[i].set_data(circle_radius * np.cos(angle), circle_radius * np.sin(angle))
    
    joint_positions['hip'] = np.array([circle_radius * np.cos(time_angle), circle_radius * np.sin(time_angle), 0])
    joint_positions['knee'] = np.array([circle_radius * np.cos(time_angle), circle_radius * np.sin(time_angle) + 0.2, 0])
    joint_positions['foot'] = np.array([circle_radius * np.cos(time_angle), circle_radius * np.sin(time_angle) + 0.3, 0])
    joint_positions['head'] = np.array([circle_radius * np.cos(time_angle), circle_radius * np.sin(time_angle) + 0.7, 0])

    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, init_func=init, blit=True, repeat=True)
plt.show()
