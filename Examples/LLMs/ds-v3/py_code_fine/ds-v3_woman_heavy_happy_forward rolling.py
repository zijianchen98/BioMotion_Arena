
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Ellipse

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points = [ax.plot([], [], 'o', color='white', markersize=8)[0] for _ in range(num_points)]

# Define keyframes for a forward rolling motion (simplified)
def get_keyframes():
    # Keyframes for each point (simplified for a rolling motion)
    # This is a very rough approximation; a more accurate version would require detailed motion capture data
    keyframes = []
    
    # Time steps
    t = np.linspace(0, 2*np.pi, 100)
    
    # Body center trajectory (rolling motion)
    x_center = 0.5 * np.cos(t)
    y_center = -0.5 * np.sin(t)
    
    # Points relative to the body center (simulated for a heavy woman rolling)
    # Points: head, shoulders, elbows, hands, hips, knees, feet
    for i in range(len(t)):
        frame = []
        angle = t[i]
        
        # Head
        head_x = x_center[i] + 0.1 * np.cos(angle + np.pi/2)
        head_y = y_center[i] + 0.1 * np.sin(angle + np.pi/2)
        frame.append((head_x, head_y))
        
        # Shoulders
        shoulder1_x = x_center[i] + 0.15 * np.cos(angle + np.pi/2 + 0.2)
        shoulder1_y = y_center[i] + 0.15 * np.sin(angle + np.pi/2 + 0.2)
        frame.append((shoulder1_x, shoulder1_y))
        
        shoulder2_x = x_center[i] + 0.15 * np.cos(angle + np.pi/2 - 0.2)
        shoulder2_y = y_center[i] + 0.15 * np.sin(angle + np.pi/2 - 0.2)
        frame.append((shoulder2_x, shoulder2_y))
        
        # Elbows
        elbow1_x = shoulder1_x + 0.1 * np.cos(angle + np.pi/2 + 0.5)
        elbow1_y = shoulder1_y + 0.1 * np.sin(angle + np.pi/2 + 0.5)
        frame.append((elbow1_x, elbow1_y))
        
        elbow2_x = shoulder2_x + 0.1 * np.cos(angle + np.pi/2 - 0.5)
        elbow2_y = shoulder2_y + 0.1 * np.sin(angle + np.pi/2 - 0.5)
        frame.append((elbow2_x, elbow2_y))
        
        # Hands
        hand1_x = elbow1_x + 0.1 * np.cos(angle + np.pi/2 + 0.8)
        hand1_y = elbow1_y + 0.1 * np.sin(angle + np.pi/2 + 0.8)
        frame.append((hand1_x, hand1_y))
        
        hand2_x = elbow2_x + 0.1 * np.cos(angle + np.pi/2 - 0.8)
        hand2_y = elbow2_y + 0.1 * np.sin(angle + np.pi/2 - 0.8)
        frame.append((hand2_x, hand2_y))
        
        # Hips
        hip1_x = x_center[i] + 0.15 * np.cos(angle - np.pi/2 + 0.2)
        hip1_y = y_center[i] + 0.15 * np.sin(angle - np.pi/2 + 0.2)
        frame.append((hip1_x, hip1_y))
        
        hip2_x = x_center[i] + 0.15 * np.cos(angle - np.pi/2 - 0.2)
        hip2_y = y_center[i] + 0.15 * np.sin(angle - np.pi/2 - 0.2)
        frame.append((hip2_x, hip2_y))
        
        # Knees
        knee1_x = hip1_x + 0.1 * np.cos(angle - np.pi/2 + 0.5)
        knee1_y = hip1_y + 0.1 * np.sin(angle - np.pi/2 + 0.5)
        frame.append((knee1_x, knee1_y))
        
        knee2_x = hip2_x + 0.1 * np.cos(angle - np.pi/2 - 0.5)
        knee2_y = hip2_y + 0.1 * np.sin(angle - np.pi/2 - 0.5)
        frame.append((knee2_x, knee2_y))
        
        # Feet
        foot1_x = knee1_x + 0.1 * np.cos(angle - np.pi/2 + 0.8)
        foot1_y = knee1_y + 0.1 * np.sin(angle - np.pi/2 + 0.8)
        frame.append((foot1_x, foot1_y))
        
        foot2_x = knee2_x + 0.1 * np.cos(angle - np.pi/2 - 0.8)
        foot2_y = knee2_y + 0.1 * np.sin(angle - np.pi/2 - 0.8)
        frame.append((foot2_x, foot2_y))
        
        # Additional points for a heavy figure (e.g., belly)
        belly_x = x_center[i] + 0.05 * np.cos(angle)
        belly_y = y_center[i] + 0.05 * np.sin(angle)
        frame.append((belly_x, belly_y))
        
        keyframes.append(frame)
    
    return keyframes

keyframes = get_keyframes()

# Animation update function
def update(frame):
    for i in range(num_points):
        x, y = keyframes[frame][i]
        points[i].set_data(x, y)
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(keyframes), interval=50, blit=True)

plt.title('Point-Light Animation: Happy Woman Forward Rolling', color='white')
plt.show()
