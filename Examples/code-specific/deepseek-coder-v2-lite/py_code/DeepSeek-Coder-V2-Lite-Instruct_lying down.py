
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100
light_radius = 0.1

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(0.2, 0.8, num_lights)
positions[:, 1] = 0.5

# Function to update positions
def update_positions(frame_number, positions):
    # Define the motion pattern
    t = frame_number / num_frames
    amplitude = 0.1
    frequency = 2
    phase = 0
    y_motion = amplitude * np.sin(2 * np.pi * frequency * t + phase)
    
    # Update positions
    positions[:, 1] = 0.5 + y_motion
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the lights
lights = []
for i in range(num_lights):
    light = plt.Circle((positions[i, 0], positions[i, 1]), light_radius, color='white')
    lights.append(ax.add_patch(light))

# Create the animation
ani = animation.FuncAnimation(fig, update_positions, fargs=(positions,), frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
