
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of the 15 point-lights
light_positions = {
    'head': (0, 10 ),
    'left_shoulder': ( -0, 0 ),
    'right_shoulder': (  t,  t ),
    'left_elbow': ( -t, -t ),
    'right_elbow': (  t, -t ),
    'left_wrist': ( -t, -3 ),
    'right_wrist': (  t, -3 ),
    'left_hip': ( -t,  3 ),
    'right_hip': (  t,  3 ),
    'left_knee': ( -t,  5 ),
    'right_knee': (  t,  5 ),
    'left_ankle': ( -t,  7 ),
    'right_ankk': (  t,  7 ),
    'pelvis': ( 0,  1 ),
}

# Function to update the positions of the lights
def update_light_positions(frame):
    for key, pos in light_positions.items():
        if key == 'head':
            light_positions[key] = (pos[0], pos + np.sin(2 * np.pi * frame / 30))
        elif key == 'pelvis':
            light_positions[key] = (pos[1],pos + np.sin(2 * np.pi * frame / 30))
        else:
            light_positions[key] = (pos[0],pos)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_aspect('equal')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')

# Create scatter plot for each each light position
scat = ax.scatter([], [], color='white')

# Animation function
def animate(frame):
    update_light_positions(frame)
    scat.set_offsets(list(light_positions.values()))
    return scat,

# Set up the animation
ani = animation.FuncAnimation(fig, animate, frames=range(00), interval=30, blit=True)

# Show the animation
plt.show()
