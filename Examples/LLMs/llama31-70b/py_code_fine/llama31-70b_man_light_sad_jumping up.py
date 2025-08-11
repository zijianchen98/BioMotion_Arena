
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights for the sadman with light weight
lights = {
    'head': [0, 0],
   'shoulder_left': [-0.2, 0.3],
   'shoulder_right': [0.2, 0.3],
    'elbow_left': [-0.4, 0.1],
    'elbow_right': [0.4, 0.1],
    'wrist_left': [-0.6, -0.2],
    'wrist_right': [0.6, -0.2],
    'hip_left': [-0.2, -0.3],
    'hip_right': [0.2, -0.3],
    'knee_left': [-0.4, -0.6],
    'knee_right': [0.4, -0.6],
    'ankle_left': [-0.6, -0.9],
    'ankle_right': [0.6, -0.9],
    'toe_left': [-0.8, -1.2],
    'toe_right': [0.8, -1.2],
}

# Define the animation frames
frames = 60
jump_amplitude = 0.2
jump_frequency = 0.1

# Create a new figure
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1.5, 0.5)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the plot
plot, = ax.plot([], [], 'o', markersize=5, color='white')

# Animation function
def animate(i):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1.5, 0.5)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Calculate the new positions of the point-lights
    new_positions = []
    for light, position in lights.items():
        if light in ['head','shoulder_left','shoulder_right']:
            new_position = [position[0], position[1] + jump_amplitude * np.sin(i * jump_frequency)]
        elif light in ['elbow_left', 'elbow_right', 'wrist_left', 'wrist_right']:
            new_position = [position[0], position[1] + jump_amplitude * np.sin(i * jump_frequency + np.pi/2)]
        elif light in ['hip_left', 'hip_right']:
            new_position = [position[0], position[1] + jump_amplitude * np.sin(i * jump_frequency + np.pi)]
        elif light in ['knee_left', 'knee_right', 'ankle_left', 'ankle_right']:
            new_position = [position[0], position[1] + jump_amplitude * np.sin(i * jump_frequency + np.pi*1.5)]
        else:
            new_position = [position[0], position[1] + jump_amplitude * np.sin(i * jump_frequency + np.pi*2)]
        new_positions.append(new_position)

    # Plot the new positions
    x = [position[0] for position in new_positions]
    y = [position[1] for position in new_positions]
    plot = ax.plot(x, y, 'o', markersize=5, color='white')
    return plot,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=frames, blit=True, interval=50)

plt.show()
