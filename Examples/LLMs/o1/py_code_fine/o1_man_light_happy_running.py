import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of markers
NUM_MARKERS = 15

# Total frames for one cycle
FRAMES_PER_CYCLE = 50

# Total animation frames (multiple cycles)
TOTAL_FRAMES = FRAMES_PER_CYCLE * 4

# Animation interval (milliseconds)
INTERVAL = 30

# Base positions for 15 points (approximate upright neutral pose)
# (x, y) in some arbitrary "body space"
base_positions = np.array([
    [0.0, 1.8],  # Head
    [0.0, 1.6],  # Neck / Shoulder center
    [0.25, 1.6], # Right shoulder
    [0.45, 1.4], # Right elbow
    [0.55, 1.2], # Right wrist
    [-0.25, 1.6],# Left shoulder
    [-0.45, 1.4],# Left elbow
    [-0.55, 1.2],# Left wrist
    [0.15, 1.0], # Right hip
    [0.25, 0.6], # Right knee
    [0.25, 0.2], # Right ankle
    [-0.15, 1.0],# Left hip
    [-0.25, 0.6],# Left knee
    [-0.25, 0.2],# Left ankle
    [0.0, 1.2],  # Torso center
])

# Amplitude factors for how much each point might move
amplitude = np.array([
    0.05,  # head bob
    0.04,
    0.08,
    0.10,
    0.12,
    0.08,
    0.10,
    0.12,
    0.06,
    0.15,
    0.18,
    0.06,
    0.15,
    0.18,
    0.05
])

# Phases to offset motion among points (arms, legs, etc.)
phase_offsets = np.array([
    0.0,
    0.2,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.5,
    0.0,
    0.5,
    0.0,
    0.5,
    0.0,
    0.5,
    0.25
])

def get_positions(frame):
    # t goes from 0 to 1 for each cycle
    t = (frame % FRAMES_PER_CYCLE) / FRAMES_PER_CYCLE
    # Running motion typically has a frequency ~ 2 steps per cycle
    # We'll define a sine-based cycle for arms and legs
    # Overall horizontal speed
    x_speed = 0.05

    # Base horizontal shift as time progresses
    x_shift = x_speed * frame

    # Vertical bobbing of the torso
    body_bob = 0.05 * np.sin(2 * np.pi * t * 2)

    # Construct an overall sine mod for each marker
    # We'll combine a main sine with offsets and amplitude
    theta = 2 * np.pi * (2 * t + phase_offsets)
    sin_motion = amplitude * np.sin(theta)

    # We'll apply sin_motion partly to x, partly to y, to simulate limb swinging
    # For variety, let's do an alternating effect
    dx = sin_motion * (np.arange(NUM_MARKERS) % 2) * 0.5
    dy = sin_motion * (1 - (np.arange(NUM_MARKERS) % 2)) * 0.5

    # Add small up-down bob for the entire figure
    # We'll add the body_bob to everyone's y
    new_positions = base_positions.copy()
    new_positions[:,0] += dx + x_shift
    new_positions[:,1] += dy + body_bob

    return new_positions

def update(frame):
    pts = get_positions(frame)
    scatter.set_offsets(pts)
    return scatter,

fig, ax = plt.subplots(figsize=(6,6))
ax.set_facecolor('black')
ax.set_xlim([-2.0, 4.0])
ax.set_ylim([0.0, 2.5])
ax.axis('off')

# Initial scatter
scatter = ax.scatter(
    base_positions[:,0],
    base_positions[:,1],
    c='white',
    s=50
)

anim = FuncAnimation(
    fig, update, frames=TOTAL_FRAMES, interval=INTERVAL, blit=True, repeat=True
)

plt.show()