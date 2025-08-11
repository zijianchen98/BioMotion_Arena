
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and the duration of the animation
num_frames = 100
duration = 5  # seconds
fps = num_frames / duration

# Define the positions of the point-lights for the waving hand
# This is a simplified representation of a human figure with 15 points
# The points represent key joints in the body and hand

# Initial positions of the points
initial_positions = np.array([
    [0, 0],  # Hip
    [0, -1],  # Knee
    [0, -2],  # Ankle
    [0, -3],  # Foot
    [1, 0],  # Waist
    [2, 0],  # Chest
    [3, 0],  # Shoulder
    [4, 0],  # Elbow
    [5, 0],  # Wrist
    [5, 1],  # Finger 1
    [5, 2],  # Finger 2
    [5, 3],  # Finger 3
    [5, 4],  # Finger 4
    [5, -1],  # Finger 5
    [5, -2]  # Finger 6
])

# Function to update the positions of the points for each frame
def update_positions(frame):
    angle = np.sin(2 * np.pi * frame / num_frames) * np.pi / 6  # Sine wave for smooth waving motion
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    
    # Apply rotation to the hand (points 7-14)
    hand_positions = initial_positions[7:15]
    rotated_hand_positions = np.dot(hand_positions, rotation_matrix.T)
    new_positions = np.vstack((initial_positions[:7], rotated_hand_positions))
    
    return new_positions

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.axis('off')

# Create the point-lights
points, = ax.plot([], [], 'wo', markersize=10)

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Animation update function
def animate(frame):
    new_positions = update_positions(frame)
    x = new_positions[:, 0]
    y = new_positions[:, 1]
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=num_frames, interval=1000/fps, blit=True)

# Display the animation
plt.show()
