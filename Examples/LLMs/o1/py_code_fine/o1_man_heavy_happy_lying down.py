import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def generate_frames(num_frames=100):
    """
    Generate a numpy array of shape (num_frames, 15, 2) representing
    the 2D positions of 15 point-lights over time.
    In this example, the figure is 'lying down' on the x-axis, with a small
    'breathing' or 'waving arms' motion for demonstration.
    """
    frames = np.zeros((num_frames, 15, 2))

    # Base/initial positions (lying horizontally around y=0),
    # indexing each point: [head, chest, pelvis, L-shoulder, R-shoulder, L-elbow,
    # R-elbow, L-wrist, R-wrist, L-hip, R-hip, L-knee, R-knee, L-ankle, R-ankle]
    # These positions form a simple "body" shape lying on its back.
    base_positions = np.array([
        [0.0,  1.0],  # Head
        [0.0,  0.5],  # Chest
        [0.0,  0.0],  # Pelvis
        [-0.4, 0.5],  # Left shoulder
        [ 0.4, 0.5],  # Right shoulder
        [-0.6, 0.5],  # Left elbow
        [ 0.6, 0.5],  # Right elbow
        [-0.8, 0.5],  # Left wrist
        [ 0.8, 0.5],  # Right wrist
        [-0.2, 0.0],  # Left hip
        [ 0.2, 0.0],  # Right hip
        [-0.3,-0.5],  # Left knee
        [ 0.3,-0.5],  # Right knee
        [-0.3,-1.0],  # Left ankle
        [ 0.3,-1.0],  # Right ankle
    ])

    # Generate frames with a small vertical oscillation to simulate
    # breathing or pushing motion while lying down
    for i in range(num_frames):
        t = i / (num_frames - 1)
        # Simple sinusoidal offset
        breathing_offset = 0.05 * np.sin(2 * np.pi * t * 2)  # 2 cycles
        # Arms wave slightly
        arm_wave = 0.15 * np.sin(2 * np.pi * t * 2)

        # Copy the base positions
        current = base_positions.copy()

        # Chest and pelvis move slightly up and down
        current[1, 1] += breathing_offset
        current[2, 1] += breathing_offset * 0.8

        # Left wrist and right wrist move up/down to simulate arm movement
        current[7, 1] += arm_wave
        current[8, 1] += arm_wave

        frames[i] = current

    return frames

def main():
    # Generate the data for animation
    frames = generate_frames(num_frames=100)

    # Set up the figure and axes (black background, no axes)
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.axis('off')

    # Scatter for the 15 points
    scatter = ax.scatter(
        frames[0, :, 0],
        frames[0, :, 1],
        c='white',
        s=50
    )

    # Animation update function
    def update(frame_idx):
        scatter.set_offsets(frames[frame_idx])
        return (scatter,)

    anim = FuncAnimation(
        fig,
        update,
        frames=range(len(frames)),
        interval=50,
        blit=True
    )

    plt.show()

if __name__ == "__main__":
    main()