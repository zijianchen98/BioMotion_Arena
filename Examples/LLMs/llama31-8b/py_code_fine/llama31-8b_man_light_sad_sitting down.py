
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters of the animation
num_lights = 15
light_radius = 0.1
background_color = 'black'

# Define the positions of the lights
lights = np.random.rand(num_lights, 2) * 2 - 1  # Randomly position lights within a 2x2 square

# Define the sitting down motion
def sitting_down(t):
    # Define the joint angles
    shoulder_angle = np.sin(2 * np.pi * t)
    elbow_angle = np.sin(2 * np.pi * t + np.pi / 2)
    wrist_angle = np.sin(2 * np.pi * t + np.pi)

    # Calculate the positions of the lights
    lights[0, :] = [0, 0]  # Shoulder
    lights[1, :] = [np.cos(shoulder_angle), np.sin(shoulder_angle) * 0.5]  # Elbow
    lights[2, :] = [np.cos(shoulder_angle) + np.cos(elbow_angle), np.sin(shoulder_angle) * 0.5 + np.sin(elbow_angle) * 0.3]  # Wrist
    lights[3, :] = [np.cos(shoulder_angle) + np.cos(elbow_angle) + np.cos(wrist_angle), np.sin(shoulder_angle) * 0.5 + np.sin(elbow_angle) * 0.3 + np.sin(wrist_angle) * 0.1]  # Hand
    lights[4, :] = [np.cos(shoulder_angle), -np.sin(shoulder_angle) * 0.5]  # Hip
    lights[5, :] = [np.cos(shoulder_angle) - np.cos(elbow_angle), -np.sin(shoulder_angle) * 0.5 - np.sin(elbow_angle) * 0.3]  # Knee
    lights[6, :] = [np.cos(shoulder_angle) - np.cos(elbow_angle) - np.cos(wrist_angle), -np.sin(shoulder_angle) * 0.5 - np.sin(elbow_angle) * 0.3 - np.sin(wrist_angle) * 0.1]  # Ankle
    lights[7, :] = [-np.cos(shoulder_angle), -np.sin(shoulder_angle) * 0.5]  # Other hip
    lights[8, :] = [-np.cos(shoulder_angle) + np.cos(elbow_angle), -np.sin(shoulder_angle) * 0.5 + np.sin(elbow_angle) * 0.3]  # Other knee
    lights[9, :] = [-np.cos(shoulder_angle) + np.cos(elbow_angle) - np.cos(wrist_angle), -np.sin(shoulder_angle) * 0.5 + np.sin(elbow_angle) * 0.3 - np.sin(wrist_angle) * 0.1]  # Other ankle
    lights[10, :] = [-np.cos(shoulder_angle), np.sin(shoulder_angle) * 0.5]  # Other shoulder
    lights[11, :] = [-np.cos(shoulder_angle) - np.cos(elbow_angle), np.sin(shoulder_angle) * 0.5 + np.sin(elbow_angle) * 0.3]  # Other elbow
    lights[12, :] = [-np.cos(shoulder_angle) - np.cos(elbow_angle) - np.cos(wrist_angle), np.sin(shoulder_angle) * 0.5 + np.sin(elbow_angle) * 0.3 + np.sin(wrist_angle) * 0.1]  # Other wrist
    lights[13, :] = [0, -np.sin(shoulder_angle) * 0.5]  # Other hip
    lights[14, :] = [np.cos(shoulder_angle), -np.sin(shoulder_angle) * 0.5]  # Other hip

    return lights

# Create the figure and axis
fig, ax = plt.subplots()

# Create the initial plot
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor(background_color)
ax.set_axis_off()

# Create the scatter plot of the lights
light_scatter = ax.scatter(lights[:, 0], lights[:, 1], s=light_radius * 200, color='white')

# Define the animation function
def animate(i):
    global light_scatter
    lights = sitting_down(i / 100)
    light_scatter.set_offsets(lights)
    return light_scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, blit=True, interval=20)

plt.show()
