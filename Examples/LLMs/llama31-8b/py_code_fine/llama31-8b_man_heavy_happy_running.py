
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Define the point lights
lights = {
    'head': [0, 0],
   'shoulder': [0, -100],
    'elbow': [-50, -150],
    'wrist': [-100, -200],
    'hand': [-150, -250],
    'hip': [0, 100],
    'knee': [50, 150],
    'ankle': [100, 200],
    'foot': [150, 250],
   'shoulder2': [0, -50],
    'elbow2': [-25, -125],
    'wrist2': [-75, -225],
    'hand2': [-125, -325],
    'hip2': [0, 50],
    'knee2': [25, 125],
    'ankle2': [75, 225],
    'foot2': [125, 325]
}

# Define the animation parameters
num_points = len(lights)
num_frames = 60  # 1 second at 60 FPS
frame_rate = 60
frame_duration = 1000 / frame_rate

# Initialize the plot
ax.set_xlim(-200, 200)
ax.set_ylim(-300, 300)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_axis_off()

# Define the animation function
def animate(frame):
    ax.clear()
    ax.set_xlim(-200, 200)
    ax.set_ylim(-300, 300)
    ax.set_facecolor('black')
    ax.set_aspect('equal')
    ax.set_axis_off()

    # Calculate the current pose
    t = frame / num_frames
    poses = [
        {'hip': [0, 100 * np.sin(2 * np.pi * 2 * t)],
         'knee': [50, 150 + 100 * np.sin(2 * np.pi * 2 * t)],
         'ankle': [100, 200 + 100 * np.sin(2 * np.pi * 2 * t)],
         'foot': [150, 250 + 100 * np.sin(2 * np.pi * 2 * t)]},
        {'hip': [0, 100 * np.sin(2 * np.pi * 2 * t)],
         'knee': [25, 125 + 100 * np.sin(2 * np.pi * 2 * t)],
         'ankle': [75, 225 + 100 * np.sin(2 * np.pi * 2 * t)],
         'foot': [125, 325 + 100 * np.sin(2 * np.pi * 2 * t)]},
        {'hip': [0, 50 * np.sin(2 * np.pi * 1.5 * t)],
         'knee': [-50, 150 + 50 * np.sin(2 * np.pi * 1.5 * t)],
         'ankle': [-100, 200 + 50 * np.sin(2 * np.pi * 1.5 * t)],
         'foot': [-150, 250 + 50 * np.sin(2 * np.pi * 1.5 * t)]},
        {'hip': [0, 50 * np.sin(2 * np.pi * 1.5 * t)],
         'knee': [-75, 125 + 50 * np.sin(2 * np.pi * 1.5 * t)],
         'ankle': [-125, 225 + 50 * np.sin(2 * np.pi * 1.5 * t)],
         'foot': [-175, 325 + 50 * np.sin(2 * np.pi * 1.5 * t)]}
    ]

    # Plot the point lights
    for i, (key, pos) in enumerate(lights.items()):
        ax.plot(pos[0] + poses[i]['hip'][0], pos[1] + poses[i]['hip'][1], 'o', color='white')
        ax.plot(pos[0] + poses[i]['knee'][0], pos[1] + poses[i]['knee'][1], 'o', color='white')
        ax.plot(pos[0] + poses[i]['ankle'][0], pos[1] + poses[i]['ankle'][1], 'o', color='white')
        ax.plot(pos[0] + poses[i]['foot'][0], pos[1] + poses[i]['foot'][1], 'o', color='white')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=frame_duration, blit=False)

# Display the animation
plt.show()
