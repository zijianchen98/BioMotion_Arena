
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define initial positions for 15 point-lights (simplified human figure bowing)
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles, torso points
initial_positions = np.array([
    [0, 10],  # head
    [-2, 8], [-2, 8],  # left shoulder, right shoulder
    [-4, 6], [0, 6],  # left elbow, right elbow
    [-6, 4], [2, 4],  # left wrist, right wrist
    [0, 0],  # torso
    [-1, -2], [1, -2],  # left hip, right hip
    [-2, -4], [0, -4],  # left knee, right knee
    [-3, -6], [2, -6]   # left ankle, right ankle
])

# Number of frames for the animation
n_frames = 60

# Create figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axis('off')

# Initialize scatter plot
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Animation function
def update(frame):
    # Calculate bowing motion: head and upper body move down, knees bend
    t = frame / n_frames
    angle = np.pi * t / 2  # Smooth bowing motion over time
    bend_knees = 0.5 * np.sin(np.pi * t)  # Knee bending
    
    # New positions for bowing
    new_positions = initial_positions.copy()
    # Head and torso move down
    new_positions[0, 1] -= 6 * t  # Head moves down
    new_positions[8, 1] -= 4 * t  # Torso moves down
    # Shoulders follow head
    new_positions[1:3, 1] -= 4 * t
    # Arms bend slightly
    new_positions[3:7, 0] += 1 * np.sin(angle)
    new_positions[3:7, 1] -= 2 * t
    # Hips move down slightly
    new_positions[9:11, 1] -= 2 * t
    # Knees bend
    new_positions[11:13, 1] -= bend_knees * 2
    new_positions[11:13, 0] -= bend_knees * 0.5
    # Ankles follow knees
    new_positions[13:, 1] -= bend_knees * 4
    new_positions[13:, 0] -= bend_knees * 0.5
    
    scatter.set_offsets(new_positions)
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=50, blit=True)

plt.show()
