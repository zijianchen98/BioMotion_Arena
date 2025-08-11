
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters for the point-light stimulus
num_point_lights = 15
light_distance = 5.0
light_angle_step = np.pi / 180.0  # Convert degrees to radians

# Define the parameters for the subject and action
subject_x = 0.0
subject_y = 0.0
subject_z = 0.0
subject_speed_x = 0.0
subject_speed_y = 0.0
subject_speed_z = 0.0

# Define the parameters for the animation
frame_rate = 30.0  # Frames per second
duration = 10.0  # Seconds

# Create a figure and axis object
fig, ax = plt.subplots()

# Define the point-lights
light_positions = []
for i in range(num_point_lights):
    light_angle = i * light_angle_step
    light_x = subject_x + np.cos(light_angle) * light_distance
    light_y = subject_y + np.sin(light_angle) * light_distance
    light_z = subject_z
    light_positions.append([light_x, light_y, light_z])

# Create a scatter plot for the point-lights
scatter = ax.scatter(light_positions, [], c='white', s=1, zorder=0)

# Define the animation function
def animate(i):
    global subject_x, subject_y, subject_z, subject_speed_x, subject_speed_y, subject_speed_z
    subject_x += subject_speed_x * i
    subject_y += subject_speed_y * i
    subject_z += subject_speed_z * i
    
    # Update the scatter plot
    scatter.set_offsets([[light_x, light_y, light_z] for light_x, light_y, light_z in light_positions])
    
    # Ensure the subject stays within the solid black background
    if subject_x < -5.0:
        subject_x = -5.0
    elif subject_x > 5.0:
        subject_x = 5.0
    if subject_y < -5.0:
        subject_y = -5.0
    elif subject_y > 5.0:
        subject_y = 5.0
    if subject_z < -5.0:
        subject_z = -5.0
    elif subject_z > 5.0:
        subject_z = 5.0
    
    # Set the axis limits
    ax.set_xlim(-5.0, 5.0)
    ax.set_ylim(-5.0, 5.0)
    ax.set_zlim(-5.0, 5.0)
    
    # Set the axis labels
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')
    
    # Set the axis limits
    ax.set_xlim(-5.0, 5.0)
    ax.set_ylim(-5.0, 5.0)
    ax.set_zlim(-5.0, 5.0)
    
    # Set the axis labels
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=int(duration / frame_rate), interval=1000 // frame_rate)

# Show the animation
plt.show()
