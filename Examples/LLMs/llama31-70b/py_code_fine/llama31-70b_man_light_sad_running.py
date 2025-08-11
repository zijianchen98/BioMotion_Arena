
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# These positions are chosen to represent the major joints of the human body
# (head, shoulders, elbows, wrists, hips, knees, ankles)
initial_positions = np.array([
    [0.0, 0.5],  # head
    [-0.2, 0.4], [-0.2, 0.6],  # shoulders
    [-0.4, 0.3], [-0.4, 0.7],  # elbows
    [-0.6, 0.2], [-0.6, 0.8],  # wrists
    [0.0, 0.0],  # hips
    [-0.2, -0.2], [-0.2, 0.2],  # knees
    [-0.4, -0.4], [-0.4, 0.4],  # ankles
    [0.2, 0.4], [0.2, 0.6],  # right shoulder and elbow
    [0.4, 0.3], [0.4, 0.7],  # right wrist
    [0.2, -0.2], [0.2, 0.2],  # right knee
    [0.4, -0.4], [0.4, 0.4],  # right ankle
])

# Define the movement patterns for each point-light
# These patterns are based on the biomechanics of human running
def update(frame):
    positions = initial_positions.copy()
    
    # Head movement
    positions[0, 1] = 0.5 + 0.1 * np.sin(frame / 10.0)
    
    # Shoulder movement
    positions[1, 0] = -0.2 + 0.05 * np.sin(frame / 5.0)
    positions[2, 0] = -0.2 + 0.05 * np.cos(frame / 5.0)
    
    # Elbow movement
    positions[3, 0] = -0.4 + 0.1 * np.sin(frame / 5.0)
    positions[4, 0] = -0.4 + 0.1 * np.cos(frame / 5.0)
    
    # Wrist movement
    positions[5, 0] = -0.6 + 0.15 * np.sin(frame / 5.0)
    positions[6, 0] = -0.6 + 0.15 * np.cos(frame / 5.0)
    
    # Hip movement
    positions[7, 0] = 0.0 + 0.05 * np.sin(frame / 10.0)
    
    # Knee movement
    positions[8, 0] = -0.2 + 0.1 * np.sin(frame / 5.0)
    positions[9, 0] = -0.2 + 0.1 * np.cos(frame / 5.0)
    
    # Ankle movement
    positions[10, 0] = -0.4 + 0.15 * np.sin(frame / 5.0)
    positions[11, 0] = -0.4 + 0.15 * np.cos(frame / 5.0)
    
    # Right shoulder movement
    positions[12, 0] = 0.2 + 0.05 * np.cos(frame / 5.0)
    positions[13, 0] = 0.2 + 0.05 * np.sin(frame / 5.0)
    
    # Right elbow movement
    positions[14, 0] = 0.4 + 0.1 * np.cos(frame / 5.0)
    positions[15, 0] = 0.4 + 0.1 * np.sin(frame / 5.0)
    
    # Right wrist movement
    positions[16, 0] = 0.6 + 0.15 * np.cos(frame / 5.0)
    positions[17, 0] = 0.6 + 0.15 * np.sin(frame / 5.0)
    
    # Right knee movement
    positions[18, 0] = 0.2 + 0.1 * np.cos(frame / 5.0)
    positions[19, 0] = 0.2 + 0.1 * np.sin(frame / 5.0)
    
    # Right ankle movement
    positions[20, 0] = 0.4 + 0.15 * np.cos(frame / 5.0)
    positions[21, 0] = 0.4 + 0.15 * np.sin(frame / 5.0)
    
    scatter.set_offsets(positions)

fig, ax = plt.subplots()
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white')
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
