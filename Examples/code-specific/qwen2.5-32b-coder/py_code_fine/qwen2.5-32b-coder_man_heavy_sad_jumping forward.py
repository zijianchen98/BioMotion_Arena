
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
frames = 100
fps = 30

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(6, 6), facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of the points
points = np.zeros((num_points, 2))

# Create scatter plot for the points
scatter = ax.scatter(points[:, 0], points[:, 1], s=100, c='white')

# Define the motion function
def update(frame):
    t = frame / frames * 2 * np.pi
    
    # Body motion (simplified model)
    y_body = -0.5 + 0.4 * np.sin(t)
    x_body = 0.0 + 0.2 * np.sin(2 * t)
    
    # Arms
    arm_length = 0.3
    arm_angle = np.pi / 4 + 0.5 * np.sin(t + np.pi / 2)
    points[0] = [x_body - arm_length * np.cos(arm_angle), y_body + arm_length * np.sin(arm_angle)]
    points[1] = [x_body + arm_length * np.cos(arm_angle), y_body + arm_length * np.sin(arm_angle)]
    
    # Legs
    leg_length = 0.3
    leg_angle = -np.pi / 4 + 0.5 * np.sin(t)
    points[2] = [x_body - 0.1 - leg_length * np.cos(leg_angle), y_body - leg_length * np.sin(leg_angle)]
    points[3] = [x_body + 0.1 - leg_length * np.cos(leg_angle), y_body - leg_length * np.sin(leg_angle)]
    
    # Head
    head_radius = 0.1
    points[4] = [x_body, y_body + 0.3]
    
    # Eyes
    eye_offset = 0.05
    points[5] = [x_body - eye_offset, y_body + 0.35]
    points[6] = [x_body + eye_offset, y_body + 0.35]
    
    # Mouth (sad face)
    mouth_radius = 0.05
    mouth_angle = np.linspace(np.pi/4, 3*np.pi/4, 5)
    points[7:12] = np.array([x_body + mouth_radius * np.cos(mouth_angle), y_body + 0.2 + mouth_radius * np.sin(mouth_angle)]).T
    
    # Extra points for more realism
    points[12] = [x_body - 0.05, y_body + 0.15]
    points[13] = [x_body + 0.05, y_body + 0.15]
    points[14] = [x_body, y_body + 0.1]
    
    scatter.set_offsets(points)
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

plt.show()
