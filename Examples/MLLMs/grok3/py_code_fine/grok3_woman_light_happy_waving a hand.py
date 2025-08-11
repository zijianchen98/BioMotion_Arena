
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define joint positions for a happy woman waving a hand (15 point-lights)
# Initial positions (x, y) for joints: head, shoulders, elbows, wrists, hips, knees, ankles
initial_positions = np.array([
    [0, 10],  # head
    [-2, 8],  [2, 8],  # shoulders
    [-3, 6],  [3, 6],  # elbows
    [-4, 4],  [4, 2],  # wrists (waving motion starts here)
    [0, 0],   # hips
    [-1, -4], [1, -4],  # knees
    [-1, -8], [1, -8]   # ankles
])

# Number of frames for the animation
n_frames = 100

# Create figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-6, 6)
ax.set_ylim(-10, 12)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
scatter = ax.scatter([], [], c='white', s=100)

# Animation function
def update(frame):
    # Create a waving motion for the right arm (wrist and elbow)
    angle = np.sin(2 * np.pi * frame / n_frames) * 0.5
    positions = initial_positions.copy()
    
    # Apply waving motion to right wrist and elbow
    positions[6] = [4 + angle, 2 + 0.5 * np.cos(angle)]  # right wrist
    positions[5] = [3 + 0.5 * angle, 6 + 0.25 * np.cos(angle)]  # right elbow
    
    # Slight torso and shoulder movement for realism
    positions[1] = [-2 + 0.1 * np.sin(angle), 8 + 0.1 * np.cos(angle)]  # left shoulder
    positions[2] = [2 + 0.1 * np.sin(angle), 8 + 0.1 * np.cos(angle)]  # right shoulder
    
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=50, blit=True)

plt.show()
