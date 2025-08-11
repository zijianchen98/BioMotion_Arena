
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# These points represent the following joints:
# 0: Head, 1-2: Shoulders, 3-4: Elbows, 5-6: Wrists, 7: Chest, 8-9: Hips, 10-11: Knees, 12-13: Ankles, 14: Feet
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], # Left Shoulder
    [1, -1],  # Right Shoulder
    [-2, -3], # Left Elbow
    [2, -3],  # Right Elbow
    [-2, -5], # Left Wrist
    [2, -5],  # Right Wrist
    [0, -2],  # Chest
    [-1, -4], # Left Hip
    [1, -4],  # Right Hip
    [-1, -6], # Left Knee
    [1, -6],  # Right Knee
    [-1, -8], # Left Ankle
    [1, -8],  # Right Ankle
    [0, -10]  # Feet
])

# Define the range of motion for each joint
# This will simulate the "heavy weight" effect by limiting the movement
motion_range = {
    "head": 0.1,
    "shoulders": 0.2,
    "elbows": 0.3,
    "wrists": 0.4,
    "chest": 0.1,
    "hips": 0.2,
    "knees": 0.3,
    "ankles": 0.4,
    "feet": 0.1
}

# Function to update the positions of the point-lights
def update_positions(frame):
    positions = initial_positions.copy()
    
    # Simulate slight movements for each joint
    positions[0] += np.random.uniform(-motion_range["head"], motion_range["head"], 2)  # Head
    
    positions[1:3] += np.random.uniform(-motion_range["shoulders"], motion_range["shoulders"], (2, 2))  # Shoulders
    positions[3:5] += np.random.uniform(-motion_range["elbows"], motion_range["elbows"], (2, 2))  # Elbows
    positions[5:7] += np.random.uniform(-motion_range["wrists"], motion_range["wrists"], (2, 2))  # Wrists
    
    positions[7] += np.random.uniform(-motion_range["chest"], motion_range["chest"], 2)  # Chest
    
    positions[8:10] += np.random.uniform(-motion_range["hips"], motion_range["hips"], (2, 2))  # Hips
    positions[10:12] += np.random.uniform(-motion_range["knees"], motion_range["knees"], (2, 2))  # Knees
    positions[12:14] += np.random.uniform(-motion_range["ankles"], motion_range["ankles"], (2, 2))  # Ankles
    
    positions[14] += np.random.uniform(-motion_range["feet"], motion_range["feet"], 2)  # Feet
    
    return positions

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-10, 2)
ax.axis('off')  # Hide axes for a cleaner look

scatter = ax.scatter([], [], s=50, c='white')

def animate(frame):
    positions = update_positions(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Display the animation
plt.show()
