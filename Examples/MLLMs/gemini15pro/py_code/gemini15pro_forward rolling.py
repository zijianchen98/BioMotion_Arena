
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the joint positions for a forward roll animation
# This is a simplified representation, adjust for more realism
def get_joint_positions(frame):
    cycle = 12
    frame = frame % cycle
    x = np.linspace(0, 2*np.pi, cycle)

    head = [np.sin(x[frame]), 2 - 0.5*np.abs(np.sin(x[frame]))]

    shoulder_left = [np.sin(x[frame]) - 0.2, 1.5 - 0.2*np.abs(np.sin(x[frame]))]
    shoulder_right = [np.sin(x[frame]) + 0.2, 1.5 - 0.2*np.abs(np.sin(x[frame]))]

    elbow_left = [np.sin(x[frame]) - 0.4, 1 - 0.4*np.abs(np.sin(x[frame]))]
    elbow_right = [np.sin(x[frame]) + 0.4, 1 - 0.4*np.abs(np.sin(x[frame]))]

    hand_left = [np.sin(x[frame]) - 0.6, 0.5 - 0.2*np.abs(np.sin(x[frame]))]
    hand_right = [np.sin(x[frame]) + 0.6, 0.5 - 0.2*np.abs(np.sin(x[frame]))]


    hip_left = [np.sin(x[frame]) - 0.2, 0.5 - 0.2*np.abs(np.sin(x[frame]))]
    hip_right = [np.sin(x[frame]) + 0.2, 0.5 - 0.2*np.abs(np.sin(x[frame]))]

    knee_left = [np.sin(x[frame]) - 0.3, 0 - 0.4 * np.abs(np.sin(x[frame]))]
    knee_right = [np.sin(x[frame]) + 0.3, 0 - 0.4* np.abs(np.sin(x[frame]))]

    foot_left = [np.sin(x[frame]) - 0.4, -0.5 - 0.1*np.abs(np.sin(x[frame]))]
    foot_right = [np.sin(x[frame]) + 0.4, -0.5 - 0.1*np.abs(np.sin(x[frame]))]

    return np.array([head, shoulder_left, shoulder_right, elbow_left, elbow_right, 
                     hand_left, hand_right, hip_left, hip_right, knee_left, knee_right,
                     foot_left, foot_right, [np.sin(x[frame]), 1.7], [np.sin(x[frame]), 1.2]])

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim([-2, 2])
ax.set_ylim([-1, 2.5])
ax.set_aspect('equal')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# Initialize the points
points, = ax.plot([], [], 'wo')


# Animation update function
def update(frame):
    positions = get_joint_positions(frame)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(24), interval=70, blit=True)


plt.show()

