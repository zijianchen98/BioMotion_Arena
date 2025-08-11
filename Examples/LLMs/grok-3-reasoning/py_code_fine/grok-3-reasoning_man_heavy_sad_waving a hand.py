
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define fixed positions
positions = np.array([
    [0,7.5],  # head
    [0,6.5],  # neck
    [-0.5,5.5],  # left shoulder
    [0.5,5.5],  # right shoulder
    [-0.6,5],  # left elbow
    [0,0],  # right elbow, to be updated
    [-0.7,4],  # left wrist
    [0,0],  # right wrist, to be updated
    [0,4.5],  # torso center
    [-0.5,3.5],  # left hip
    [0.5,3.5],  # right hip
    [-0.5,1.5],  # left knee
    [0.5,1.5],  # right knee
    [-0.5,0],  # left ankle
    [0.5,0]   # right ankle
])

# Function to compute elbow position
def compute_elbow(S, W, L1, L2):
    V = W - S
    d = np.linalg.norm(V)
    a = (L1**2 - L2**2 + d**2) / (2*d)
    h = np.sqrt(L1**2 - a**2)
    V_unit = V / d
    U = np.array([-V_unit[1], V_unit[0]])  # perpendicular vector
    P = S + a * V_unit
    E1 = P + h * U
    E2 = P - h * U
    # Choose the one with lower y-coordinate
    if E1[1] < E2[1]:
        return E1
    else:
        return E2

# Set up the figure
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-3,3)
ax.set_ylim(0,8)
ax.set_axis_off()

# Initial scatter plot
scatter = ax.scatter(positions[:,0], positions[:,1], color='white', s=50)

# Animation function
def animate(i):
    # Compute right wrist position
    wx = 1.5 + 0.5 * np.sin(2*np.pi*i / 60)
    wy = 5
    W = np.array([wx, wy])
    S = positions[3]  # right shoulder
    E = compute_elbow(S, W, 1, 1)
    positions[5] = E
    positions[7] = W
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = FuncAnimation(fig, animate, frames=150, interval=33, blit=True)

plt.show()
