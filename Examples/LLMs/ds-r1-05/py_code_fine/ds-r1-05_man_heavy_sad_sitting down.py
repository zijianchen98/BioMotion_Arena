
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Key poses (15 points: head, neck, shoulders, elbows, hands, torso, hips, knees, feet)
standing = [
    (0, 1.6),     # Head
    (0, 1.4),     # Neck
    (-0.2, 1.3),  # Right shoulder
    (-0.35, 1.0), # Right elbow
    (-0.5, 0.7),  # Right hand
    (0.2, 1.3),   # Left shoulder
    (0.35, 1.0),  # Left elbow
    (0.5, 0.7),   # Left hand
    (0, 1.1),     # Torso
    (-0.2, 0.9),  # Right hip
    (-0.2, 0.5),  # Right knee
    (-0.2, 0.1),  # Right foot
    (0.2, 0.9),   # Left hip
    (0.2, 0.5),   # Left knee
    (0.2, 0.1)    # Left foot
]

sitting = [
    (0, 1.0),     # Head
    (0, 0.95),    # Neck
    (-0.2, 0.85), # Right shoulder
    (-0.3, 0.75), # Right elbow
    (-0.35, 0.5), # Right hand
    (0.2, 0.85),  # Left shoulder
    (0.3, 0.75),  # Left elbow
    (0.35, 0.5),  # Left hand
    (0, 0.7),     # Torso
    (-0.2, 0.45), # Right hip
    (-0.25, 0.3), # Right knee
    (-0.2, 0.1),  # Right foot
    (0.2, 0.45),  # Left hip
    (0.25, 0.3),  # Left knee
    (0.2, 0.1)    # Left foot
]

halfway = [
    (0, 1.3),     # Head
    (0, 1.2),     # Neck
    (-0.2, 1.15), # Right shoulder
    (-0.35, 0.95),# Right elbow
    (-0.4, 0.7),  # Right hand
    (0.2, 1.15),  # Left shoulder
    (0.35, 0.95), # Left elbow
    (0.4, 0.7),   # Left hand
    (0, 0.9),     # Torso
    (-0.2, 0.65), # Right hip
    (-0.22, 0.4), # Right knee
    (-0.2, 0.1),  # Right foot
    (0.2, 0.65),  # Left hip
    (0.22, 0.4),  # Left knee
    (0.2, 0.1)    # Left foot
]

# Calculate intermediate control points for smooth motion
P1 = []
for j in range(15):
    px = 2 * halfway[j][0] - 0.5 * standing[j][0] - 0.5 * sitting[j][0]
    py = 2 * halfway[j][1] - 0.5 * standing[j][1] - 0.5 * sitting[j][1]
    P1.append((px, py))

# Animation parameters
total_frames = 60
total_cycle_frames = 2 * total_frames
interval_time = 20  # ms per frame (~50 FPS)

# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-0.7, 0.7)
ax.set_ylim(0, 1.8)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
scat = ax.scatter([], [], color='white', s=70)

# Animation update function
def update(frame):
    # Calculate normalized time (0->1: sit down, 1->0: stand up)
    t_val = 1 - abs((frame % total_cycle_frames) / total_frames - 1)
    
    # Update point positions using quadratic Bezier interpolation
    points = []
    for j in range(15):
        x0, y0 = standing[j]
        x1, y1 = P1[j]
        x2, y2 = sitting[j]
        x = (1-t_val)**2 * x0 + 2*(1-t_val)*t_val * x1 + t_val**2 * x2
        y = (1-t_val)**2 * y0 + 2*(1-t_val)*t_val * y1 + t_val**2 * y2
        points.append([x, y])
    scat.set_offsets(points)
    return [scat]

# Create and show animation
ani = FuncAnimation(fig, update, frames=total_cycle_frames,
                    interval=interval_time, blit=True, repeat=True)
plt.show()
