
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for a walking person
def walking_person(t, phase=0):
    # Define the point-light locations for the head, torso, and limbs
    head = np.array([0, 1])
    torso = np.array([0, 0.5])
    right_shoulder = np.array([0.2, 0.7])
    right_elbow = np.array([0.4, 0.7])
    right_hand = np.array([0.6, 0.7])
    left_shoulder = np.array([-0.2, 0.7])
    left_elbow = np.array([-0.4, 0.7])
    left_hand = np.array([-0.6, 0.7])
    right_hip = np.array([0.2, 0])
    right_knee = np.array([0.2, -0.5])
    right_foot = np.array([0.2, -1])
    left_hip = np.array([-0.2, 0])
    left_knee = np.array([-0.2, -0.5])
    left_foot = np.array([-0.2, -1])

    # Define the movement of each point-light
    head_movement = np.array([0, 0.05 * np.sin(t + phase)])
    torso_movement = np.array([0, 0.05 * np.sin(t + phase)])
    right_shoulder_movement = np.array([0.05 * np.sin(t + phase), 0.05 * np.cos(t + phase)])
    right_elbow_movement = np.array([0.1 * np.sin(t + phase), 0.1 * np.cos(t + phase)])
    right_hand_movement = np.array([0.15 * np.sin(t + phase), 0.15 * np.cos(t + phase)])
    left_shoulder_movement = np.array([-0.05 * np.sin(t + phase), 0.05 * np.cos(t + phase)])
    left_elbow_movement = np.array([-0.1 * np.sin(t + phase), 0.1 * np.cos(t + phase)])
    left_hand_movement = np.array([-0.15 * np.sin(t + phase), 0.15 * np.cos(t + phase)])
    right_hip_movement = np.array([0.05 * np.sin(t + phase), -0.05 * np.cos(t + phase)])
    right_knee_movement = np.array([0.1 * np.sin(t + phase), -0.1 * np.cos(t + phase)])
    right_foot_movement = np.array([0.15 * np.sin(t + phase), -0.15 * np.cos(t + phase)])
    left_hip_movement = np.array([-0.05 * np.sin(t + phase), -0.05 * np.cos(t + phase)])
    left_knee_movement = np.array([-0.1 * np.sin(t + phase), -0.1 * np.cos(t + phase)])
    left_foot_movement = np.array([-0.15 * np.sin(t + phase), -0.15 * np.cos(t + phase)])

    # Combine the point-light locations and movements
    points = np.array([
        head + head_movement,
        torso + torso_movement,
        right_shoulder + right_shoulder_movement,
        right_elbow + right_elbow_movement,
        right_hand + right_hand_movement,
        left_shoulder + left_shoulder_movement,
        left_elbow + left_elbow_movement,
        left_hand + left_hand_movement,
        right_hip + right_hip_movement,
        right_knee + right_knee_movement,
        right_foot + right_foot_movement,
        left_hip + left_hip_movement,
        left_knee + left_knee_movement,
        left_foot + left_foot_movement,
        np.array([0, -1.5])  # Add a point for the shadow
    ])

    return points

# Create a new figure
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Set the aspect ratio to be equal
ax.set_aspect('equal')

# Set the limits of the axes
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2, 2)

# Remove the axes
ax.axis('off')

# Create a scatter plot of the point-lights
points, = ax.plot([], [], 'o', markersize=10, color='white')

# Function to update the plot
def update(t):
    points.set_data(walking_person(t).T[0], walking_person(t).T[1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 10, 128), interval=50)

plt.show()
