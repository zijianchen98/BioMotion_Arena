
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-3, 3)
ax.set_ylim(0, 7)
ax.axis('off')

# Initial positions of the 15 points (head, shoulders, elbows, hands, torso, hips, knees, feet)
initial_points = [
    (0, 6),         # Head
    (-1, 5),        # Left shoulder
    (1, 5),         # Right shoulder
    (-1, 4),        # Left elbow
    (1, 4),         # Right elbow (will be updated)
    (-1, 3),        # Left hand
    (1, 3),         # Right hand (will be updated)
    (0, 5),         # Upper torso
    (0, 4.5),       # Mid torso
    (0, 4),         # Lower torso
    (-0.5, 4),      # Left hip
    (0.5, 4),       # Right hip
    (-0.5, 3),      # Left knee
    (0.5, 3),       # Right knee
    (-0.5, 2),      # Left foot
    (0.5, 2)        # Right foot
]

# Create scatter plot with initial positions
scat = ax.scatter([p[0] for p in initial_points], [p[1] for p in initial_points], c='white', s=50)

def update(frame):
    t = frame * 0.15  # Time parameter for animation speed
    
    # Create a copy of initial points to modify
    new_points = list(initial_points)
    
    # Right arm angles (shoulder and elbow)
    theta = np.radians(30 * np.sin(t))          # Shoulder angle
    phi = np.radians(-60 + 30 * np.sin(t*1.2))  # Elbow angle
    
    # Right arm kinematics
    shoulder_x, shoulder_y = new_points[2]     # Right shoulder position
    upper_arm_length, forearm_length = 1.0, 1.0
    
    # Calculate elbow position
    elbow_x = shoulder_x + upper_arm_length * np.sin(theta)
    elbow_y = shoulder_y - upper_arm_length * np.cos(theta)
    new_points[3] = (elbow_x, elbow_y)  # Update right elbow
    
    # Calculate hand position
    hand_x = elbow_x + forearm_length * np.sin(theta + phi)
    hand_y = elbow_y - forearm_length * np.cos(theta + phi)
    new_points[6] = (hand_x, hand_y)    # Update right hand
    
    # Body sway to simulate weight shift
    shift = 0.2 * np.sin(t)
    new_points[7] = (shift, 5)         # Upper torso
    new_points[8] = (shift*0.8, 4.5)   # Mid torso
    new_points[9] = (shift*0.6, 4)     # Lower torso
    
    # Update hips and legs
    new_points[10] = (-0.5 + shift*0.4, 4)  # Left hip
    new_points[11] = (0.5 + shift*0.4, 4)   # Right hip
    new_points[13] = (0.5 + shift*0.2, 3)   # Right knee
    
    # Update scatter plot positions
    scat.set_offsets(new_points)
    return scat,

# Create animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128), interval=20, blit=True)
plt.show()
