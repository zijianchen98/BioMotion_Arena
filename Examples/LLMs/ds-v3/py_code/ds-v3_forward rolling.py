
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rcParams

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points, = ax.plot([], [], 'wo', markersize=8)

# Time steps
frames = 100
t = np.linspace(0, 2 * np.pi, frames)

# Define the motion of each point-light to simulate a forward roll
def update(frame):
    # Head (moves in a circular path)
    head_x = 0.5 * np.cos(t[frame])
    head_y = 0.5 * np.sin(t[frame]) + 0.5
    
    # Shoulders (two points, moving in a similar but offset path)
    shoulder_left_x = 0.3 * np.cos(t[frame] + np.pi/6) - 0.2
    shoulder_left_y = 0.3 * np.sin(t[frame] + np.pi/6) + 0.3
    shoulder_right_x = 0.3 * np.cos(t[frame] - np.pi/6) + 0.2
    shoulder_right_y = 0.3 * np.sin(t[frame] - np.pi/6) + 0.3
    
    # Elbows (connected to shoulders)
    elbow_left_x = 0.4 * np.cos(t[frame] + np.pi/4) - 0.3
    elbow_left_y = 0.4 * np.sin(t[frame] + np.pi/4) + 0.1
    elbow_right_x = 0.4 * np.cos(t[frame] - np.pi/4) + 0.3
    elbow_right_y = 0.4 * np.sin(t[frame] - np.pi/4) + 0.1
    
    # Hands (connected to elbows)
    hand_left_x = 0.5 * np.cos(t[frame] + np.pi/3) - 0.4
    hand_left_y = 0.5 * np.sin(t[frame] + np.pi/3) - 0.1
    hand_right_x = 0.5 * np.cos(t[frame] - np.pi/3) + 0.4
    hand_right_y = 0.5 * np.sin(t[frame] - np.pi/3) - 0.1
    
    # Torso (central point)
    torso_x = 0.1 * np.cos(t[frame])
    torso_y = 0.1 * np.sin(t[frame])
    
    # Hips (two points, moving in a similar but offset path)
    hip_left_x = 0.2 * np.cos(t[frame] + np.pi/6) - 0.1
    hip_left_y = 0.2 * np.sin(t[frame] + np.pi/6) - 0.3
    hip_right_x = 0.2 * np.cos(t[frame] - np.pi/6) + 0.1
    hip_right_y = 0.2 * np.sin(t[frame] - np.pi/6) - 0.3
    
    # Knees (connected to hips)
    knee_left_x = 0.3 * np.cos(t[frame] + np.pi/4) - 0.2
    knee_left_y = 0.3 * np.sin(t[frame] + np.pi/4) - 0.6
    knee_right_x = 0.3 * np.cos(t[frame] - np.pi/4) + 0.2
    knee_right_y = 0.3 * np.sin(t[frame] - np.pi/4) - 0.6
    
    # Feet (connected to knees)
    foot_left_x = 0.4 * np.cos(t[frame] + np.pi/3) - 0.3
    foot_left_y = 0.4 * np.sin(t[frame] + np.pi/3) - 0.8
    foot_right_x = 0.4 * np.cos(t[frame] - np.pi/3) + 0.3
    foot_right_y = 0.4 * np.sin(t[frame] - np.pi/3) - 0.8
    
    # Combine all points
    x = np.array([
        head_x,
        shoulder_left_x, shoulder_right_x,
        elbow_left_x, elbow_right_x,
        hand_left_x, hand_right_x,
        torso_x,
        hip_left_x, hip_right_x,
        knee_left_x, knee_right_x,
        foot_left_x, foot_right_x,
        0.0  # Additional point for balance (e.g., center of mass)
    ])
    
    y = np.array([
        head_y,
        shoulder_left_y, shoulder_right_y,
        elbow_left_y, elbow_right_y,
        hand_left_y, hand_right_y,
        torso_y,
        hip_left_y, hip_right_y,
        knee_left_y, knee_right_y,
        foot_left_y, foot_right_y,
        0.0  # Additional point for balance
    ])
    
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.tight_layout()
plt.show()
