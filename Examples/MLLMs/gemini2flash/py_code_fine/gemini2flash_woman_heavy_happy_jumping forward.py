
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
num_points = 15

# Define the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
plt.axis('off')

# Initialize the point-lights
points, = ax.plot([], [], 'wo', markersize=6)

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to update the animation for each frame
def animate(i):
    # Define the motion of each point-light to represent a person jumping forward
    # The following is a simplified example, you can adjust the parameters
    # to create more realistic and coherent motion.

    # Head
    x_head = 0
    y_head = 4 + 0.2 * np.sin(i * 0.1)

    # Shoulders
    x_shoulder_left = -1 + 0.1 * np.sin(i * 0.1 + np.pi/2)
    y_shoulder_left = 3 + 0.1 * np.cos(i * 0.1 + np.pi/2)
    x_shoulder_right = 1 + 0.1 * np.sin(i * 0.1 + np.pi/2)
    y_shoulder_right = 3 + 0.1 * np.cos(i * 0.1 + np.pi/2)
    
    # Elbows
    x_elbow_left = -2 + 0.3 * np.sin(i * 0.1)
    y_elbow_left = 2 + 0.2 * np.cos(i * 0.1)
    x_elbow_right = 2 + 0.3 * np.sin(i * 0.1)
    y_elbow_right = 2 + 0.2 * np.cos(i * 0.1)
    
    # Wrists
    x_wrist_left = -3 + 0.4 * np.sin(i * 0.1 + np.pi/4)
    y_wrist_left = 1 + 0.3 * np.cos(i * 0.1 + np.pi/4)
    x_wrist_right = 3 + 0.4 * np.sin(i * 0.1 + np.pi/4)
    y_wrist_right = 1 + 0.3 * np.cos(i * 0.1 + np.pi/4)

    # Torso
    x_torso_mid = 0
    y_torso_mid = 1.5 + 0.1 * np.sin(i * 0.1)
    
    # Hips
    x_hip_left = -0.5 + 0.05 * np.sin(i * 0.1)
    y_hip_left = 0 + 0.1 * np.cos(i * 0.1)
    x_hip_right = 0.5 + 0.05 * np.sin(i * 0.1)
    y_hip_right = 0 + 0.1 * np.cos(i * 0.1)
    
    # Knees
    x_knee_left = -1 + 0.5 * np.sin(i * 0.2)
    y_knee_left = -2 + 0.3 * np.cos(i * 0.2)
    x_knee_right = 1 + 0.5 * np.sin(i * 0.2)
    y_knee_right = -2 + 0.3 * np.cos(i * 0.2)
    
    # Ankles
    x_ankle_left = -1.5 + 0.6 * np.sin(i * 0.2 + np.pi/3)
    y_ankle_left = -3 + 0.4 * np.cos(i * 0.2 + np.pi/3)
    x_ankle_right = 1.5 + 0.6 * np.sin(i * 0.2 + np.pi/3)
    y_ankle_right = -3 + 0.4 * np.cos(i * 0.2 + np.pi/3)

    x = [x_head, x_shoulder_left, x_shoulder_right, x_elbow_left, x_elbow_right,
         x_wrist_left, x_wrist_right, x_torso_mid, x_hip_left, x_hip_right,
         x_knee_left, x_knee_right, x_ankle_left, x_ankle_right,0]

    y = [y_head, y_shoulder_left, y_shoulder_right, y_elbow_left, y_elbow_right,
         y_wrist_left, y_wrist_right, y_torso_mid, y_hip_left, y_hip_right,
         y_knee_left, y_knee_right, y_ankle_left, y_ankle_right,-4]

    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

# Save the animation
ani.save('jumping_woman.mp4', writer='ffmpeg', fps=30)

# Show the animation
plt.show()
