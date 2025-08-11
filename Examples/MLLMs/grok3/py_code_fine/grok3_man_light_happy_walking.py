
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Define initial positions and structure of 15 point-lights for a walking human
# Based on a simplified biomechanical model (head, torso, arms, legs, joints)
def initialize_points():
    # Initial positions (x, y) for 15 points: head, shoulders, elbows, wrists, hips, knees, ankles
    points = np.array([
        [0, 10],  # Head
        [-1, 8],  # Left shoulder
        [-3, 6],  # Left elbow
        [-4, 4],  # Left wrist
        [1, 8],   # Right shoulder
        [3, 6],   # Right elbow
        [4, 4],   # Right wrist
        [-1, 5],  # Left hip
        [-2, 2],  # Left knee
        [-2, 0],  # Left ankle
        [1, 5],   # Right hip
        [2, 2],   # Right knee
        [2, 0],   # Right ankle
        [0, 6],   # Torso top
        [0, 4]    # Torso bottom
    ])
    return points

# Update function for animation
def update(frame, points, scat):
    # Simulate walking motion with sinusoidal movement for legs and arms
    t = frame * 0.1  # Time parameter for smooth motion
    phase = np.sin(t)
    phase_opp = np.cos(t)

    # Update positions for walking motion
    new_points = points.copy()
    
    # Head and torso slight vertical bounce
    new_points[0] += [0, 0.2 * phase]  # Head
    new_points[13] += [0, 0.1 * phase]  # Torso top
    new_points[14] += [0, 0.1 * phase]  # Torso bottom

    # Left arm swing
    new_points[1] += [-0.5 * phase, 0]  # Left shoulder
    new_points[2] += [-0.7 * phase, -0.5 * phase]  # Left elbow
    new_points[3] += [-0.9 * phase, -1.0 * phase]  # Left wrist

    # Right arm swing (opposite phase)
    new_points[4] += [0.5 * phase_opp, 0]  # Right shoulder
    new_points[5] += [0.7 * phase_opp, -0.5 * phase_opp]  # Right elbow
    new_points[6] += [0.9 * phase_opp, -1.0 * phase_opp]  # Right wrist

    # Left leg motion
    new_points[7] += [-0.3 * phase, 0]  # Left hip
    new_points[8] += [-0.5 * phase, -2.0 * phase]  # Left knee
    new_points[9] += [-0.5 * phase, -4.0 * phase]  # Left ankle

    # Right leg motion (opposite phase)
    new_points[10] += [0.3 * phase_opp, 0]  # Right hip
    new_points[11] += [0.5 * phase_opp, -2.0 * phase_opp]  # Right knee
    new_points[12] += [0.5 * phase_opp, -4.0 * phase_opp]  # Right ankle

    scat.set_offsets(new_points)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-6, 6)
ax.set_ylim(-2, 12)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
points = initialize_points()
scat = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Create animation
ani = FuncAnimation(fig, update, frames=range(100), fargs=(points, scat), interval=50, blit=True)

plt.show()
