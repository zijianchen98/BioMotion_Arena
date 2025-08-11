
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the point-lights for a happyman bowing
initial_positions = {
    'head': np.array([0, 1]),
    'left_shoulder': np.array([-0.5, -0.5]),
    'right_shoulder': np.array([0.5, -0.5]),
    'left_elbow': np.array([-1.0, -1.0]),
    'right_elbow': np.array([1.0, -1.0]),
    'left_hand': np.array([-1.5, -1.5]),
    'right_hand': np.array([1.5, -1.5]),
    'left_hip': np.array([-0.5, -2.0]),
    'right_hip': np.array([0.5, -2.0]),
    'left_knee': np.array([-0.5, -3.0]),
    'right_knee': np.array([0.5, -3.0]),
    'left_foot': np.array([-0.5, -4.0]),
    'right_foot': np.array([0.5, -4.0]),
}

# Create the figure and axis for the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-5, 2)
ax.axis('off')

# Scatter plot for the point-lights
scat = ax.scatter([], [], s=50, c='white')

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    # Update positions based on frame
    positions = initial_positions.copy()
    
    # Bowing motion simulation
    angle = np.sin(frame / 10.0) * np.pi / 6  # Angle of bowing
    
    # Update head position
    positions['head'] = np.array([0, 1 + np.sin(frame / 10.0)])
    
    # Update shoulder positions
    positions['left_shoulder'] = np.array([-0.5 + np.cos(angle), -0.5 + np.sin(angle)])
    positions['right_shoulder'] = np.array([0.5 - np.cos(angle), -0.5 + np.sin(angle)])
    
    # Update elbow and hand positions
    positions['left_elbow'] = np.array([-1.0 + np.cos(angle), -1.0 + np.sin(angle)])
    positions['right_elbow'] = np.array([1.0 - np.cos(angle), -1.0 + np.sin(angle)])
    positions['left_hand'] = np.array([-1.5 + np.cos(angle), -1.5 + np.sin(angle)])
    positions['right_hand'] = np.array([1.5 - np.cos(angle), -1.5 + np.sin(angle)])
    
    # Update hip positions
    positions['left_hip'] = np.array([-0.5, -2.0])
    positions['right_hip'] = np.array([0.5, -2.0])
    
    # Update knee and foot positions
    positions['left_knee'] = np.array([-0.5, -3.0])
    positions['right_knee'] = np.array([0.5, -3.0])
    positions['left_foot'] = np.array([-0.5, -4.0])
    positions['right_foot'] = np.array([0.5, -4.0])
    
    # Convert to list of positions
    positions_list = [positions[key] for key in positions]
    
    # Update scatter plot
    scat.set_offsets(positions_list)
    return scat,

# Animation setup
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init, blit=True, interval=50)

plt.show()
