
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and the figure
num_points = 15
point_lights = np.zeros((num_points, 2))

# Initialize the positions for the point-lights
# Define static positions for the points representing human body parts
point_lights[0] = [0, 2]    # head
point_lights[1] = [-0.5, 1.5]  # left shoulder
point_lights[2] = [0.5, 1.5]   # right shoulder
point_lights[3] = [-0.5, 1]     # left elbow
point_lights[4] = [0.5, 1]      # right elbow
point_lights[5] = [-0.5, 0.5]   # left wrist
point_lights[6] = [0.5, 0.5]    # right wrist
point_lights[7] = [0, 1]        # torso
point_lights[8] = [-0.5, 0]     # left hip
point_lights[9] = [0.5, 0]      # right hip
point_lights[10] = [-0.5, -1]   # left knee
point_lights[11] = [0.5, -1]    # right knee
point_lights[12] = [-0.25, -2]   # left foot
point_lights[13] = [0.25, -2]    # right foot
point_lights[14] = [0, -1.5]    # position of waving hand

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')
points, = ax.plot(point_lights[:, 0], point_lights[:, 1], 'wo', markersize=10)

# Define the animation function
def animate(frame):
    # Simulate hand waving motion
    wave_amplitude = 0.5
    wave_frequency = 0.1
    point_lights[14][1] = np.sin(frame * wave_frequency) * wave_amplitude - 1.5  # Waving hand up and down
    points.set_data(point_lights[:, 0], point_lights[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 200), interval=50, blit=True)

# Show the animation
plt.axis('off')  # Turn off the axis
plt.show()
