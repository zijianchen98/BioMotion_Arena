#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def generate_motion_frames(num_frames=60):
    """
    Generates a sequence of 2D coordinates for 15 point-lights that transition
    from an initial standing posture (sad stance) to a sitting posture.
    Returns a NumPy array of shape (num_frames, 15, 2).
    """
    # Standing posture (sad stance) for 15 points
    p0 = np.array([
        [0.45, 0.10],  # Left foot
        [0.55, 0.10],  # Right foot
        [0.45, 0.30],  # Left knee
        [0.55, 0.30],  # Right knee
        [0.48, 0.45],  # Left hip
        [0.52, 0.45],  # Right hip
        [0.40, 0.55],  # Left hand
        [0.60, 0.55],  # Right hand
        [0.43, 0.55],  # Left elbow
        [0.57, 0.55],  # Right elbow
        [0.46, 0.60],  # Left shoulder
        [0.54, 0.60],  # Right shoulder
        [0.50, 0.62],  # Chest
        [0.50, 0.68],  # Neck
        [0.50, 0.72],  # Head
    ])

    # Sitting posture (sad stance) for 15 points
    p1 = np.array([
        [0.45, 0.10],  # Left foot
        [0.55, 0.10],  # Right foot
        [0.45, 0.25],  # Left knee
        [0.55, 0.25],  # Right knee
        [0.48, 0.30],  # Left hip
        [0.52, 0.30],  # Right hip
        [0.42, 0.42],  # Left hand
        [0.58, 0.42],  # Right hand
        [0.44, 0.45],  # Left elbow
        [0.56, 0.45],  # Right elbow
        [0.47, 0.48],  # Left shoulder
        [0.53, 0.48],  # Right shoulder
        [0.49, 0.50],  # Chest
        [0.49, 0.53],  # Neck
        [0.49, 0.57],  # Head
    ])

    frames = np.zeros((num_frames, 15, 2))
    for i in range(num_frames):
        t = i / (num_frames - 1)
        frames[i] = (1 - t) * p0 + t * p1

        # Optional subtle forward head tilt to enhance "sad" impression
        # Scale tilt by 't' so it's stronger at the final frames
        head_index = 14
        neck_index = 13
        tilt_amount = 0.01 * t
        frames[i, head_index, 0] -= tilt_amount
        frames[i, neck_index, 0] -= tilt_amount / 2

    return frames

def main():
    # Create black figure and axis
    fig, ax = plt.subplots(facecolor='black')
    ax.set_facecolor('black')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    plt.axis('off')

    # Generate motion data
    frames = generate_motion_frames(num_frames=60)

    # Scatter plot for the 15 white points
    scatter = ax.scatter([], [], c='white', s=50)

    def init():
        scatter.set_offsets([])
        return (scatter,)

    def update(frame_index):
        scatter.set_offsets(frames[frame_index])
        return (scatter,)

    ani = FuncAnimation(
        fig, update, frames=len(frames), init_func=init,
        interval=50, blit=True, repeat=True
    )

    plt.show()

if __name__ == "__main__":
    main()