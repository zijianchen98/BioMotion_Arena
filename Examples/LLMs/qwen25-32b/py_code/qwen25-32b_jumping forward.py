
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the frames for the jumping forward motion
frames = 100
fig, ax = plt.subplots()
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.axis('off')

# Initial positions of the 15 point-lights representing the man's body
positions = np.array([
    [4.5, 7],  # Head
    [4, 6],    # Left Shoulder
    [5, 6],    # Right Shoulder
    [3.5, 4],  # Left Elbow
    [5.5, 4],  # Right Elbow
    [3, 2],    # Left Hand
    [6, 2],    # Right Hand
    [4.5, 5],  # Torso
    [4, 3],    # Left Hip
    [5, 3],    # Right Hip
    [3.5, 1],  # Left Knee
    [5.5, 1],  # Right Knee
    [3, 0],    # Left Foot
    [6, 0],    # Right Foot
    [4.5, 2]   # Lower Body Center
])

# Create a scatter plot for the points
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=10)

def update(frame):
    global positions
    
    # Jumping motion simulation
    t = frame / frames * 2 * np.pi
    amplitude = 1.5
    frequency = 0.5
    displacement = amplitude * np.sin(frequency * t)
    
    # Update y positions for the head, torso, and lower body center
    positions[0][1] = 7 + displacement
    positions[8][1] = 3 + displacement
    positions[14][1] = 2 + displacement
    
    # Update x positions for the arms and legs to simulate swinging
    arm_displacement = amplitude * np.sin(2 * frequency * t + np.pi)
    leg_displacement = amplitude * np.sin(2 * frequency * t)
    
    positions[6][0] = 6 + arm_displacement
    positions[7][0] = 4.5 + leg_displacement
    positions[11][0] = 5.5 + leg_displacement
    positions[13][0] = 6 + leg_displacement
    
    scat.set_offsets(positions)

ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, repeat=True)
plt.show()
