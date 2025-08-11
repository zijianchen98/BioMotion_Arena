
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights for the sad woman with heavy weight
# Each point-light represents a joint in the body
point_lights = [
    np.array([0, 0]),  # head
    np.array([0, -10]),  # left shoulder
    np.array([0, -20]),  # left elbow
    np.array([0, -30]),  # left wrist
    np.array([10, 0]),  # right shoulder
    np.array([10, -10]),  # right elbow
    np.array([10, -20]),  # right wrist
    np.array([0, 10]),  # left hip
    np.array([0, 20]),  # left knee
    np.array([0, 30]),  # left ankle
    np.array([10, 10]),  # right hip
    np.array([10, 20]),  # right knee
    np.array([10, 30]),  # right ankle
    np.array([0, -40]),  # weight in left hand
    np.array([10, -40]),  # weight in right hand
]

# Define the motion parameters for the turning around action
def update_point_lights(frame):
    angle = np.radians(frame)
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    
    updated_point_lights = []
    for point_light in point_lights:
        if point_light[0] == 0:  # left side
            updated_point_light = np.dot(rotation_matrix, point_light)
            updated_point_light[1] -= 10 * np.sin(angle)  # add some sagging motion to the left side
        elif point_light[0] == 10:  # right side
            updated_point_light = np.dot(rotation_matrix, point_light)
            updated_point_light[1] += 10 * np.sin(angle)  # add some sagging motion to the right side
        else:
            updated_point_light = np.dot(rotation_matrix, point_light)
        updated_point_lights.append(updated_point_light)
    
    return updated_point_lights

# Create the animation
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.set_aspect('equal')
ax.axis('off')

def animate(frame):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(-50, 50)
    ax.set_ylim(-50, 50)
    ax.set_aspect('equal')
    ax.axis('off')
    
    updated_point_lights = update_point_lights(frame)
    for point_light in updated_point_lights:
        ax.plot(point_light[0], point_light[1], 'o', markersize=5, color='white')

ani = animation.FuncAnimation(fig, animate, frames=range(0, 360, 10), interval=50)

plt.show()
