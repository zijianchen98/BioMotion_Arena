#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def generate_forward_roll_data(num_frames=60):
    """
    Generate 2D coordinates for 15 point-lights representing
    a simplistic forward roll motion. Returns an array of shape
    (num_frames, 15, 2) where each sub-array corresponds to the
    (x, y) coordinates of 15 joints at a given frame.
    """
    # Set constants
    R = 0.6               # Radius for rolling circle of trunk center
    body_offset_y = 0.8   # Vertical shift so the figure is above the "floor"
    num_points = 15
    data = np.zeros((num_frames, num_points, 2))

    # Define base offsets (relative to trunk center) for each "joint":
    # [head, neck, R_shoulder, R_elbow, R_wrist,
    #  L_shoulder, L_elbow, L_wrist, R_hip, R_knee,
    #  R_foot,     L_hip,   L_knee,  L_foot, pelvis]
    # These are rough static offsets in the trunk's reference frame
    # which we'll rotate (for trunk, arms, legs) to form a simplified
    # rolling motion. Units are fairly arbitrary.
    base_offsets = np.array([
        [ 0.0,  0.30],  # head
        [ 0.0,  0.15],  # neck
        [ 0.15,  0.10], # right shoulder
        [ 0.25,  0.00], # right elbow
        [ 0.30, -0.10], # right wrist
        [-0.15,  0.10], # left shoulder
        [-0.25,  0.00], # left elbow
        [-0.30, -0.10], # left wrist
        [ 0.10, -0.20], # right hip
        [ 0.15, -0.35], # right knee
        [ 0.15, -0.50], # right foot
        [-0.10, -0.20], # left hip
        [-0.15, -0.35], # left knee
        [-0.15, -0.50], # left foot
        [ 0.0,  -0.15], # pelvis
    ])

    # Generate frames
    for i in range(num_frames):
        # t goes from 0 to 1 across all frames
        t = i / num_frames
        # Angle covers one full rotation (2*pi) for a forward roll
        angle = 2 * np.pi * t

        # Trunk center rolling around pivot at (0, 0)
        # so the trunk center is a circle of radius R
        cx = R * np.cos(angle)
        cy = R * np.sin(angle) + body_offset_y

        # For each joint, we define a transformation
        # The trunk "body" rotates with angle. 
        # We'll also add some secondary movement for arms/legs
        # to make it look a bit more dynamic:
        # e.g. arms swing or fold during the roll, using sine waves.
        # This is purely to give a more "biological" feel.
        arm_phase = np.sin(2 * np.pi * (t + 0.2))
        leg_phase = np.cos(2 * np.pi * (t + 0.3))

        # We'll fold these small phases into the base offsets
        # for elbows and knees. Index by the base_offsets list:
        # Right elbow -> index 3, Right knee -> index 9, etc.
        # We'll arbitrarily scale them to keep them small.
        # For a bit of variation:
        new_offsets = np.copy(base_offsets)
        # Right elbow and left elbow (indexes 3, 6)
        new_offsets[3, 1] += 0.05 * arm_phase
        new_offsets[6, 1] += 0.05 * arm_phase
        # Right knee and left knee (indexes 9, 12)
        new_offsets[9, 1] += 0.05 * leg_phase
        new_offsets[12, 1] += 0.05 * leg_phase

        # Build rotation matrix for trunk angle
        rot = np.array([
            [ np.cos(angle), -np.sin(angle)],
            [ np.sin(angle),  np.cos(angle)]
        ])

        # Rotate and translate the 15 offsets
        for j in range(num_points):
            rotated_offset = rot @ new_offsets[j]
            # Translate by trunk center
            px = cx + rotated_offset[0]
            py = cy + rotated_offset[1]
            data[i, j, 0] = px
            data[i, j, 1] = py

    return data


def main():
    # Create black figure and axis
    fig, ax = plt.subplots(figsize=(6, 6))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    # Generate coordinates for rolling motion
    frames_data = generate_forward_roll_data(num_frames=60)
    num_frames, num_points, _ = frames_data.shape

    # Create scatter plot (15 points) for the first frame
    scatter = ax.scatter(
        frames_data[0, :, 0],
        frames_data[0, :, 1],
        c='white',
        s=40
    )
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-0.2, 2.0)
    ax.set_aspect('equal')
    plt.axis('off')

    # Animation update function
    def update(frame):
        scatter.set_offsets(frames_data[frame])
        return (scatter,)

    # Create animation
    ani = FuncAnimation(
        fig,
        update,
        frames=num_frames,
        interval=50,  # 20 fps ~ 50 ms per frame
        blit=True,
        repeat=True
    )

    plt.show()


if __name__ == "__main__":
    main()