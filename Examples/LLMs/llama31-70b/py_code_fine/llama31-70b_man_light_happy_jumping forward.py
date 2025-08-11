
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# Representing the joints of a human body
joints = np.array([
    [0.0, 0.0],  # Head
    [-0.2, 0.3],  # Left shoulder
    [0.2, 0.3],  # Right shoulder
    [-0.3, 0.1],  # Left elbow
    [0.3, 0.1],  # Right elbow
    [-0.4, 0.0],  # Left wrist
    [0.4, 0.0],  # Right wrist
    [0.0, -0.2],  # Hip
    [-0.2, -0.4],  # Left knee
    [0.2, -0.4],  # Right knee
    [-0.3, -0.6],  # Left ankle
    [0.3, -0.6],  # Right ankle
    [-0.1, -0.8],  # Left toe
    [0.1, -0.8],  # Right toe
    [0.0, -0.5]  # Center of mass
])

# Define the animation function
def animate(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Update the positions of the joints based on the frame number
    # Simulate a jumping motion
    head = joints[0] + np.array([0.0, 0.1 * np.sin(frame / 10.0)])
    left_shoulder = joints[1] + np.array([-0.1 * np.sin(frame / 10.0), 0.1 * np.cos(frame / 10.0)])
    right_shoulder = joints[2] + np.array([0.1 * np.sin(frame / 10.0), 0.1 * np.cos(frame / 10.0)])
    left_elbow = joints[3] + np.array([-0.2 * np.sin(frame / 10.0), 0.2 * np.cos(frame / 10.0)])
    right_elbow = joints[4] + np.array([0.2 * np.sin(frame / 10.0), 0.2 * np.cos(frame / 10.0)])
    left_wrist = joints[5] + np.array([-0.3 * np.sin(frame / 10.0), 0.3 * np.cos(frame / 10.0)])
    right_wrist = joints[6] + np.array([0.3 * np.sin(frame / 10.0), 0.3 * np.cos(frame / 10.0)])
    hip = joints[7] + np.array([0.0, -0.1 * np.sin(frame / 10.0)])
    left_knee = joints[8] + np.array([-0.1 * np.sin(frame / 10.0), -0.2 * np.cos(frame / 10.0)])
    right_knee = joints[9] + np.array([0.1 * np.sin(frame / 10.0), -0.2 * np.cos(frame / 10.0)])
    left_ankle = joints[10] + np.array([-0.2 * np.sin(frame / 10.0), -0.3 * np.cos(frame / 10.0)])
    right_ankle = joints[11] + np.array([0.2 * np.sin(frame / 10.0), -0.3 * np.cos(frame / 10.0)])
    left_toe = joints[12] + np.array([-0.1 * np.sin(frame / 10.0), -0.4 * np.cos(frame / 10.0)])
    right_toe = joints[13] + np.array([0.1 * np.sin(frame / 10.0), -0.4 * np.cos(frame / 10.0)])
    center_of_mass = joints[14] + np.array([0.0, -0.1 * np.sin(frame / 10.0)])

    # Plot the point-lights
    ax.plot(head[0], head[1], 'o', markersize=5, color='white')
    ax.plot(left_shoulder[0], left_shoulder[1], 'o', markersize=5, color='white')
    ax.plot(right_shoulder[0], right_shoulder[1], 'o', markersize=5, color='white')
    ax.plot(left_elbow[0], left_elbow[1], 'o', markersize=5, color='white')
    ax.plot(right_elbow[0], right_elbow[1], 'o', markersize=5, color='white')
    ax.plot(left_wrist[0], left_wrist[1], 'o', markersize=5, color='white')
    ax.plot(right_wrist[0], right_wrist[1], 'o', markersize=5, color='white')
    ax.plot(hip[0], hip[1], 'o', markersize=5, color='white')
    ax.plot(left_knee[0], left_knee[1], 'o', markersize=5, color='white')
    ax.plot(right_knee[0], right_knee[1], 'o', markersize=5, color='white')
    ax.plot(left_ankle[0], left_ankle[1], 'o', markersize=5, color='white')
    ax.plot(right_ankle[0], right_ankle[1], 'o', markersize=5, color='white')
    ax.plot(left_toe[0], left_toe[1], 'o', markersize=5, color='white')
    ax.plot(right_toe[0], right_toe[1], 'o', markersize=5, color='white')
    ax.plot(center_of_mass[0], center_of_mass[1], 'o', markersize=5, color='white')

# Create a new figure
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

# Show the animation
plt.show()
