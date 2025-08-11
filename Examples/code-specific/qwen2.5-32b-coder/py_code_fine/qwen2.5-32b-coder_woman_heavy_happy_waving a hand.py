
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
frames = 120
fps = 30

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 6), facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of points
points = np.zeros((num_points, 2))

# Create scatter plot for points
scat = ax.scatter(points[:, 0], points[:, 1], s=100, c='white')

# Function to update the position of points
def update(frame):
    # Base angles for the motion
    t = frame / fps
    
    # Positions for the head
    points[0] = [0.0, 0.7]
    
    # Positions for the shoulders
    points[1] = [-0.15, 0.5]
    points[2] = [0.15, 0.5]
    
    # Positions for the arms
    arm_angle = np.sin(t) * 0.3 + np.pi/4
    points[3] = [points[2][0] + 0.3 * np.cos(arm_angle), points[2][1] - 0.3 * np.sin(arm_angle)]
    points[4] = [points[3][0] + 0.3 * np.cos(arm_angle + np.pi/2), points[3][1] - 0.3 * np.sin(arm_angle + np.pi/2)]
    
    # Waving hand
    hand_angle = np.sin(t * 2) * 0.5
    points[5] = [points[4][0] + 0.2 * np.cos(hand_angle), points[4][1] - 0.2 * np.sin(hand_angle)]
    
    # Positions for the torso
    points[6] = [0.0, 0.3]
    
    # Positions for the hips
    points[7] = [-0.1, 0.1]
    points[8] = [0.1, 0.1]
    
    # Positions for the legs
    leg_angle = np.sin(t) * 0.2 - np.pi/4
    points[9] = [points[7][0] + 0.3 * np.cos(leg_angle), points[7][1] - 0.3 * np.sin(leg_angle)]
    points[10] = [points[8][0] + 0.3 * np.cos(leg_angle), points[8][1] - 0.3 * np.sin(leg_angle)]
    
    # Positions for the feet
    points[11] = [points[9][0] + 0.2 * np.cos(leg_angle + np.pi/2), points[9][1] - 0.2 * np.sin(leg_angle + np.pi/2)]
    points[12] = [points[10][0] + 0.2 * np.cos(leg_angle + np.pi/2), points[10][1] - 0.2 * np.sin(leg_angle + np.pi/2)]
    
    # Adding extra points for more realistic motion
    points[13] = [(points[2][0] + points[6][0]) / 2, (points[2][1] + points[6][1]) / 2]  # Midpoint shoulder-torso
    points[14] = [(points[7][0] + points[8][0]) / 2, (points[7][1] + points[8][1]) / 2]  # Midpoint hip
    
    scat.set_offsets(points)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Show plot
plt.show()
