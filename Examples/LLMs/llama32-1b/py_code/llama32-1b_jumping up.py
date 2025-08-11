
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the subject's motion parameters
subject_x = 0
subject_y = 0
subject_z = 0
subject_velocity_x = 0
subject_velocity_y = 0
subject_velocity_z = 0

# Define the action's motion parameters
action_x = 2
action_y = 3
action_z = 4
action_velocity_x = 0
action_velocity_y = 0
action_velocity_z = 0

# Define the point-light parameters
point_light1_x = 0
point_light1_y = 0
point_light1_z = 0
point_light1_intensity = 1.0

point_light2_x = 2
point_light2_y = 0
point_light2_z = 0
point_light2_intensity = 1.0

point_light3_x = 4
point_light3_y = 0
point_light3_z = 0
point_light3_intensity = 1.0

point_light4_x = 6
point_light4_y = 0
point_light4_z = 0
point_light4_intensity = 1.0

point_light5_x = 8
point_light5_y = 0
point_light5_z = 0
point_light5_intensity = 1.0

point_light6_x = 10
point_light6_y = 0
point_light6_z = 0
point_light6_intensity = 1.0

point_light7_x = 12
point_light7_y = 0
point_light7_z = 0
point_light7_intensity = 1.0

point_light8_x = 14
point_light8_y = 0
point_light8_z = 0
point_light8_intensity = 1.0

point_light9_x = 16
point_light9_y = 0
point_light9_z = 0
point_light9_intensity = 1.0

point_light10_x = 18
point_light10_y = 0
point_light10_z = 0
point_light10_intensity = 1.0

point_light11_x = 20
point_light11_y = 0
point_light11_z = 0
point_light11_intensity = 1.0

point_light12_x = 22
point_light12_y = 0
point_light12_z = 0
point_light12_intensity = 1.0

point_light13_x = 24
point_light13_y = 0
point_light13_z = 0
point_light13_intensity = 1.0

point_light14_x = 26
point_light14_y = 0
point_light14_z = 0
point_light14_intensity = 1.0

point_light15_x = 28
point_light15_y = 0
point_light15_z = 0
point_light15_intensity = 1.0

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize the axis with a black background
ax.set_facecolor('black')

# Define the point-light positions
point_light_positions = [
    (point_light1_x, point_light1_y, point_light1_z),
    (point_light2_x, point_light2_y, point_light2_z),
    (point_light3_x, point_light3_y, point_light3_z),
    (point_light4_x, point_light4_y, point_light4_z),
    (point_light5_x, point_light5_y, point_light5_z),
    (point_light6_x, point_light6_y, point_light6_z),
    (point_light7_x, point_light7_y, point_light7_z),
    (point_light8_x, point_light8_y, point_light8_z),
    (point_light9_x, point_light9_y, point_light9_z),
    (point_light10_x, point_light10_y, point_light10_z),
    (point_light11_x, point_light11_y, point_light11_z),
    (point_light12_x, point_light12_y, point_light12_z),
    (point_light13_x, point_light13_y, point_light13_z),
    (point_light14_x, point_light14_y, point_light14_z),
    (point_light15_x, point_light15_y, point_light15_z),
]

# Define the action's position
action_position = (action_x, action_y, action_z)

# Define the velocity parameters
subject_velocity = np.array([subject_velocity_x, subject_velocity_y, subject_velocity_z])
action_velocity = np.array([action_velocity_x, action_velocity_y, action_velocity_z])

# Function to update the plot
def update(frame):
    global subject_x, subject_y, subject_z, subject_velocity_x, subject_velocity_y, subject_velocity_z
    global action_x, action_y, action_z, action_velocity_x, action_velocity_y, action_velocity_z
    global point_light_positions, action_position
    
    # Update the subject's position
    subject_x += subject_velocity_x * 0.01
    subject_y += subject_velocity_y * 0.01
    subject_z += subject_velocity_z * 0.01
    
    # Update the action's position
    action_x += action_velocity_x * 0.01
    action_y += action_velocity_y * 0.01
    action_z += action_velocity_z * 0.01
    
    # Update the point-light positions
    for i in range(len(point_light_positions)):
        point_light_positions[i] = (point_light_positions[i][0] + action_x * 0.01, 
                                   point_light_positions[i][1] + action_y * 0.01, 
                                   point_light_positions[i][2] + action_z * 0.01)
    
    # Update the axis limits
    ax.set_xlim(-50, 50)
    ax.set_ylim(-50, 50)
    ax.set_zlim(-50, 50)
    
    # Draw the point-lights
    for i in range(len(point_light_positions)):
        ax.scatter(point_light_positions[i][0], point_light_positions[i][1], 
                  point_light_positions[i][2], s=100, c='w', alpha=0.5)
    
    # Draw the action
    ax.scatter(action_position[0], action_position[1], action_position[2], s=100, c='r', alpha=0.5)
    
    # Update the axis
    plt.xlim(-50, 50)
    plt.ylim(-50, 50)
    plt.zlim(-50, 50)
    plt.pause(0.01)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=16)

plt.show()
