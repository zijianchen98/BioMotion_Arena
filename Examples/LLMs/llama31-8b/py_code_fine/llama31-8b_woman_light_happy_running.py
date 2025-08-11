
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and the frame rate
num_frames = 100
frame_rate = 30

# Define the animation parameters
num_lights = 15
light_radius = 5
light_color = 'white'
background_color = 'black'
subject_color = 'blue'

# Define the subject's motion parameters
subject_position = np.zeros((num_frames, 2))
subject_velocity = np.array([2, 2])  # pixels per frame
subject_acceleration = np.array([0, 0])  # pixels per frame^2

# Initialize the light positions
light_positions = np.random.rand(num_lights, 2) * 200 - 100  # random positions between -100 and 100 pixels

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize the plot
ax.set_xlim(-150, 150)
ax.set_ylim(-150, 150)
ax.set_aspect('equal')
ax.set_facecolor(background_color)

# Function to update the plot
def update(frame):
    global subject_position, light_positions

    # Update the subject's position
    subject_position[frame] = subject_position[frame-1] + subject_velocity

    # Update the light positions
    light_positions[:, 0] += np.sin(frame/10 + np.arange(num_lights))  # move lights in a sinusoidal pattern
    light_positions[:, 1] += np.cos(frame/10 + np.arange(num_lights))  # move lights in a sinusoidal pattern

    # Clear the previous frame
    ax.clear()

    # Set the axis limits and aspect ratio
    ax.set_xlim(-150, 150)
    ax.set_ylim(-150, 150)
    ax.set_aspect('equal')

    # Plot the subject
    ax.plot(subject_position[frame, 0], subject_position[frame, 1], 'o', color=subject_color, markersize=10)

    # Plot the lights
    for i in range(num_lights):
        ax.plot(light_positions[i, 0], light_positions[i, 1], 'o', color=light_color, markersize=light_radius)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000/frame_rate)

# Display the animation
plt.show()
