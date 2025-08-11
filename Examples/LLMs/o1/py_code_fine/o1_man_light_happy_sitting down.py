#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def generate_sitting_motion(num_frames=60):
    """
    Generates a simple 2D point-light motion (15 points) from a standing posture
    to a sitting posture. Returns a NumPy array of shape (num_frames, 15, 2).
    """

    # Define 15 keypoints for the initial standing posture (x, y)
    # Head, Torso center, Right shoulder, Left shoulder, Right elbow, Left elbow,
    # Right wrist, Left wrist, Pelvis center, Right hip, Left hip,
    # Right knee, Left knee, Right ankle, Left ankle
    start_points = np.array([
        [ 0.00, 1.80],  # 1. Head
        [ 0.00, 1.50],  # 2. Torso center
        [ 0.20, 1.50],  # 3. Right shoulder
        [-0.20, 1.50],  # 4. Left shoulder
        [ 0.30, 1.40],  # 5. Right elbow
        [-0.30, 1.40],  # 6. Left elbow
        [ 0.30, 1.20],  # 7. Right wrist
        [-0.30, 1.20],  # 8. Left wrist
        [ 0.00, 1.00],  # 9. Pelvis center
        [ 0.10, 1.00],  # 10. Right hip
        [-0.10, 1.00],  # 11. Left hip
        [ 0.15, 0.60],  # 12. Right knee
        [-0.15, 0.60],  # 13. Left knee
        [ 0.15, 0.10],  # 14. Right ankle
        [-0.15, 0.10],  # 15. Left ankle
    ])

    # Define 15 keypoints for the final sitting posture (x, y)
    end_points = np.array([
        [ 0.00, 1.50],  # 1. Head (lowered slightly)
        [ 0.00, 1.30],  # 2. Torso center
        [ 0.20, 1.30],  # 3. Right shoulder
        [-0.20, 1.30],  # 4. Left shoulder
        [ 0.30, 1.10],  # 5. Right elbow
        [-0.30, 1.10],  # 6. Left elbow
        [ 0.30, 0.90],  # 7. Right wrist
        [-0.30, 0.90],  # 8. Left wrist
        [ 0.00, 0.80],  # 9. Pelvis center
        [ 0.10, 0.80],  # 10. Right hip
        [-0.10, 0.80],  # 11. Left hip
        [ 0.15, 0.50],  # 12. Right knee
        [-0.15, 0.50],  # 13. Left knee
        [ 0.15, 0.20],  # 14. Right ankle
        [-0.15, 0.20],  # 15. Left ankle
    ])

    # Interpolate linearly between standing and sitting for num_frames
    frames = np.zeros((num_frames, 15, 2))
    for i in range(num_frames):
        t = i / (num_frames - 1)
        frames[i] = (1 - t) * start_points + t * end_points

    return frames

def main():
    # Generate frames for the sitting-down motion
    num_frames = 60
    motion_data = generate_sitting_motion(num_frames)

    # Set up the figure and axes
    fig, ax = plt.subplots()
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(0.0, 2.0)
    ax.axis("off")

    # Create a scatter plot for the 15 points (initially at the first frame)
    scatter = ax.scatter(
        motion_data[0, :, 0],
        motion_data[0, :, 1],
        c="white",
        s=30
    )

    # Update function for animation
    def update(frame_idx):
        scatter.set_offsets(motion_data[frame_idx])
        return (scatter,)

    # Create the animation
    ani = FuncAnimation(
        fig,
        update,
        frames=num_frames,
        interval=50,  # adjust for desired speed (ms)
        blit=True,
        repeat=True
    )

    plt.show()

if __name__ == "__main__":
    main()