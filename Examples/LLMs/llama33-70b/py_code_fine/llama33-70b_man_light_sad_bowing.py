
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights for the sad man
point_lights = {
    'head': [0, 1.5],
    'neck': [0, 1.2],
    'left_shoulder': [-0.5, 1.0],
    'right_shoulder': [0.5, 1.0],
    'left_elbow': [-0.7, 0.5],
    'right_elbow': [0.7, 0.5],
    'left_wrist': [-0.9, 0.0],
    'right_wrist': [0.9, 0.0],
    'left_hip': [-0.3, -0.5],
    'right_hip': [0.3, -0.5],
    'left_knee': [-0.3, -1.0],
    'right_knee': [0.3, -1.0],
    'left_ankle': [-0.3, -1.5],
    'right_ankle': [0.3, -1.5],
    'torso': [0, 0.0]
}

# Define the bowing action
def bowing_action(frame):
    angle = np.radians(frame)
    bowing_factor = 0.5 * np.sin(angle)
    
    # Update point-light positions
    updated_point_lights = {
        'head': [0, 1.5 - bowing_factor],
        'neck': [0, 1.2 - bowing_factor],
        'left_shoulder': [-0.5, 1.0 - bowing_factor],
        'right_shoulder': [0.5, 1.0 - bowing_factor],
        'left_elbow': [-0.7, 0.5 - bowing_factor],
        'right_elbow': [0.7, 0.5 - bowing_factor],
        'left_wrist': [-0.9, 0.0 - bowing_factor],
        'right_wrist': [0.9, 0.0 - bowing_factor],
        'left_hip': [-0.3, -0.5 - bowing_factor],
        'right_hip': [0.3, -0.5 - bowing_factor],
        'left_knee': [-0.3, -1.0 - bowing_factor],
        'right_knee': [0.3, -1.0 - bowing_factor],
        'left_ankle': [-0.3, -1.5 - bowing_factor],
        'right_ankle': [0.3, -1.5 - bowing_factor],
        'torso': [0, 0.0 - bowing_factor]
    }
    
    return updated_point_lights

# Create a new figure
fig, ax = plt.subplots()

# Initialize the point-lights
point_light_x = [point_lights[key][0] for key in point_lights]
point_light_y = [point_lights[key][1] for key in point_lights]

# Plot the initial point-lights
ax.scatter(point_light_x, point_light_y, color='white', s=50)

# Set the background color to black
ax.set_facecolor('black')

# Set the axis limits
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2.0, 2.0)

# Remove the axis ticks
ax.set_xticks([])
ax.set_yticks([])

# Define the animation function
def animate(frame):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-2.0, 2.0)
    ax.set_xticks([])
    ax.set_yticks([])
    
    updated_point_lights = bowing_action(frame)
    point_light_x = [updated_point_lights[key][0] for key in updated_point_lights]
    point_light_y = [updated_point_lights[key][1] for key in updated_point_lights]
    
    ax.scatter(point_light_x, point_light_y, color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(0, 360), interval=50)

plt.show()
