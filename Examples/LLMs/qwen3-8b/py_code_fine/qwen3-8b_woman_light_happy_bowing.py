
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define the body parts and their positions for a happy woman bowing
body_parts = {
    'head': (0, 1),
    'neck': (0, 0.8),
    'shoulder_left': (-0.3, 0.5),
    'shoulder_right': (0.3, 0.5),
    'elbow_left': (-0.4, 0.3),
    'elbow_right': (0.4, 0.3),
    'wrist_left': (-0.5, 0.1),
    'wrist_right': (0.5, 0.1),
    'hip_left': (-0.2, -0.5),
    'hip_right': (0.2, -0.5),
    'knee_left': (-0.3, -0.8),
    'knee_right': (0.3, -0.8),
    'ankle_left': (-0.4, -1.0),
    'ankle_right': (0.4, -1.0),
    'spine': [(0, 1), (0, 0.8), (0, 0.5), (0, 0.3), (0, 0.1), (0, -0.5), (0, -0.8), (0, -1.0)]
}

# Create point-light circles for each body part
lights = {}
for part, pos in body_parts.items():
    if isinstance(pos, list):
        for p in pos:
            lights[(part, p)] = Circle(p, 0.02, color='white')
            ax.add_patch(lights[(part, p)])
    else:
        lights[part] = Circle(pos, 0.02, color='white')
        ax.add_patch(lights[part])

# Define a function to animate the motion
def animate(frame):
    # Define a realistic motion pattern for a happy woman bowing
    # This is a simplified biomechanical model
    t = frame / 60.0  # Time parameter
    head_y = 1 - 0.5 * np.sin(t * 2 * np.pi)
    neck_y = 0.8 - 0.3 * np.sin(t * 2 * np.pi)
    shoulder_left = (-0.3 + 0.1 * np.sin(t * 2 * np.pi), 0.5 + 0.1 * np.cos(t * 2 * np.pi))
    shoulder_right = (0.3 + 0.1 * np.sin(t * 2 * np.pi), 0.5 + 0.1 * np.cos(t * 2 * np.pi))
    elbow_left = (-0.4 + 0.1 * np.sin(t * 2 * np.pi), 0.3 + 0.1 * np.cos(t * 2 * np.pi))
    elbow_right = (0.4 + 0.1 * np.sin(t * 2 * np.pi), 0.3 + 0.1 * np.cos(t * 2 * np.pi))
    wrist_left = (-0.5 + 0.1 * np.sin(t * 2 * np.pi), 0.1 + 0.1 * np.cos(t * 2 * np.pi))
    wrist_right = (0.5 + 0.1 * np.sin(t * 2 * np.pi), 0.1 + 0.1 * np.cos(t * 2 * np.pi))
    hip_left = (-0.2 + 0.1 * np.sin(t * 2 * np.pi), -0.5 + 0.1 * np.cos(t * 2 * np.pi))
    hip_right = (0.2 + 0.1 * np.sin(t * 2 * np.pi), -0.5 + 0.1 * np.cos(t * 2 * np.pi))
    knee_left = (-0.3 + 0.1 * np.sin(t * 2 * np.pi), -0.8 + 0.1 * np.cos(t * 2 * np.pi))
    knee_right = (0.3 + 0.1 * np.sin(t * 2 * np.pi), -0.8 + 0.1 * np.cos(t * 2 * np.pi))
    ankle_left = (-0.4 + 0.1 * np.sin(t * 2 * np.pi), -1.0 + 0.1 * np.cos(t * 2 * np.pi))
    ankle_right = (0.4 + 0.1 * np.sin(t * 2 * np.pi), -1.0 + 0.1 * np.cos(t * 2 * np.pi))

    # Update positions
    lights['head'].center = (0, head_y)
    lights['neck'].center = (0, neck_y)
    lights['shoulder_left'].center = shoulder_left
    lights['shoulder_right'].center = shoulder_right
    lights['elbow_left'].center = elbow_left
    lights['elbow_right'].center = elbow_right
    lights['wrist_left'].center = wrist_left
    lights['wrist_right'].center = wrist_right
    lights['hip_left'].center = hip_left
    lights['hip_right'].center = hip_right
    lights['knee_left'].center = knee_left
    lights['knee_right'].center = knee_right
    lights['ankle_left'].center = ankle_left
    lights['ankle_right'].center = ankle_right

    # Update spine points
    for i, (x, y) in enumerate(body_parts['spine']):
        if i == 0:
            new_y = head_y
        elif i == 1:
            new_y = neck_y
        elif i == 2:
            new_y = 0.5
        elif i == 3:
            new_y = 0.3
        elif i == 4:
            new_y = 0.1
        elif i == 5:
            new_y = -0.5
        elif i == 6:
            new_y = -0.8
        elif i == 7:
            new_y = -1.0
        lights[(body_parts['spine'][i][0], body_parts['spine'][i][1])].center = (x, new_y)

    return lights.values()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=120, interval=50, blit=True)

# Show the animation
plt.show()
