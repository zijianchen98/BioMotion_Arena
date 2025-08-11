
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights and their initial positions
point_lights = np.array([
    [0, 0.5],  # head
    [-0.2, 0.3],  # left shoulder
    [0.2, 0.3],  # right shoulder
    [-0.2, 0.1],  # left elbow
    [0.2, 0.1],  # right elbow
    [-0.2, -0.1],  # left wrist
    [0.2, -0.1],  # right wrist
    [0, -0.3],  # torso
    [-0.1, -0.5],  # left hip
    [0.1, -0.5],  # right hip
    [-0.1, -0.7],  # left knee
    [0.1, -0.7],  # right knee
    [-0.1, -0.9],  # left ankle
    [0.1, -0.9],  # right ankle
    [0, -1.0]  # feet
])

# Define the movement of each point-light
def update(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    
    # Update the position of each point-light
    for i, light in enumerate(point_lights):
        if i == 0:  # head
            ax.plot(light[0], light[1] + 0.1 * np.sin(frame / 10), 'o', markersize=5, color='white')
        elif i == 1 or i == 2:  # shoulders
            ax.plot(light[0], light[1] + 0.05 * np.sin(frame / 10), 'o', markersize=5, color='white')
        elif i == 3 or i == 4:  # elbows
            ax.plot(light[0], light[1] + 0.1 * np.sin(frame / 10), 'o', markersize=5, color='white')
        elif i == 5 or i == 6:  # wrists
            ax.plot(light[0], light[1] + 0.15 * np.sin(frame / 10), 'o', markersize=5, color='white')
        elif i == 7:  # torso
            ax.plot(light[0], light[1], 'o', markersize=5, color='white')
        elif i == 8 or i == 9:  # hips
            ax.plot(light[0], light[1] + 0.05 * np.sin(frame / 10), 'o', markersize=5, color='white')
        elif i == 10 or i == 11:  # knees
            ax.plot(light[0], light[1] + 0.1 * np.sin(frame / 10), 'o', markersize=5, color='white')
        elif i == 12 or i == 13:  # ankles
            ax.plot(light[0], light[1] + 0.15 * np.sin(frame / 10), 'o', markersize=5, color='white')
        elif i == 14:  # feet
            ax.plot(light[0], light[1] + 0.1 * np.sin(frame / 10), 'o', markersize=5, color='white')

# Create the animation
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
