import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of frames in the animation
N_FRAMES = 60

# Number of points (15 white point-lights)
N_POINTS = 15

def generate_jump_data(num_frames=N_FRAMES):
    """
    Returns a (num_frames, N_POINTS, 2) array of x,y positions
    for 15 point-lights depicting a simplified forward jump.
    """
    data = np.zeros((num_frames, N_POINTS, 2))

    # Time array (0 to 1)
    t_vals = np.linspace(0, 1, num_frames)
    
    for i, t in enumerate(t_vals):
        # Center of mass (pelvis) motion in x
        # Move from x=0 to x=3 over t in [0,1]
        x_cm = 3 * t
        
        # Center of mass (pelvis) motion in y (simple sine-based jump)
        # Jump occurs between t=0.2 and t=0.8
        if 0.2 <= t <= 0.8:
            phase = (t - 0.2) / 0.6  # map [0.2,0.8] -> [0,1]
            y_cm = np.sin(np.pi * phase)  # peak at t=0.5
        else:
            y_cm = 0.0
        
        # Pelvis as point 0
        data[i, 0] = [x_cm, y_cm]
        
        # Torso (slightly above pelvis)
        data[i, 1] = [x_cm, y_cm + 0.4]
        
        # Head (above torso)
        data[i, 2] = [x_cm, y_cm + 0.8]
        
        # Left shoulder
        data[i, 3] = [x_cm - 0.15, y_cm + 0.4]
        # Right shoulder
        data[i, 4] = [x_cm + 0.15, y_cm + 0.4]
        
        # Left elbow
        data[i, 5] = [x_cm - 0.15, y_cm + 0.25]
        # Right elbow
        data[i, 6] = [x_cm + 0.15, y_cm + 0.25]
        
        # Left wrist
        data[i, 7] = [x_cm - 0.15, y_cm + 0.1]
        # Right wrist
        data[i, 8] = [x_cm + 0.15, y_cm + 0.1]
        
        # Left hip
        data[i, 9]  = [x_cm - 0.1, y_cm]
        # Right hip
        data[i, 10] = [x_cm + 0.1, y_cm]
        
        # Simulate knee bend based on jump phase
        # Knees will bend more at the start/end of jump
        knee_bend = 0.25 if (t < 0.2 or t > 0.8) else 0.05
        
        # Left knee
        data[i, 11] = [x_cm - 0.1, y_cm - 0.25 - knee_bend]
        # Right knee
        data[i, 12] = [x_cm + 0.1, y_cm - 0.25 - knee_bend]
        
        # Left ankle
        data[i, 13] = [x_cm - 0.1, y_cm - 0.5 - knee_bend]
        # Right ankle
        data[i, 14] = [x_cm + 0.1, y_cm - 0.5 - knee_bend]
    
    return data

# Generate frames for the jump
frames_data = generate_jump_data()

# Create figure with black background
fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Set axis limits (to comfortably see the jump)
ax.set_xlim(-1, 4)
ax.set_ylim(-1.5, 2)

# Remove axes for a cleaner "point-light" look
ax.axis('off')

# Create scatter for 15 points (white color)
scat = ax.scatter(
    frames_data[0, :, 0],
    frames_data[0, :, 1],
    c='white',
    s=50
)

def update(frame_index):
    scat.set_offsets(frames_data[frame_index])
    return scat,

ani = FuncAnimation(
    fig,
    update,
    frames=N_FRAMES,
    interval=50,  # 20 fps if 50 ms interval
    blit=True,
    repeat=True
)

plt.show()