
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Define constants for arm lengths and motion parameters
L_upper = 0.3    # Length of upper arm
L_forearm = 0.3  # Length of forearm
omega = np.pi    # Angular frequency for period T=2 seconds
A = 0.3          # Amplitude for wrist x-movement
B = 0.1          # Amplitude for wrist y-movement

# Initial positions of the 15 point-lights representing the human figure
points = {
    'head': (0, 1.8),
    'left_shoulder': (-0.2, 1.5),
    'right_shoulder': (0.2, 1.5),
    'left_elbow': (-0.2, 1.2),
    'right_elbow': (0.2, 1.2),    # To be updated during animation
    'left_wrist': (-0.2, 0.9),
    'right_wrist': (0.2, 0.9),    # To be updated during animation
    'left_hip': (-0.1, 1.0),
    'right_hip': (0.1, 1.0),
    'left_knee': (-0.1, 0.5),
    'right_knee': (0.1, 0.5),
    'left_ankle': (-0.1, 0.0),
    'right_ankle': (0.1, 0.0),
    'left_toe': (-0.1, -0.1),
    'right_toe': (0.1, -0.1),
}

# Define the order of points for consistent indexing
order = [
    'head', 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow',
    'left_wrist', 'right_wrist', 'left_hip', 'right_hip', 'left_knee',
    'right_knee', 'left_ankle', 'right_ankle', 'left_toe', 'right_toe'
]

# Initialize positions as a NumPy array for animation
positions = np.array([points[key] for key in order])

# Function to compute elbow position using inverse kinematics
def compute_elbow(S, W, L1, L2):
    """
    Compute elbow position given shoulder (S) and wrist (W) positions.
    L1: upper arm length, L2: forearm length.
    Returns one of two possible elbow positions (lower y-coordinate).
    """
    V = np.array(W) - np.array(S)
    d = np.linalg.norm(V)
    if d > L1 + L2 or d < abs(L1 - L2):
        raise ValueError("No solution for elbow position")
    a = (L1**2 - L2**2 + d**2) / (2 * d)
    h = np.sqrt(L1**2 - a**2)
    V_unit = V / d
    P = np.array([-V_unit[1], V_unit[0]])  # Perpendicular vector
    E1 = S + a * V_unit + h * P
    E2 = S + a * V_unit - h * P
    return E1 if E1[1] < E2[1] else E2

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-0.6, 0.6)    # Adjusted to accommodate waving motion
ax.set_ylim(-0.2, 2.0)    # Covers full height of figure
ax.set_facecolor('black') # Solid black background
ax.axis('off')            # Hide axes for pure point-light display

# Initialize scatter plot with 15 white points
scatter = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Animation update function
def update(frame):
    """
    Update point positions for each frame.
    Animates the right arm waving while keeping other points static.
    """
    t = frame * 0.05  # Time step: 0.05 seconds per frame
    S = np.array([0.2, 1.5])  # Right shoulder position (fixed)
    # Wrist position oscillates to simulate waving
    W = np.array([0.2 + A * np.sin(omega * t), 1.2 + B * np.cos(omega * t)])
    # Compute elbow position to maintain biomechanical plausibility
    E = compute_elbow(S, W, L_upper, L_forearm)
    # Update right elbow (index 4) and right wrist (index 6)
    positions[4] = E
    positions[6] = W
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = FuncAnimation(
    fig, update, frames=100, interval=50, blit=True
)

# Display the animation
plt.show()
