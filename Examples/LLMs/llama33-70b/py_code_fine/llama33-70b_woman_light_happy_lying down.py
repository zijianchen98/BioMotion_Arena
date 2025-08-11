
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights for the happy woman
point_lights = {
    'head': np.array([0, 1, 0]),  # x, y, z
    'neck': np.array([0, 0.8, 0]),
   'shoulder1': np.array([-0.3, 0.6, 0]),
   'shoulder2': np.array([0.3, 0.6, 0]),
    'elbow1': np.array([-0.4, 0.4, 0]),
    'elbow2': np.array([0.4, 0.4, 0]),
    'wrist1': np.array([-0.5, 0.2, 0]),
    'wrist2': np.array([0.5, 0.2, 0]),
    'hip1': np.array([-0.2, -0.2, 0]),
    'hip2': np.array([0.2, -0.2, 0]),
    'knee1': np.array([-0.2, -0.5, 0]),
    'knee2': np.array([0.2, -0.5, 0]),
    'ankle1': np.array([-0.2, -0.8, 0]),
    'ankle2': np.array([0.2, -0.8, 0]),
}

# Define the motion of the point-lights for the lying down action
def update(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Update the position of each point-light
    for i, (name, point) in enumerate(point_lights.items()):
        # Simulate the lying down motion
        if name in ['head', 'neck','shoulder1','shoulder2']:
            point_lights[name] = np.array([point[0], point[1] - 0.01 * frame, point[2]])
        elif name in ['elbow1', 'elbow2', 'wrist1', 'wrist2']:
            point_lights[name] = np.array([point[0], point[1] - 0.02 * frame, point[2]])
        elif name in ['hip1', 'hip2']:
            point_lights[name] = np.array([point[0], point[1] - 0.03 * frame, point[2]])
        elif name in ['knee1', 'knee2']:
            point_lights[name] = np.array([point[0], point[1] - 0.04 * frame, point[2]])
        elif name in ['ankle1', 'ankle2']:
            point_lights[name] = np.array([point[0], point[1] - 0.05 * frame, point[2]])

        # Plot the point-light
        ax.plot(point_lights[name][0], point_lights[name][1], 'o', markersize=5, color='white')

# Create the animation
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
