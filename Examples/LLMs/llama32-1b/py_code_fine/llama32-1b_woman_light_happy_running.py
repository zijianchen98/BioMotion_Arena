
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light source parameters
light_position = np.array([5, 5, 5])  # position in 3D space
light_intensity = 1.0  # intensity of the light source

# Define the subject parameters
subject_position = np.array([0, 0, 0])  # position of the subject in 3D space
subject_velocity = np.array([1.0, 0.0, 0.0])  # velocity of the subject in 3D space
subject_mass = 1.0  # mass of the subject

# Define the action parameters
action_position = np.array([5, 5, 5])  # position of the action in 3D space
action_velocity = np.array([0.5, 0.5, 0.5])  # velocity of the action in 3D space
action_mass = 1.0  # mass of the action

# Define the number of point-lights
num_point_lights = 15

# Define the time step and total time
dt = 0.02
t_total = 10.0

# Define the figure and axis
fig, ax = plt.subplots()

# Initialize the point-lights
point_lights = []
for i in range(num_point_lights):
    # Calculate the position of the point-light
    light_position = np.array([light_position[0] + i * 0.1, light_position[1] + i * 0.1, light_position[2] + i * 0.1])
    
    # Calculate the direction of the point-light
    light_direction = (light_position - subject_position) / np.linalg.norm(light_position - subject_position)
    light_direction = light_direction / np.linalg.norm(light_direction)
    
    # Calculate the intensity of the point-light
    light_intensity = 1.0 + (i / num_point_lights) * 0.1
    
    # Create a point-light object
    point_light = plt.Line2D([0, 0], [0, 0], color='w', lw=2, alpha=light_intensity, label=f'Light {i}')
    
    # Add the point-light to the list of point-lights
    point_lights.append(point_light)
    
    # Add the point-light to the axis
    ax.add_artist(point_light)

# Define the function to update the animation
def update(i):
    # Update the position of the subject
    subject_position += subject_velocity * dt
    
    # Update the position of the action
    action_position += action_velocity * dt
    
    # Update the position of the point-lights
    for point_light in point_lights:
        # Calculate the distance between the point-light and the subject
        distance = np.linalg.norm(subject_position - point_light.get_center())
        
        # Update the position of the point-light
        if distance > 0.1:
            point_light.set_center(np.array([point_light.get_center()[0] + 0.1, point_light.get_center()[1] + 0.1, point_light.get_center()[2] + 0.1]))
    
    # Update the label of the point-light
    for point_light in point_lights:
        point_light.set_label(f'Light {point_light.index+1}')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=int(t_total / dt), interval=dt*1000, blit=True)

# Show the animation
plt.show()
