
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100
arm_length = 1.0
wrist_radius = 0.1
hand_radius = 0.2

# Initialize positions
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(-arm_length, arm_length, num_lights)
positions[:, 1] = -arm_length * np.ones(num_lights)

# Create figure
fig, ax = plt.subplots()
ax.set_xlim(-arm_length - hand_radius, arm_length + hand_radius)
ax.set_ylim(-arm_length - hand_radius, arm_length + hand_radius)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize lights
lights = []
for i in range(num_lights):
    light = plt.Circle((positions[i, 0], positions[i, 1]), wrist_radius, color='white')
    lights.append(ax.add_patch(light))

# Function to update positions
def update(frame):
    angle = 2 * np.pi * frame / num_frames
    shoulder_x = 0.0
    shoulder_y = arm_length
    wrist_x = shoulder_x + arm_length * np.cos(angle)
    wrist_y = shoulder_y + arm_length * np.sin(angle)
    
    positions[:, 0] = np.linspace(shoulder_x, wrist_x, num_lights)
    positions[:, 1] = np.linspace(shoulder_y, wrist_y, num_lights)
    
    for i, light in enumerate(lights):
        light.center = (positions[i, 0], positions[i, 1])

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=False, repeat=True)

# Show animation
plt.show()
