
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights for the sad woman
point_lights = [
    # Head
    np.array([0, 10]),
    np.array([2, 12]),
    np.array([-2, 12]),
    # Shoulders
    np.array([-5, 5]),
    np.array([5, 5]),
    # Elbows
    np.array([-8, 0]),
    np.array([8, 0]),
    # Wrists
    np.array([-10, -2]),
    np.array([10, -2]),
    # Hips
    np.array([-3, -5]),
    np.array([3, -5]),
    # Knees
    np.array([-4, -10]),
    np.array([4, -10]),
    # Ankles
    np.array([-5, -15]),
    np.array([5, -15])
]

# Define the motion of the point-lights for the "lying down" action
def animate(frame):
    # Move the point-lights to simulate the "lying down" action
    animated_point_lights = []
    for i, point_light in enumerate(point_lights):
        if i < 3:  # Head
            animated_point_light = point_light + np.array([0, -frame / 10])
        elif i < 5:  # Shoulders
            animated_point_light = point_light + np.array([0, -frame / 10])
        elif i < 7:  # Elbows
            animated_point_light = point_light + np.array([0, -frame / 10])
        elif i < 9:  # Wrists
            animated_point_light = point_light + np.array([0, -frame / 10])
        elif i < 11:  # Hips
            animated_point_light = point_light + np.array([0, -frame / 10])
        elif i < 13:  # Knees
            animated_point_light = point_light + np.array([0, -frame / 10])
        else:  # Ankles
            animated_point_light = point_light + np.array([0, -frame / 10])
        animated_point_lights.append(animated_point_light)
    
    # Update the plot
    plt.cla()
    plt.xlim(-15, 15)
    plt.ylim(-20, 15)
    plt.axis('off')
    plt.gca().set_facecolor('black')
    plt.scatter(*zip(*animated_point_lights), c='white', s=50)

# Create the animation
ani = animation.FuncAnimation(plt.gcf(), animate, frames=range(100), interval=50)

plt.show()
